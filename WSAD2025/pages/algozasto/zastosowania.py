import streamlit as st

st.set_page_config(page_title="Zastosowania ELM", layout="wide")

st.markdown("### Zastosowania")

# Dwie kolumny
col1, col2 = st.columns(2)

with col1:
    st.markdown("<div style='text-align:center; font-weight:bold;'>Mammografia <br><span style='font-size: 0.9em;'></span></div>", unsafe_allow_html=True)
    st.markdown("""
    - Klasyfikacja  
    - Porównanie z SVM  
    - Wysoki poziom skomplikowalności  
    - Wielowymiarowe dane wejściowe
    """)
    st.image("pages/algozasto/figure/3568984.jpg", caption="Mammografia", width=500)

with col2:
    st.markdown("<div style='text-align:center; font-weight:bold;'>Produkt Krajowy Brutto <br><span style='font-size: 0.9em;'></span></div>", unsafe_allow_html=True)
    st.markdown("""
    - Regresja  
    - Porównanie z metodą wstecznej propagacji błędu  
    - Niska skomplikowalność  
    - Dane wejściowe kilku-wymiarowe
    """)
    st.image("pages/algozasto/figure/11235458_10698.jpg", caption="GDP", width=500)

