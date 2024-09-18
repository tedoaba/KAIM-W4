import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
from feature_engineering import extract_features

def test_extract_features():
    data = pd.DataFrame({
        'Date': ['2024-09-01', '2024-09-02', '2024-09-03']
    })
    
    data_with_features = extract_features(data)
    assert 'Month' in data_with_features.columns
    assert 'DayOfWeek' in data_with_features.columns
