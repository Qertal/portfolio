import streamlit as st

st.set_page_config(page_title="3-krokowy algorytm ELM", layout="wide")

st.markdown("## Podstawowy 3-krokowy algorytm ELM")

st.markdown(r"""
Rozważmy zbiór treningowy:  
$N = \{(x_{i}, y_{i}) \mid x_{i} \in \mathbb{R}^n,\ y_{i} \in \mathbb{R}^m,\ i = 1, \dots, N\}$, do tego funkcję aktywacji $g(x)$ oraz $L$ ukrytych neuronów. Algorytm dzielimy wówczas na trzy kluczowe kroki:
""")

st.markdown("#### Krok 1:")
st.markdown(r"""
Losowo przypisujemy:
- wagi wejściowe $w_i$,
- biasy $b_i$ dla $i = 1, \dots, L$.
""")

st.markdown("#### Krok 2:")
st.markdown(r"""
Obliczamy macierz warstwy ukrytej $\mathbf{H} \in \mathbb{R}^{N \times L}$ oraz jej pseudoodwrotność: $\mathbf{H}^{+}$.""")

st.markdown("#### Krok 3:")
st.markdown(r"""
Obliczamy wagi wyjściowe $\beta \in \mathbb{R}^{L \times m}$ według wzoru:
""")
st.latex(r"""\beta = \mathbf{H}^{+} Y""")

st.markdown(r"""
gdzie:
- $\mathbf{Y} = [y_1, \dots, y_N]^T \in \mathbb{R}^{N \times m}$
""")
