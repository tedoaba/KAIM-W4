import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from data_loader import load_data, clean_data
from feature_engineering import extract_features
from eda import explore_data
from utils import setup_logging


def main():
    # Setup logging
    log_file = os.path.join("../logs", "eda.log")
    setup_logging(log_file)

    # Filepath to dataset
    file_path = os.path.join("../data", "store.csv")
    
    # Step 1: Load the data
    data = load_data(file_path)
    
    # Step 2: Preprocess the data (missing values, outliers, etc.)
    cleaned_data = clean_data(data)
    
    # Step 3: Feature Engineering
    #data_with_features = extract_features(cleaned_data)
    
    # Step 4: Exploratory Data Analysis
    #explore_data(data_with_features)
    
    print("Data preprocessing, feature engineering, and EDA completed successfully.")

if __name__ == "__main__":
    main()
