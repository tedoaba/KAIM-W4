import pandas as pd
import logging

def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        logging.info(f"Data loaded successfully from {file_path}")
        return data
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        raise

def clean_data(df):
    # Example missing value handling
    df.fillna(0, inplace=True)
    
    # Handle outliers if necessary
    # Add your outlier detection logic here
    
    logging.info("Data cleaned successfully")
    return df
