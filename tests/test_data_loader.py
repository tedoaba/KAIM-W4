import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
import pandas as pd
from data_loader import clean_data

def test_clean_data():
    data = pd.DataFrame({
        'Sales': [100, None, 150],
        'Customers': [50, 70, None]
    })
    cleaned_data = clean_data(data)
    
    assert cleaned_data['Sales'].isnull().sum() == 0
    assert cleaned_data['Customers'].isnull().sum() == 0
