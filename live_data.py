from dotenv import load_dotenv
import os
import requests
import time
import pandas as pd
import numpy as np

import datetime as dt
from zoneinfo import ZoneInfo
from typing import List, Tuple



RETRYABLE = {429, 500, 502, 503, 504}

def get_recent_bars(symbol: str, interval: str) -> pd.DataFrame:
    load_dotenv()
    API_KEY = os.getenv('TWELVEDATA_API_KEY')

    response = get_with_retry(url = 'https://api.twelvedata.com/time_series',
                              params = 
                              {
                                    'symbol': symbol,
                                    'interval': interval,
                                    'outputsize': 500,
                                    'timezone': 'America/New_York',
                                    'apikey': API_KEY
                               },
                              max_attempts = 4 
                              )
    if response.status_code != 200:
        raise RuntimeError(f'API Error: {response.status_code}: {response.text}')

    data = response.json()

    if data.get('status') == 'error':
        raise RuntimeError(f'Twelve Data API error: {data.get('message')}')
    
    data = pd.DataFrame(data['values'])
    return data


def get_with_retry(url, params, max_attempts=4):
    for attempt in range(1, max_attempts + 1):
        try:
            response = requests.get(url, params=params, timeout=10)
        except (requests.ConnectionError, requests.Timeout) as e:   # no response at all
            if attempt == max_attempts:
                raise RuntimeError(f'Network error after {max_attempts} attempts: {e}')
        else:                                                        # we got a response
            if response.status_code not in RETRYABLE:
                return response          # 200, or a permanent error like 401 - caller decides
            if attempt == max_attempts:
                return response          # still 429/5xx after all attempts
        time.sleep(2 ** attempt)         # 2, 4, 8 s



def otf_streak(highs: List, lows: List) -> List:
    otf_streaks = [0] * len(highs)
    for i in range(1, len(otf_streaks)):
        if (lows[i] > lows[i-1]) and (highs[i] < highs[i-1]):
            otf_streaks[i] = otf_streaks[i-1]
        elif lows[i] > lows[i-1]:
            otf_streaks[i] = 1 if otf_streaks[i-1] < 0 else otf_streaks[i-1] + 1
        elif highs[i] < highs[i-1]:
            otf_streaks[i] = -1 if otf_streaks[i-1] > 0 else otf_streaks[i-1] - 1
    return otf_streaks

def center_of_mass(abs_returns_window):
    n = len(abs_returns_window)
    positions = np.arange(1, n + 1)
    total_weight = np.sum(abs_returns_window)
    if total_weight == 0:
        return 0.0
    raw_com = np.sum(positions * abs_returns_window) / total_weight
    center = (n + 1) / 2
    radius = (n - 1) / 2
    return (raw_com - center) / radius




