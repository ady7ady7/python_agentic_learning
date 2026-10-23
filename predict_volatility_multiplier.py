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



    
    
    