import streamlit as st

st.set_page_config(page_title="Podział algorytmów ELM", layout="wide")

st.markdown("### Podział algorytmów ELM")

st.markdown("<div style='text-align:center; font-size: 1.5em; font-weight: bold;'>Podział ze względu na:</div>", unsafe_allow_html=True)
st.markdown("")

# Dwie kolumny obok siebie
col1, col2 = st.columns(2)

with col1:
    st.markdown("<div style='text-align:center; font-weight:bold;'>Sposób znajdowania macierzy pseudoodwrotnej:</div>", unsafe_allow_html=True)
    st.markdown("""
    - Singular Value Decomposition ELM (**SVD-ELM**)  
    - Tensor Product Matrix ELM (**TPM-ELM**)  
    - Cholesky factorization of singular matrix ELM (**Geninv-ELM**)  
    - QR factorization and ginv ELM (**QRGinv-ELM**)
    """)

with col2:
    st.markdown("<div style='text-align:center; font-weight:bold;'>Sposób nauki modelu:</div>", unsafe_allow_html=True)
    st.markdown("""
    - Incremental ELM (**I-ELM**)  
    - Ensemble ELM (**EN-ELM**)  
    - Incremental Regularized ELM (**IR-ELM**)  
    - Multi-layer ELM (**ML-ELM**)
    """)

# Końcowy komentarz
col1, col2, col3 = st.columns([1,2,1])



with col2:
    st.markdown("<div style='text-align:center; margin-top: 2em;'>To tak naprawdę tylko wierzchołek góry lodowej, jeśli chodzi o algorytmy ELM.</div>", unsafe_allow_html=True)

    st.image("pages/algozasto/figure/gora.jpg", caption="Gora lodowa", width=500)
