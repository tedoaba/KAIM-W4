import pandas as pd
import logging

def load_data(file_path):
    logging.info(f"Loading data from {file_path}")
    return pd.read_csv(file_path)
