import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
from extract import search_every_commodities

load_dotenv()

DB_HOST = os.getenv('DB_HOST_PROD')
DB_PORT = os.getenv('DB_PORT_PROD')
DB_NAME = os.getenv('DB_NAME_PROD')
DB_USER = os.getenv('DB_USER_PROD')
DB_PASS = os.getenv('DB_PASS_PROD')
DB_SCHEMA = os.getenv('DB_SCHEMA_PROD')

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)


commodities = [
    'BTC-USD',
    'ETH-USD'
]

def save_date_to_postgres(df, schema = 'public'):
    df.to_sql('commodities', engine, if_exists = 'replace', index = True, index_label = 'Date', schema = schema)

if __name__ == "__main__":
    df = search_every_commodities(commodities)
    save_date_to_postgres(df)