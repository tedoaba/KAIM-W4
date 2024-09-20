# KAIM Weak 4 Challenge Task 1

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

### Running the Analysis

To run the analysis, execute:

```bash
python scripts/main.py
```

### Running the tests

To run the analysis, execute:

```bash
python -m unittest discover -s tests
```
