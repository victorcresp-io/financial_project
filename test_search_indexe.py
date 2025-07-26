import unittest
import pandas as pd

from src.extract import search_commodities

#Test for seeing if the data return in the function is correct 
class TestSearchCommodities(unittest.TestCase):
    data_example = {
        "simbol": ["BTC-USD"],
        "Open": [5],
        "High": [1],
        "Low": [0],
        "Close": [0],
        "Volume": [10],
        "Dividends": [1.5],
        "Stock Splits": [2]
    }

    def test_search_commodities(self):
        df_target = pd.DataFrame(self.data_example)

        commodities = "BTC-USD"

        df_real_data = search_commodities(commodities)

        df_real_columns = df_real_data.columns
        df_target_columns = df_target.columns

        print(len(df_real_columns))
        print(len(df_target_columns))

        self.assertEqual(df_target_columns.all(), df_real_columns.all())

if __name__ == "__main__":
    unittest.main()