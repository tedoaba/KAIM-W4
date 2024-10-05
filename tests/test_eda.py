import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
from eda import data_overview

def test_explore_data():
    data = pd.DataFrame({
        'Promo': [1, 0, 1],
        'Sales': [100, 200, 300]
    })
    
    data_overview(data)
    assert True
