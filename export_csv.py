import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv(r"project2_xauusd_analysis\.env")

engine = create_engine(
    f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT', 5432)}/{os.getenv('DB_NAME')}"
)

query = """
SELECT
    timestamp AT TIME ZONE 'America/New_York' AS et_time,
    open, high, low, close, volume,
    EXTRACT(DOW FROM timestamp AT TIME ZONE 'America/New_York') AS day_of_week,
    (timestamp AT TIME ZONE 'America/New_York')::date AS trade_date
FROM xauusd_m5_tradfi_ohlcv
ORDER BY timestamp
"""

print("Fetching data...")
df = pd.read_sql(query, engine)
df = df[df['et_time'].dt.dayofweek != 6].copy()
print(f"Rows: {len(df)}")

df.to_csv("xauusd_m5_et.csv", index=False)
print(f"Full dataset saved: xauusd_m5_et.csv ({os.path.getsize('xauusd_m5_et.csv') / 1024 / 1024:.1f} MB)")

df.head(10).to_csv("xauusd_m5_et_example.csv", index=False)
print("Example file saved: xauusd_m5_et_example.csv")
