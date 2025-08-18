import streamlit as st

st.set_page_config(page_title="Filary matematyczne ELM", layout="wide")

st.markdown("### Filary matematyczne ELM")

col1, col2 = st.columns(2)

with col1: 
    # Twierdzenie 5
    st.markdown("#### Twierdzenie 5")
    st.markdown(r"""
    Rozważmy standardową sieć SLFN z $N$ ukrytymi neuronami oraz funkcją aktywacji g(x), nieskończenie różniczkowalną. Dla $N$ parami różnych próbek $(x_i, y_i)$, gdzie $N, n, m \in \mathbb{R}$, $i = 1, \dots, N$, $x_i \in \mathbb{R}^n$ i $y_i \in \mathbb{R}^m$, dla **dowolnych** $w_i$ oraz $b_i$ wybranych **losowo** z $\mathbb{R}^n$ i $\mathbb{R}$ odpowiednio, zgodnie z dowolnym **ciągłym rozkładem prawdopodobieństwa** macierz warstwy ukrytej $\mathbf{H} \in \mathbb{R}^{N \times L}$ jest **prawie na pewno odwracalna**, a z tego wynika:  
    """)

    st.latex(r"""\|\mathbf{H} \beta - Y\| = 0 \quad \text{dla } \beta \in \mathbb{R}^{L \times m}""")

with col2:
# Twierdzenie 6
    st.markdown("#### Twierdzenie 6")
    st.markdown(r"""
    Rozważmy standardową sieć SLFN z $N$ ukrytymi neuronami oraz funkcją aktywacji g(x), nieskończenie różniczkowalną. Dla dowolnej małej liczby dodatniej $\varepsilon$, istnieje $L \leq N$ takie, że dla $N$ parami różnych próbek $(x_i, y_i)$, gdzie $N, n, m \in \mathbb{R}$, $i = 1, \dots, N$, $x_i \in \mathbb{R}^n$, $y_i \in \mathbb{R}^m$ oraz **dowolnych** $w_i$ i $b_i$ losowanych z $\mathbb{R}^n$ i $\mathbb{R}$ zgodnie z **dowolnym ciągłym rozkładem**:
    z prawdopodobieństwem **równym 1** zachodzi nierówność:""")

    st.latex(r"""\|\mathbf{H} \beta - Y\| < \varepsilon""")

    st.markdown(r"""
    gdzie: $\mathbf{H} \in \mathbb{R}^{N \times L}$, $\beta \in \mathbb{R}^{L \times m}$, $\mathbf{Y} \in \mathbb{R}^{N \times m}$.
    """)

# Poprawiona wersja twierdzenie 5
st.markdown("#### Poprawiona wersja twierdzenie 5")


st.markdown(r"""
Dla danej sieci SLFN z $N$ ukrytymi neoranami, z $N$ parami różnymi próbek $(x_i,y_i)$, gdzie $x_i \in \mathbb{R}^n$, $y_i \in \mathbb{R}^m$, gdzie:

- funkcja aktywacji $g: \mathbb{R} \rightarrow \mathbb{R}$ posiada następujące cechy: $g \in \mathcal{C}^1$ (m. in. jest różniczkowalna oraz $g'$ jest ciągła) i zbiór punktów krytycznych $\left\{ x \in \mathbb{R} \mid g'(x) = 0 \right\}$ jest przeliczalny,
- wektory wejściowe $x_i$ są liniowo niezależne (w domyśle wymagamy, że $n \geq N$),

jest prawdą, że wnętrze zbioru:

$$
W = \left\{
(w_1, b_1, \dots, w_N, b_N) \in \mathbb{R}^{N(n+1)} \mid \text{macierz } \mathbf{H} \text{ SLFN jest nieodwracalna}
\right\}
$$

jest puste.

**Informacyjnie:**

- Wnętrze w odniesieniu do standardowej topologii przestrzeni $\mathbb{R}^{N(n+1)}$, tj. $\mathbf{x}\in\mathbb{R}^{N(n+1)}$ jest we wnętrzu zbioru $S\subseteq\mathbb{R}^{N(n+1)}$, jeśli istnieje kula $B(\mathbf{x},\epsilon)$ z centrum w $\mathbf{x}$, taka, że $B(\mathbf{x},\epsilon)\subseteq S$.
""")