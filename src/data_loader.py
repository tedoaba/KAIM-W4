import pandas as pd
import logging

# Function to load datasets
def load_data(train_path, test_path, store_path):
    logging.info(f"Loading data from {train_path}, {test_path}, {store_path}")
    train = pd.read_csv(train_path)
    test = pd.read_csv(test_path)
    store = pd.read_csv(store_path)
    return train, test, store