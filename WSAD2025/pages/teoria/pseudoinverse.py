import streamlit as st

st.set_page_config(page_title="Pseudoodwrotność", layout="wide")
st.markdown("### Pseudorozwiązanie i pseudoodwrotność")

col1, col2 = st.columns(2)

with col1:
    # --- Twierdzenie 3 ---
    st.markdown("#### Twierdzenie 3")

    st.markdown(r"""
    Niech $\mathbf{G} \in \mathbb{R}^{L \times N}$ oraz $\mathbf{Y} \in \mathbb{R}^{N \times m}$, gdzie $L, N, m \in \mathbb{N}$ i $\mathbf{G}Y$ istnieje. Wówczas następujące warunki są równoważne:
    """)

    st.markdown(r"""
    1. Dla dowolnego $\mathbf{Y}$ iloczyn $\mathbf{G}Y$ jest rozwiązaniem **w sensie najmniejszych kwadratów**, mającym **najmniejszą normę** układu $\mathbf{H}\beta = \mathbf{Y}$, gdzie $\mathbf{H} \in \mathbb{R}^{N \times L}$, $\beta \in \mathbb{R}^{L \times m}$  
    2. $\mathbf{G}$ jest **uogólnioną macierzą odwrotną** (pseudoodwrotnością) w sensie **Moore’a-Penrose’a** macierzy $\mathbf{H}$.
    """)


with col2:

    # --- Definicja 2 ---
    st.markdown("#### Definicja 2")

    st.markdown(r"""
    **Pseudoodwrotnością Moore’a-Penrose’a** macierzy $\mathbf{H} \in \mathbb{R}^{N \times L}$ nazywamy macierz $\mathbf{G} \in \mathbb{R}^{L \times N}$, która spełnia następujące cztery warunki:
    """)

    st.markdown(r"""
    1. $\mathbf{HGH = H}$  
    2. $\mathbf{GHG = G}$  
    3. $\mathbf{(HG)^T = HG}$  
    4. $\mathbf{(GH)^T = GH}$
    """)

    st.markdown(r"""  
    Zapisujemy: $\mathbf{G = H^+}$
    """)

st.markdown("#### Twierdzenie 4")
st.markdown(r"""
    Każda macierz $\mathbf{H} \in \mathbb{R}^{N \times L}$ ma dokładnie jedną pseudoodwrotność w sensie Moore’a-Penrose’a.
    """)

# --- Metody znajdowania pseudoodwrotności ---
st.markdown("### Przykłady metod znajdowania pseudoodwrotności")
st.markdown(r"""
- Rozkład według wartości osobliwych (SVD)  
- Rozkład QR  
- Metoda równań normalnych  
- Rozkład na macierze pełnego rzędu  
- Rozkład Cholesky'ego
""")
