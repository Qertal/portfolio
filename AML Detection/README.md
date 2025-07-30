# Synthetic Transaction Monitoring – AML Fraud Detection

This repository contains a Jupyter notebook analyzing a synthetic dataset of financial transactions with the goal of detecting potential money laundering activities using supervised machine learning techniques.

---

##  Dataset

Dataset: [Synthetic Transaction Monitoring Dataset - AML](https://www.kaggle.com/datasets/berkanoztas/synthetic-transaction-monitoring-dataset-aml)

File used: `SAML-D.csv`

The dataset includes anonymized information about:
- transaction participants (sender, receiver, banks),
- transaction metadata (amount, time, location),
- flags indicating known fraudulent patterns.

---

##  Features of the Notebook

-  **Exploratory Data Analysis (EDA)**: Distribution of transaction values, account IDs, timestamps, etc.
-  **Data Cleaning**: Missing values, type conversion.
-  **Model Training**: 
  - `RandomForestClassifier`
  - `XGBoost (XGBClassifier)`
-  **Imbalanced Learning**: Tuning features
-  **Model Evaluation**: 
  - Confusion matrix
  - F1-score
  - ROC-AUC
-  **Feature Importance**: Extraction and visualization of top contributing features.

## Main Chapters

-   Importing necessary packages
-   Importing dataset & EDA
-   Data Visualizations
-   Skewness test
-   Preparing data and preprocessing
-   Finding best model and model val
-   Kicking out a Laundering_type feature, to make a scenario harder
-   Changing from randomforest into XGBoost
-   Analyzing the best model

---

##  Requirements

Install dependencies via `pip`:

```bash
pip install pandas scikit-learn xgboost matplotlib seaborn
```
If you have any questions to me, feel free to contact via Email/Linkedin
qertal123@gmail.com
https://www.linkedin.com/in/paweldrzyzga/
