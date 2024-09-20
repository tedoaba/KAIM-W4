import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
import pandas as pd
from feature_engineering import encode_features

class TestFeatureEngineering(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'StoreType': ['a', 'b', 'c'],
            'Assortment': ['x', 'y', None],
            'PromoInterval': [None, 'Jan', 'Feb'],
        })

    def test_encode_features(self):
        df_encoded = encode_features(self.df)
        self.assertIn('StoreType', df_encoded.columns)

if __name__ == "__main__":
    unittest.main()
