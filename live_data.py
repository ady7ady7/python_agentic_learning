from dotenv import load_dotenv
import os
import requests
import pandas as pd


def get_recent_bars(symbol: str, interval: str) -> pd.DataFrame:
    load_dotenv()
    API_KEY = os.getenv('TWELVEDATA_API_KEY')

    response = requests.get('https://api.twelvedata.com/time_series', params = {
        'symbol': symbol,
        'interval': interval,
        'outputsize': 5,
        'timezone': 'America/New_York',
        'apikey': API_KEY 
    })
    
    if response.status_code != 200:
        raise RuntimeError(f'API Error: {response.status_code}: {response.text}')

    data = response.json()

    if data.get('status') == 'error':
        raise RuntimeError(f'Twelve Data API error: {data.get('message')}')
    
    data = pd.DataFrame(data['values'])
    return data