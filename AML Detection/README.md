# 🕵️ Synthetic Transaction Monitoring – AML Fraud Detection

This repository contains a Jupyter notebook analyzing a synthetic dataset of financial transactions with the goal of detecting potential money laundering activities using supervised machine learning techniques.

---

##  Dataset

Dataset: [Synthetic Transaction Monitoring Dataset - AML](https://www.kaggle.com/datasets/hidalgokim/synthetic-transaction-monitoring-dataset-aml)

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
-  **Imbalanced Learning**: Tuning `scale_pos_weight` for rare fraud cases.
-  **Model Evaluation**: 
  - Confusion matrix
  - F1-score
  - ROC-AUC
-  **Feature Importance**: Extraction and visualization of top contributing features.

---

##  Requirements

Install dependencies via `pip`:

```bash
pip install pandas scikit-learn xgboost matplotlib seaborn
