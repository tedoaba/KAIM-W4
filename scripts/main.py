import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from utils import setup_logging
from data_loader import load_data
from feature_engineering import handle_missing_values, encode_features
from eda import data_overview, plot_store_type_distribution, plot_assortment_distribution, plot_competition_distance_distribution, plot_promo2_distribution, plot_competition_distance_by_assortment, plot_correlation_matrix

def main():
    setup_logging()
    file_path = '../data/store.csv'
    store_data = load_data(file_path)
    
    data_overview(store_data)
    store_data = handle_missing_values(store_data)
    store_data = encode_features(store_data)
    
    # Call the plotting functions
    plot_store_type_distribution(store_data)
    plot_assortment_distribution(store_data)
    plot_competition_distance_distribution(store_data)
    plot_promo2_distribution(store_data)
    plot_competition_distance_by_assortment(store_data)
    plot_correlation_matrix(store_data)
    
    print("EDA Completed!")

if __name__ == "__main__":
    main()
