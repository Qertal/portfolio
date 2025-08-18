import streamlit as st

st.set_page_config(page_title="Pseudorozwiązanie", layout="wide")

st.markdown("### Rozwiązanie w sensie najmniejszych kwadratów")

col1, col2 = st.columns(2)
with col1:
    # Twierdzenie 1
    st.markdown("#### Twierdzenie 1")
    st.markdown(r"""
    Niech $\mathbf{H} \in M_{m \times n}(\mathbb{R})$. Niech ponadto $b \in \mathbb{R}^m$.  
    Wówczas istnieje (przynajmniej jeden) taki wektor $w \in \mathbb{R}^n$, że dla każdego $v \in \mathbb{R}^n$ zachodzi nierówność:
    """)
    st.latex(r"""
    \|\mathbf{H}w - b\| \leq \|\mathbf{H}v - b\|
    """)

with col2:
    # Definicja 1
    st.markdown("#### Definicja 1")
    st.markdown(r"""
    Niech $\mathbf{H} \in M_{m \times n}(\mathbb{R})$, a $b \in \mathbb{R}^m$.  
    **Pseudorozwiązaniem w sensie normy euklidesowej** układu równań
    """)
    st.latex(r"""
    \mathbf{H} [x_1, ..., x_n]^T = b
    """)
    st.markdown(r"""
    nazywa się każdy wektor $w \in \mathbb{R}^n$ spełniający nierówność:
    """)
    st.latex(r"""
    \|\mathbf{H}w - b\| \leq \|\mathbf{H}v - b\| \quad \text{dla dowolnego } v \in \mathbb{R}^n
    """)


# Twierdzenie 2
st.markdown("#### Twierdzenie 2")
st.markdown(r"""
Przypuśćmy, że układ równań
""")
st.latex(r"""
\mathbf{H} [x_1, ..., x_n]^T = b
""")
st.markdown(r"""
jest niesprzeczny. Niech ponadto $w \in \mathbb{R}^n$. Wówczas następujące warunki są równoważne:
""")
st.markdown(r"""
1. Wektor $w$ jest pseudorozwiązaniem układu,  
2. Wektor $w$ jest rozwiązaniem układu.
""")
