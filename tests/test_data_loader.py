import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
from data_loader import load_data

class TestDataLoader(unittest.TestCase):
    def test_load_data(self):
        #file_path = '../data/store.csv'
        #df = load_data(file_path)
        #self.assertIsNotNone(df)
        pass

if __name__ == "__main__":
    unittest.main()
