import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()
DB_URL = f"postgresql://{os.environ['DB_USER']}:{os.environ['DB_PASSWORD']}@{os.environ['DB_HOST']}:{os.environ['DB_PORT']}/{os.environ['DB_NAME']}"
OUTPUT_DIR = "data/"

CARRIER_GRADES = ('Verizon', 'AT&T', 'T-Mobile', 'Cricket', 'Tracfone', 'Boost Mobile')

engine = create_engine(DB_URL)

print("Exporting price_history...")
price_query = """
    SELECT
        p.asin,
        p.storage_gb,
        p.color,
        p.product_grade,
        s.submodel_name,
        g.brand,
        g.generation_name,
        g.premiere_date,
        ph.datetime,
        ph.new_price / 100.0  AS new_price,
        ph.amazon    / 100.0  AS amazon,
        ph.used_price / 100.0 AS used_price,
        ph.list_price / 100.0 AS list_price,
        ph.sales_rank,
        ph.count_new,
        ph.count_used
    FROM keepa.price_history ph
    JOIN keepa.products  p ON ph.product_id  = p.id
    JOIN keepa.submodels s ON p.submodel_id  = s.id
    JOIN keepa.generations g ON s.generation_id = g.id
    WHERE ph.new_price IS NOT NULL
      AND p.product_grade NOT IN %(carrier_grades)s
    ORDER BY g.brand, s.submodel_name, p.asin, ph.datetime
"""

df_prices = pd.read_sql(price_query, engine, params={"carrier_grades": CARRIER_GRADES})
print(f"  Rows: {len(df_prices):,}")
df_prices.to_csv(OUTPUT_DIR + "price_history_full.csv", index=False)
print("  Saved: data/price_history_full.csv")

print("Exporting monthly_sold...")
sold_query = """
    SELECT
        p.asin,
        p.product_grade,
        s.submodel_name,
        g.brand,
        g.generation_name,
        g.premiere_date,
        ms.datetime,
        ms.monthly_sold
    FROM keepa.monthly_sold ms
    JOIN keepa.products  p ON ms.product_id   = p.id
    JOIN keepa.submodels s ON p.submodel_id   = s.id
    JOIN keepa.generations g ON s.generation_id = g.id
    WHERE p.product_grade NOT IN %(carrier_grades)s
    ORDER BY g.brand, s.submodel_name, p.asin, ms.datetime
"""

df_sold = pd.read_sql(sold_query, engine, params={"carrier_grades": CARRIER_GRADES})
print(f"  Rows: {len(df_sold):,}")
df_sold.to_csv(OUTPUT_DIR + "monthly_sold_full.csv", index=False)
print("  Saved: data/monthly_sold_full.csv")

print("Exporting all_asins_meta...")
meta_query = """
    SELECT
        p.asin,
        p.storage_gb,
        p.color,
        p.product_grade,
        p.listed_since,
        p.tracking_since,
        s.submodel_name,
        g.brand,
        g.generation_name,
        g.premiere_date
    FROM keepa.products p
    JOIN keepa.submodels s ON p.submodel_id = s.id
    JOIN keepa.generations g ON s.generation_id = g.id
    WHERE p.product_grade NOT IN %(carrier_grades)s
    ORDER BY g.brand, g.generation_name, s.submodel_name, p.asin
"""

df_meta = pd.read_sql(meta_query, engine, params={"carrier_grades": CARRIER_GRADES})
print(f"  Rows: {len(df_meta):,}")
df_meta.to_csv(OUTPUT_DIR + "all_asins_meta.csv", index=False)
print("  Saved: data/all_asins_meta.csv")

print("Done.")
