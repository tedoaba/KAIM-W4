import matplotlib.pyplot as plt
import seaborn as sns
import logging

def explore_data(df):
    # Example plot - Sales by Promo
    plt.figure(figsize=(10,6))
    sns.barplot(x="Promo", y="Sales", data=df)
    plt.title("Sales vs Promo")
    plt.savefig('plots/sales_vs_promo.png')
    
    logging.info("EDA completed and plots saved successfully")
    return
