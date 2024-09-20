import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging

def data_overview(df):
    logging.info("Generating data overview...")
    print(f"Dataset Shape: {df.shape}")
    print(f"Columns: {df.columns}")
    print(df.info())
    print(df.describe())

def plot_store_type_distribution(df):
    plt.figure(figsize=(8, 6))
    sns.countplot(x='StoreType', data=df)
    plt.title("Distribution of Stores by StoreType")
    plt.show()

def plot_assortment_distribution(df):
    plt.figure(figsize=(8, 6))
    sns.countplot(x='Assortment', data=df)
    plt.title("Distribution of Stores by Assortment")
    plt.show()

def plot_competition_distance_distribution(df):
    plt.figure(figsize=(10, 6))
    sns.histplot(df['CompetitionDistance'], kde=True)
    plt.title('Distribution of CompetitionDistance')
    plt.show()

def plot_promo2_distribution(df):
    plt.figure(figsize=(8, 6))
    sns.countplot(x='Promo2', data=df)
    plt.title("Promo2 Distribution")
    plt.show()

def plot_competition_distance_by_assortment(df):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Assortment', y='CompetitionDistance', data=df)
    plt.title('CompetitionDistance vs Assortment')
    plt.show()

def plot_correlation_matrix(df):
    plt.figure(figsize=(12, 8))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.title("Correlation between features")
    plt.show()
