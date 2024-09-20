import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from utils import setup_logging
from data_loader import load_data
from feature_engineering import handle_missing_values, encode_features
from eda import data_overview, plot_store_type_distribution, plot_assortment_distribution, plot_competition_distance_distribution, plot_promo2_distribution, plot_competition_distance_by_assortment, plot_correlation_matrix, visualize_outliers, plot_sales_distribution, compare_promo_distribution, plot_holiday_sales, extract_month, plot_seasonal_sales, correlation_analysis, plot_promo_sales, plot_assortment_sales


def main():
    setup_logging()
    store_file = '../data/store.csv'
    train_file= '../data/train.csv'
    test_file = '../data/test.csv'
    
    #store_data = load_data(_path)
    train, test, store = load_data(train_path=train_file, test_path=test_file, store_path=store_file)

    data_overview(store)
    store_data = handle_missing_values(store)
    store_data = encode_features(store)
    
    
    store = handle_missing_values(store)
    visualize_outliers(train)
    plot_sales_distribution(train)
    compare_promo_distribution(train, test)
    plot_holiday_sales(train)
    train = extract_month(train)
    plot_seasonal_sales(train)
    correlation_analysis(train)
    plot_promo_sales(train)
    plot_assortment_sales(train, store)



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
