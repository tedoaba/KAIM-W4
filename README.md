# KAIM Weak 4 Challenge Task 1


## Exploratory Data Analysis on Customer Purchasing Behavior

## Overview

This project focuses on conducting an exploratory data analysis (EDA) of customer purchasing behavior at Rossmann Pharmaceuticals. The analysis aims to support the finance team in forecasting sales across various stores by understanding key factors influencing purchasing behavior, such as promotions, competition, holidays, seasonality, and locality.

## Business Need

Rossmann Pharmaceuticals seeks to improve sales forecasting accuracy. Currently, store managers rely on their judgment to predict sales, which can lead to inconsistencies. By leveraging data-driven insights, the company aims to forecast sales six weeks ahead, ensuring better inventory management and resource allocation.

## Key Objectives

- Explore the behavior of customers in various stores.
- Analyze the impact of promotions and store openings on purchasing behavior.
- Clean and preprocess the data to ensure quality insights.
- Visualize findings to communicate results effectively.

## Project Structure

```bash

├── .github/
│   └── workflows/
│       └── ci-cd.yml             # GitHub Actions CI/CD pipeline config
├── data/                         # Data files (raw and processed)
│   └── rossmann_sales.csv        # Example CSV data
├── logs/                         # Logging output
│   └── eda.log                   # Log file for Task 1
├── src/                          # Main source code for EDA and utilities
│   ├── __init__.py
│   ├── data_loader.py            # Data cloader module
│   ├── feature_engineering.py    # Feature extraction module
│   ├── eda.py                    # Main EDA function
│   └── utils.py                  # Helper functions (logging, etc.)
├── scripts/                       
│   ├── __init__.py
│   ├── main.py       
├── tests/                        # Unit tests and integration tests
│   ├── __init__.py
│   ├── test_data_loader.py       # Tests for data preprocessing
│   ├── test_feature_engineering.py # Tests for feature extraction
│   └── test_eda.py                # Tests for EDA module
├── requirements.txt              # Project dependencies
├── README.md                     # Project documentation
```

## Folder Structure

- `src/`: Contains source code for data loading, feature engineering, and EDA.
- `tests/`: Contains unit and integration tests.
- `data/`: Contains raw and processed data files.
- `logs/`: Contains logging output.
- `.github/`: Contains CI/CD configurations.

## Installation

To set up the project, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/tedoaba/KAIM-W4.git
   cd KAIM-W4
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the exploratory data analysis, execute the following command in the terminal:

```bash
python scripts/main.py
```

This will load the dataset, perform data cleaning, and generate visualizations based on customer purchasing behavior.

## Logging

The project utilizes Python's logging library to track the analysis process. Logs are recorded in the `logs/eda.log` file, providing a traceable record of the steps taken during the EDA.

## Testing

Unit tests are provided to ensure the reliability of the code. To run the tests, execute:

```bash
cd tests
python -m unittest discover
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License.
