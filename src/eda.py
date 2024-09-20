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
    
# Function to extract month from the date
def extract_month(train):
    train['Month'] = pd.to_datetime(train['Date']).dt.month
    return train

# Function to handle missing values in the store dataset
def handle_missing_values(store):
    store['CompetitionDistance'].fillna(store['CompetitionDistance'].median(), inplace=True)
    store['Promo2SinceWeek'].fillna(0, inplace=True)
    store['Promo2SinceYear'].fillna(0, inplace=True)
    return store

# Function to visualize outliers in sales and customer count
def visualize_outliers(train):
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=train[['Sales', 'Customers']])
    plt.title("Boxplot of Sales and Customers")
    plt.show()

# Function to plot sales distribution in training set
def plot_sales_distribution(train):
    plt.figure(figsize=(10, 6))
    sns.histplot(train['Sales'], kde=True, bins=50)
    plt.title('Sales Distribution in Training Set')
    plt.show()

# Function to compare promo distribution between training and test set
def compare_promo_distribution(train, test):
    plt.figure(figsize=(10, 6))
    sns.histplot(train['Promo'], color='blue', label='Train', kde=True, bins=30)
    sns.histplot(test['Promo'], color='green', label='Test', kde=True, bins=30)
    plt.title('Promo Distribution: Training vs Test Set')
    plt.legend()
    plt.show()

# Function to calculate and plot sales during state holidays
def plot_holiday_sales(train):
    holiday_sales = train.groupby('StateHoliday')['Sales'].mean().reset_index()
    plt.figure(figsize=(10, 6))
    sns.barplot(x='StateHoliday', y='Sales', data=holiday_sales)
    plt.title('Sales During State Holidays')
    plt.show()

# Function to visualize seasonal sales trends
def plot_seasonal_sales(train):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Month', y='Sales', data=train)
    plt.title('Monthly Sales Distribution')
    plt.show()

# Function for correlation analysis between sales and customers
def correlation_analysis(train):
    correlation = train[['Sales', 'Customers']].corr()
    sns.heatmap(correlation, annot=True, cmap='coolwarm')
    plt.title('Correlation between Sales and Customers')
    plt.show()

# Function to plot sales during promotions vs no promotions
def plot_promo_sales(train):
    promo_sales = train.groupby('Promo')['Sales'].mean().reset_index()
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Promo', y='Sales', data=promo_sales)
    plt.title('Sales During Promotions vs No Promotions')
    plt.show()

# Function to plot average sales by assortment type
def plot_assortment_sales(train, store):
    assortment_sales = train.merge(store, on='Store')
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Assortment', y='Sales', data=assortment_sales)
    plt.title('Sales by Assortment Type')
    plt.show()



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
