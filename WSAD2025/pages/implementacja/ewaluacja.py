import streamlit as st
import pickle
import numpy as np
from sklearn.metrics import confusion_matrix
import seaborn as sns
# from sklearn.decomposition import PCA
from pages.implementacja.ELM import ELM
import joblib
import matplotlib.pyplot as plt
import pandas as pd

# model = joblib.load('pages/implementacja/data/elm.pkl')


# model
with open('pages/implementacja/data/elm.pkl', 'rb') as file:
    elm_model = pickle.load(file)

#pca
with open('pages/implementacja/data/pca.pkl', 'rb') as file:
    pca = pickle.load(file)

X_test_pca = np.load('pages/implementacja/data/X_test_pca.npy')
y_test = np.load('pages/implementacja/data/y_test.npy')

y_pred = elm_model.pred(X_test_pca)
y_pred_class = (y_pred > 0.5).astype(int)

col1, col2 = st.columns([3,3])

with col1:
    st.markdown('## Macierz pomyłek dla zbioru testowego')
    fig, ax = plt.subplots(figsize=(5, 5))  # dla heatmapy
    ax = sns.heatmap(confusion_matrix(y_test,y_pred_class), annot=True, fmt='d', xticklabels=['Kot','Pies'], yticklabels=['Kot','Pies'], cbar=False)
    st.pyplot(fig)

with col2:
    results = []
    accuracy, f1, precision, recall = elm_model.evaluate(y_pred_class, y_test)
    results.append({
                        'accuracy': accuracy,
                        'f1_score': f1,
                        'precision': precision,
                        'recall': recall
                    })
    df = pd.DataFrame(results)
    df_melted = df.melt(var_name="Metric", value_name="Value")
    fig, ax = plt.subplots(figsize=(8, 8))  # dla barplotu
    sns.barplot(data=df_melted, x="Metric", y="Value", hue="Metric", ax=ax)
    # dodanie wartosci do slupkow, ciezka przekmina
    for index, row in df_melted.iterrows():
        ax.text(index, row['Value'] + 0.01, f"{row['Value']:.5f}", ha='center')
    # podpisy etc
    #ax.set_title("Metryki modelu", fontsize=16)
    st.markdown('## Metryki modelu')
    ax.set_ylabel("Wartość", fontsize=12)
    ax.set_xlabel("Metryka", fontsize=12)
    st.pyplot(fig)

