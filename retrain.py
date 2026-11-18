
import pandas as pd
import numpy as np
from typing import List

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

FEATURES = ['log_power_obs', 'log_atr14_obs', 'center_of_mass_mean_observation',
        'log_parkinson_obs', 'log_har_d', 'is_cpi', 'is_nfp', 'is_thursday']
TARGET = 'target_log_ratio'


def center_of_mass(abs_returns_window):
        '''Helper function used to calculate the center of mass used in calculations
        in build_training_table()
        
        I took this one from the internet, but it checks the center of price movement zone for a given window
        '''
        n = len(abs_returns_window)
        positions = np.arange(1, n + 1)
        total_weight = np.sum(abs_returns_window)
        if total_weight == 0:
            return 0.0
        raw_com = np.sum(positions * abs_returns_window) / total_weight
        center = (n + 1) / 2
        radius = (n - 1) / 2
        return (raw_com - center) / radius

def build_training_table(m5_path: str, macro_path: str) -> pd.DataFrame:
    
    '''
    Function take the path to m5 csv data in et_time + path to macro releases calendar (currently NFP/CPI)
    
    Example m5 csv format:
    
    et_time,open,high,low,close,volume,day_of_week,trade_date
    2021-01-04 01:00:00,1921.648,1922.658,1921.448,1922.305,0.2,1.0,2021-01-04


    Example macro_releases csv format:
    date,event
    2021-01-08,NFP
    2021-01-13,CPI
        
    Function returns one row per trading day with trade date:
    - the 8 model features + target_log_ratio
    '''

    m5_df = pd.read_csv(m5_path, parse_dates = ['et_time'])

    # per-bar inputs
    m5_df['abs_ret_1bar'] = m5_df['close'].pct_change().abs()

    # atr14 (Wilder ATR, 14-period)
    m5_df['prev_close'] = m5_df['close'].shift(1)
    m5_df['tr'] = m5_df[['high', 'low', 'prev_close']].apply(
        lambda row: max(row['high'] - row['low'],
                        abs(row['high'] - row['prev_close']),
                        abs(row['low'] - row['prev_close'])), axis=1)
    m5_df['atr14'] = m5_df['tr'].ewm(alpha=1/14, adjust=False).mean()

    m5_df['center_of_mass'] = m5_df['abs_ret_1bar'].rolling(10).apply(center_of_mass, raw=True)
    m5_df['parkinson_volatility'] = (np.log(m5_df['high'] / m5_df['low']) ** 2) / (4 * np.log(2))

    # windows: observation 8:00-8:15, prediction 8:15-9:00 ET
    m5_df['is_obs'] = (m5_df['et_time'].dt.hour == 8) & (m5_df['et_time'].dt.minute < 15)
    m5_df['is_pred'] = (m5_df['et_time'].dt.hour == 8) & (m5_df['et_time'].dt.minute >= 15)

    observation_window = m5_df[m5_df['is_obs']].groupby('trade_date').agg(
        realized_power_observation = ('abs_ret_1bar', 'sum'),
        atr14_mean_observation = ('atr14', 'mean'),
        center_of_mass_mean_observation = ('center_of_mass', 'mean'),
        parkinson_obs = ('parkinson_volatility', 'sum')
    ).reset_index()

    predicted_window = m5_df[m5_df['is_pred']].groupby('trade_date').agg(
        realized_power_predicted = ('abs_ret_1bar', 'sum')
    ).reset_index()

    merged_df = observation_window.merge(predicted_window, how = 'inner', on = 'trade_date')

    # features
    merged_df['log_parkinson_obs'] = np.log(merged_df['parkinson_obs'])
    merged_df['log_atr14_obs'] = np.log(merged_df['atr14_mean_observation'])
    merged_df['log_power_obs'] = np.log(merged_df['realized_power_observation'])
    merged_df['log_har_d'] = np.log(merged_df['realized_power_predicted'].shift(1))

    news_releases = pd.read_csv(macro_path, parse_dates = ['date'])
    nfp_dates = news_releases.loc[news_releases['event'] == 'NFP', 'date']
    cpi_dates = news_releases.loc[news_releases['event'] == 'CPI', 'date']

    merged_df['trade_date'] = pd.to_datetime(merged_df['trade_date'])
    merged_df['is_nfp'] = merged_df['trade_date'].isin(nfp_dates).astype(int)
    merged_df['is_cpi'] = merged_df['trade_date'].isin(cpi_dates).astype(int)
    merged_df['is_thursday'] = (merged_df['trade_date'].dt.day_of_week == 3).astype(int)

    # target
    merged_df['target_log_ratio'] = np.log(merged_df['realized_power_predicted'] / merged_df['realized_power_observation'])

    merged_df = merged_df.dropna(subset = FEATURES + [TARGET])
    return merged_df[['trade_date'] + FEATURES + [TARGET]].reset_index(drop = True)


def train_and_evaluate(table: pd.DataFrame) -> tuple:
    
    '''
    This function obtains the DF, splits the data into train/test data (80/20, no shuffling, manual split here),
    it trains LinearRegression(standard params) and then calculates model's performance
    
    It returns a tuple:
    - model
    - dict with n_rows(test data), first_date (test data), last_date, baseline_mae, test_mae, test_r2
    
    
    '''
    
    train = table[:int(0.8*(len(table)))]
    test = table[int(0.8*(len(table))):]
    model = LinearRegression()
    model.fit(train[FEATURES], train[TARGET])
    
    baseline_mae = np.full(len(test), train[TARGET].mean())
    baseline_mae = mean_absolute_error(baseline_mae, test[TARGET])
    
    n_rows = len(test)
    first_date = min(pd.to_datetime(test['trade_date']))
    last_date = max(pd.to_datetime(test['trade_date']))
    
    predictions = model.predict(test[FEATURES])
    
    test_mae = mean_absolute_error(test[TARGET], predictions)
    test_r2 = r2_score(test[TARGET], predictions)
    
    
    metrics = {
        'n_rows': n_rows,
        'first_date': first_date,
        'last_date': last_date,
        'baseline_mae': baseline_mae,
        'test_mae': test_mae,
        'test_r2': test_r2
    }
    
    return model, metrics



if __name__ == '__main__':
    df = build_training_table(m5_path = './xauusd_m5_et.csv', macro_path = './macro_releases.csv')
    model, metrics = train_and_evaluate(df)
    print(f'Model: {model}')
    print(f'Metrics: {metrics}')