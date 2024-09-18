import pandas as pd
import logging

def extract_features(df):
    # Example feature extraction
    df['Month'] = pd.DatetimeIndex(df['Date']).month
    df['DayOfWeek'] = pd.DatetimeIndex(df['Date']).dayofweek
    df['Promo'] = df['Promo'].fillna(0)
    
    logging.info("Features extracted successfully")
    return df