def get_live_observation_features(data: pd.DataFrame) -> Tuple[dict, float]:
    '''
    Receives OHLC candle data - here it's fetched from TwelveData API
    Then it converts data and calculates relevant features.
    
    Returns a dict of calculated features ready for predictions
    + ALSO latest close (as I need it for actual range predictions based on quantiles and range-per-point historical checks)
    
    Current set of features (updated 9.11.2026, as I've tested some more features)
    [
        'log_power_obs', 
        'log_atr14_obs', 
        'center_of_mass_mean_observation', 
        'log_parkinson_obs', 
        'log_har_d', 
        'is_cpi',
        'is_nfp',
        'is_thursday'
        ]
    
    '''
    
    
    
    data = data.sort_values('datetime').reset_index(drop=True)
    data['hour'] = pd.to_datetime(data['datetime']).dt.hour
    data['minute'] = pd.to_datetime(data['datetime']).dt.minute
    data['trade_date'] = pd.to_datetime(data['datetime']).dt.date

    current_time = dt.datetime.now(ZoneInfo('America/New_York')) #adjusted to ET timezone
    current_hour = current_time.hour
    current_minute = current_time.minute
    current_date = current_time.date()
    print(f'Current time: {current_time}, hour: {current_hour}, minute: {current_minute}, date: {current_date}')



    ###FEATURES CALC
    data['close'] = data['close'].astype('float')
    data['open'] = data['open'].astype('float')
    data['high'] = data['high'].astype('float')
    data['low'] = data['low'].astype('float')

    # realized_power
    data['ret_1bar'] = data['close'].pct_change()
    data['abs_ret_1bar'] = data['ret_1bar'].abs()
    
    #parkinson volatility
    data['parkinson_volatility'] = (np.log(data['high'] / data['low']) ** 2) / (4 * np.log(2))
    

    # atr14 (Wilder ATR, 14-period) - M5 file has no atr14 column, built fresh here
    data['prev_close'] = data['close'].shift(1)
    data['tr'] = data[['high', 'low', 'prev_close']].apply(
    lambda row: max(row['high'] - row['low'],
        abs(row['high'] - row['prev_close']),
        abs(row['low'] - row['prev_close'])), axis=1)
    data['atr14'] = data['tr'].ewm(alpha=1/14, adjust=False).mean()

    # otf_streak - exact function from Week 9 Day 1, unchanged
    data['otf_streak'] = otf_streak(data['high'].tolist(), data['low'].tolist())

    # atr_trend (1 if atr rising over last 5 bars, else 0 - same def as Week 8)
    data['atr_trend'] = (data['atr14'] - data['atr14'].shift(5) > 0).astype(int)

    # efficiency_ratio_10, sjv_10, center_of_mass, wtc_10 - same window-10 defs as Week 8 Day 3
    data['net_displacement_10'] = data['ret_1bar'].rolling(10).sum().abs()
    data['realized_power_10'] = data['abs_ret_1bar'].rolling(10).sum()
    data['efficiency_ratio_10'] = data['net_displacement_10'] / data['realized_power_10']

    data['sq_ret_pos_10'] = (data['ret_1bar'].where(data['ret_1bar'] > 0, 0) ** 2).rolling(10).sum()
    data['sq_ret_neg_10'] = (data['ret_1bar'].where(data['ret_1bar'] < 0, 0) ** 2).rolling(10).sum()
    data['sjv_10'] = (data['sq_ret_pos_10'] - data['sq_ret_neg_10']) / (data['sq_ret_pos_10'] + data['sq_ret_neg_10'])


    data['center_of_mass'] = data['abs_ret_1bar'].rolling(10).apply(center_of_mass, raw=True)

    data['wtc_10'] = np.log(data['high'] / data['low']).rolling(10).sum() / data['realized_power_10']




    ##########
    prediction_window = data.loc[
    (data['hour'] == current_hour) & 
    (data['trade_date'] == current_date) &
    (data['minute'].between(0, 10))
    ]

    prediction_window_agg = prediction_window.groupby('trade_date').agg(
    realized_power_observation = ('abs_ret_1bar', 'sum'),
    atr14_mean_observation = ('atr14', 'mean'),
    otf_streak_observation = ('otf_streak', 'last'),
    sjv_10_observation = ('sjv_10', 'mean'),
    efficiency_ratio_10_observation = ('efficiency_ratio_10', 'mean'),
    wtc_10_observation = ('wtc_10', 'mean'),
    center_of_mass_mean_observation = ('center_of_mass', 'mean'),
    atr_trend_observation = ('atr_trend', 'last'),
    parkinson_obs = ('parkinson_volatility', 'sum')
    ).reset_index()

    #
    prediction_window_agg['log_parkinson_obs'] = np.log(prediction_window_agg['parkinson_obs'])
    prediction_window_agg['log_atr14_obs'] = np.log(prediction_window_agg['atr14_mean_observation'])
    prediction_window_agg['log_power_obs'] = np.log(prediction_window_agg['realized_power_observation'])


    # świece z minut 15-59 bieżącej godziny, ale tylko z dni PRZED dzisiaj
    prev_window = data.loc[
        (data['hour'] == current_hour) &
        (data['minute'] >= 15) &
        (data['trade_date'] < current_date)
    ]
    prev_date = prev_window['trade_date'].max()     # najpóźniejszy z tych dni = poprzedni dzień handlowy
    har_d_power = prev_window.loc[prev_window['trade_date'] == prev_date, 'abs_ret_1bar'].sum()
    if har_d_power == 0:
        raise RuntimeError(f'No previous-day bars for hour {current_hour} - cannot compute log_har_d')
    prediction_window_agg['log_har_d'] = np.log(har_d_power)
    
    
    ####added the news releases segment
    
    ###added the news releases segment, as it clearly shows a signal as well
    news_releases = pd.read_csv('./macro_releases.csv')
    news_releases['date'] = pd.to_datetime(news_releases['date'])

    nfp_dates = news_releases.loc[news_releases['event'] == 'NFP', 'date']
    cpi_dates = news_releases.loc[news_releases['event'] == 'CPI', 'date']
    fomc_dates = news_releases.loc[news_releases['event'] == 'FOMC', 'date']

    prediction_window_agg['trade_date'] = pd.to_datetime(prediction_window_agg['trade_date'])
    prediction_window_agg['day_of_week'] = prediction_window_agg['trade_date'].dt.day_of_week
    # releases (and Thursday jobless claims) are at 8:30 ET - the model learned their effect
    # only for the 8:15-9:00 window, at other hours the effect is ~1.0x, so flags = 0 there
    is_8am = int(current_hour == 8)
    prediction_window_agg['is_nfp'] = prediction_window_agg['trade_date'].isin(nfp_dates).astype(int) * is_8am
    prediction_window_agg['is_cpi'] = prediction_window_agg['trade_date'].isin(cpi_dates).astype(int) * is_8am
    # FOMC: no dates in macro_releases.csv yet and not in the model - always 0 for now
    prediction_window_agg['is_fomc'] = prediction_window_agg['trade_date'].isin(fomc_dates).astype(int)
    prediction_window_agg['is_thursday'] = (prediction_window_agg['day_of_week'] == 3).astype(int) * is_8am

    prediction_window_agg = prediction_window_agg.drop(columns = 'trade_date')
    return prediction_window_agg.iloc[0].to_dict(), prediction_window['close'].iloc[-1]

