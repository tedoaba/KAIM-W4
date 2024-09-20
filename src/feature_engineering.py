import pandas as pd
import missingno as msno
from sklearn.preprocessing import LabelEncoder
import logging

def handle_missing_values(df):
    logging.info("Handling missing values...")
    df['CompetitionDistance'].fillna(df['CompetitionDistance'].median())
    df['CompetitionOpenSinceMonth'].fillna(df['CompetitionOpenSinceMonth'].mode()[0])
    df['CompetitionOpenSinceYear'].fillna(df['CompetitionOpenSinceYear'].mode()[0])
    df['Promo2SinceWeek'].fillna(df['Promo2SinceWeek'].mode()[0])
    df['Promo2SinceYear'].fillna(df['Promo2SinceYear'].mode()[0])
    df['PromoInterval'].fillna('None')
    return df

def encode_features(df):
    logging.info("Encoding categorical features...")
    label_encoder = LabelEncoder()
    df['StoreType'] = label_encoder.fit_transform(df['StoreType'])
    df['Assortment'] = label_encoder.fit_transform(df['Assortment'])
    df['PromoInterval'].fillna('None')
    df['PromoInterval'] = label_encoder.fit_transform(df['PromoInterval'])
    return df
