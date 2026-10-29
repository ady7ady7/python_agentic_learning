import mlflow
import numpy as np
import pandas as pd

RUN_ID = '106b7bdcd4414cff940351cb351dab33'

def load_model():
    mlflow.set_tracking_uri('sqlite:///mlflow.db')
    return mlflow.sklearn.load_model(f'runs:/{RUN_ID}/model')

def predict_volatility(model, observation_features: dict) -> float:
    '''
    observation features:
    dict with the 9 feature names as keys (same order-independent, since we build a one row DF from it)
    
    '''
    row = pd.DataFrame([observation_features])
    log_ratio = model.predict(row)[0]
    return float(np.exp(log_ratio))




def calibrate_range_bounds(predicted_power: float, last_close: float) -> dict:
    """
    predicted_power: power_obs * model's predicted multiplier (already computed)
    last_close: close of the most recent CLOSED bar in the observation window
    Returns four price levels per band - NOT a directional forecast, a symmetric
    width estimate around last_close (direction is never predicted).
    """
    k_p75, k_p90 = 2079.53, 2961.72 #hardcoded 75th and 90th percentile of a range to power ratio 
    
    range_points_p75 = predicted_power * k_p75
    range_points_p90 = predicted_power * k_p90
    
    typical_low = last_close - range_points_p75 / 2
    typical_high = last_close + range_points_p75 / 2

    wide_low = last_close - range_points_p90 / 2
    wide_high = last_close + range_points_p90 / 2
        
    return typical_low, typical_high, wide_low, wide_high

        
        
    
    
    