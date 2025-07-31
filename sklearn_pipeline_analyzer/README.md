# Sklearn Pipeline Analyzer

A simple Streamlit app for analyzing trained scikit-learn `Pipeline` objects.

## Features

- Upload a `.pkl` file with a trained `Pipeline`
- Display all steps, transformers, columns, and parameters
- Supports nested `ColumnTransformer` and `Pipeline` structures

## Input

The app expects a `.pkl` file saved using `joblib.dump(...)`, containing a scikit-learn `Pipeline`.

## Example

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import joblib

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression())
])

joblib.dump(pipe, 'pipeline.pkl')
```

## About

Project is in "early access", if you have any suggestions, bugs or whatever, feel free to contact with me:
- email: qertal123@gmail.com
- [GitHub](https://github.com/qertal)
- [LinkedIn](https://www.linkedin.com/in/paweldrzyzga/)