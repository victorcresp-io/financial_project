import os
import unittest

import psycopg2
from dotenv import load_dotenv

load_dotenv('src/.env')

DB_HOST = os.getenv('DB_HOST_PROD')
DB_PORT = os.getenv('DB_PORT_PROD')
DB_NAME = os.getenv('DB_NAME_PROD')
DB_USER = os.getenv('DB_USER_PROD')
DB_PASS = os.getenv('DB_PASS_PROD')
DB_SCHEMA = os.getenv('DB_SCHEMA_PROD')

class ValidateTable(unittest.TestCase):
    def test_data_validate(self):
        conn = psycopg2.connect(
            host = DB_HOST,
            port = DB_PORT,
            dbname = DB_NAME,
            user = DB_USER,
            password = DB_PASS
        )
        cursor = conn.cursor()

        cursor.execute("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public';
        """)
        resultado = cursor.fetchone()
        tabela = resultado[0]

        self.assertEqual(tabela, 'commodities')

if __name__ == "__main__":
    unittest.main()