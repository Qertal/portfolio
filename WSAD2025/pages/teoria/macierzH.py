import streamlit as st

st.set_page_config(page_title="Macierz neuronów ukrytych", layout="wide")

st.markdown("### Macierz neuronów ukrytych")

# Treść i wzory
st.markdown(r"""
Mamy układ równań liniowych:
""")
st.latex(r"""
\sum_{i=1}^{L} \beta_i g(w_i \cdot x_j + b_i) = \mathbf{o}_j \quad \text{dla } j=1,\dots,N
""")

st.markdown("Te $N$ równań można zapisać jako:")
st.latex(r"\mathbf{H} \beta = Y")


st.markdown(r"""
Gdzie:
""")
st.latex(r"""
\mathbf{H}(w_1, ..., w_L, b_1, ..., b_L, x_1, ..., x_N) =
\begin{bmatrix}
g(w_1 \cdot x_1 + b_1) & \dots & g(w_L \cdot x_1 + b_L) \\
\vdots & \ddots & \vdots \\
g(w_1 \cdot x_N + b_1) & \dots & g(w_L \cdot x_N + b_L)
\end{bmatrix}_{N \times L}
""")

st.markdown(r"""
Wektor wag wyjściowych:
""")
st.latex(r"""
\beta = [\beta_1, \dots, \beta_L]^T \in \mathbb{R}^{L \times m}
""")

st.markdown(r"""
Macierz wartości wyjściowych (etykiet, outputów obserwacji):
""")
st.latex(r"""
Y = [\mathbf{y}_1, \dots, \mathbf{y}_N]^T \in \mathbb{R}^{N \times m}
""")

st.markdown("Gdzie $\\mathbf{H}$ nazywana jest **macierzą warstwy ukrytej** sieci neuronowej.")
