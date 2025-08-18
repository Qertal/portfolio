import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

st.set_page_config(page_title="SLFN + Wizualizacja", layout="wide")

st.markdown('<h2 style="text-align:center;">Sieć neuronowa z pojedynczą warstwą ukrytą (SLFN)</h2>', unsafe_allow_html=True)

# Układ: opis po lewej, rysunek po prawej
col1, col2 = st.columns([2, 1])

with col1:
    # Wstępny opis
    st.markdown(r"""
    Mamy $N$ ($N \in \mathbb{N}$) parami różnych próbek $(x_j, y_j)$, gdzie $j = 1, \dots, N$, \
    gdzie:

    - $x_j = [x_{j1}, x_{j2}, \dots, x_{jn}]^T \in \mathbb{R}^n$  
    - $\mathbf{y}_j = [y_{j1}, y_{j2}, \dots, y_{jm}]^T \in \mathbb{R}^m$  
    - $n, m \in \mathbb{N}$

    Standardowa sieć **SLFN (Single Hidden Layer Feedforward Network)** z $L$ ($L \in \mathbb{N}$) ukrytymi neuronami oraz funkcją aktywacji $g(x)$ modelowana jest jako:
    """)

    # Wzór matematyczny
    st.latex(r"""
    \sum_{i=1}^{L} \beta_i g(w_i \cdot x_j + b_i) = \mathbf{o}_j \quad \text{dla } j=1,\dots,N
    """)

    # Opis składników
    st.markdown(r"""
    Gdzie:
    - $w_i = [w_{i1}, w_{i2}, \dots, w_{in}]^T$, wektor wag łączący i-ty neuron ukryty z wejściem, $w_i \in \mathbb{R}^n$
    - $\beta_i = [\beta_{i1}, \beta_{i2}, \dots, \beta_{im}]^T$, wektor wag między i-tym neuronem ukrytym a wyjściem, $\beta_i \in \mathbb{R}^m$
    - $b_i$ to bias i-tego neuronu ukrytego, $b_i \in \mathbb{R}$
    - $w_i \cdot x_j$ to iloczyn skalarny pomiędzy $w_i$ a $x_j$
    - $o_j$ to wartość wyjściowa sieci neuronowej dla próbki $j$

    ---

    Po dobraniu wag i biasów sieć SLFN można traktować jako **układ równań liniowych**.  
    W przypadku ELM, wagi i biasy dobierane są po prostu **losowo**.
    """)

with col2:
    def draw_slfn():
        fig, ax = plt.subplots(figsize=(5, 11))  # Większa wysokość
        ax.axis('off')

        layers = {
            "input": 3,
            "hidden": 4,
            "output": 2
        }

        x = {"input": 0, "hidden": 1.5, "output": 3}

        # Rysuj neurony
        for layer, count in layers.items():
            for i in range(count):
                y_pos = (i - (count - 1) / 2) * -2.0  # większy odstęp
                circle = plt.Circle((x[layer], y_pos), 0.25, color="#1f77b4")
                ax.add_patch(circle)

        # Połączenia: input → hidden
        for i in range(layers["input"]):
            y1 = (i - (layers["input"] - 1) / 2) * -2.0
            for j in range(layers["hidden"]):
                y2 = (j - (layers["hidden"] - 1) / 2) * -2.0
                ax.plot([x["input"], x["hidden"]], [y1, y2], 'gray', linewidth=0.5)

        # Połączenia: hidden → output
        for i in range(layers["hidden"]):
            y1 = (i - (layers["hidden"] - 1) / 2) * -2.0
            for j in range(layers["output"]):
                y2 = (j - (layers["output"] - 1) / 2) * -2.0
                ax.plot([x["hidden"], x["output"]], [y1, y2], 'gray', linewidth=0.5)

        ax.set_xlim(-0.5, 3.5)
        ax.set_ylim(-6, 4)  # zwiększony zakres pionowy
        return fig


    st.pyplot(draw_slfn())
