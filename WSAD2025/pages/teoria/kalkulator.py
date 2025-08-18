import streamlit as st
import numpy as np
from numpy.linalg import matrix_rank, inv
from numpy import transpose, dot, allclose

st.markdown("## Kalkulator pseudoodwrotności")

st.markdown(r"""
            Niech $\mathbf{H} \in \mathrm{M}_{m \times n}$, a dodatkowo $\operatorname{rank}(\mathbf{H}) = \min\{m,n\}$, wtedy:
            
            - $\mathbf{H}^+ = \mathbf{H}^T(\mathbf{H}\mathbf{H}^T)^{-1}$, gdy $m \leq n$,
            - $\mathbf{H}^+ = (\mathbf{H}^T\mathbf{H})^{-1}\mathbf{H}^T$, gdy $m > n$.
            """)

import streamlit as st
import numpy as np

# Ustawienia domyślne w session_state
if 'rows' not in st.session_state:
    st.session_state.rows = 1

if 'columns' not in st.session_state:
    st.session_state.columns = 1

col1, col2 = st.columns([3, 12])
with col1:
    # Formularz do ustawienia rozmiaru macierzy
    with st.form("matrix_size_form"):
        rows = st.number_input("Liczba wierszy", min_value=1, max_value=10, value=st.session_state.rows)
        cols = st.number_input("Liczba kolumn", min_value=1, max_value=10, value=st.session_state.columns)
        submitted_size = st.form_submit_button("Ustaw rozmiar")

        if submitted_size:
            st.session_state.rows = rows
            st.session_state.columns = cols
with col2:
    # Formularz do wprowadzania wartości macierzy
    with st.form("matrix_input_form"):
        matrix = []
        st.write("Wprowadź wartości macierzy:")
        for i in range(int(st.session_state.rows)):
            row = []
            cols = st.columns(int(st.session_state.columns))
            for j in range(int(st.session_state.columns)):
                val = cols[j].number_input(f"H[{i+1},{j+1}]", key=f"A_{i}_{j}", step=.01)
                row.append(val)
            matrix.append(row)

        submit_matrix = st.form_submit_button("Zatwierdź macierz")

with col1:
    # Wyświetlenie macierzy po zatwierdzeniu
    if submit_matrix:
        st.write("Twoja macierz:")
        np_matrix = np.array(matrix)
        latex_matrix = r"\begin{bmatrix}" + \
        r" \\".join([" & ".join([f"{elem:.2f}" for elem in row]) for row in np_matrix]) + \
        r"\end{bmatrix}"
        st.latex(latex_matrix)


if submit_matrix:
    np_matrix = np.array(matrix)
    # st.write("Twoja macierz:")

    # latex_matrix = r"\begin{bmatrix}" + \
    #     r" \\".join([" & ".join([f"{elem:.2f}" for elem in row]) for row in np_matrix]) + \
    #     r"\end{bmatrix}"
    # st.latex(latex_matrix)



    rank = matrix_rank(np_matrix)
    st.write(f"Rząd macierzy wynosi: {rank}")

    if rank == min(st.session_state.rows, st.session_state.columns):
        st.success("Macierz jest pełnego rzędu.")

        H = np_matrix
        H_T = H.T

        if st.session_state.rows <= st.session_state.columns:
            st.latex(r"\mathbf{H}^+ = \mathbf{H}^T(\mathbf{H}\mathbf{H}^T)^{-1}")

            # Wyprowadzenie LaTeX z konkretnymi macierzami
            HHT = dot(H, H_T)
            try:
                HHT_inv = inv(HHT)
                H_plus = dot(H_T, HHT_inv)

                st.markdown("#### Wstawienie do wzoru:")
                st.latex(
                    r"\mathbf{H} = " + latex_matrix
                )
                st.latex(
                    r"\mathbf{H}\mathbf{H}^T = " + r"\begin{bmatrix}" +
                    r" \\".join([" & ".join([f"{elem:.2f}" for elem in row]) for row in HHT]) +
                    r"\end{bmatrix}"
                )
                st.latex(
                    r"(\mathbf{H}\mathbf{H}^T)^{-1} = " + r"\begin{bmatrix}" +
                    r" \\".join([" & ".join([f"{elem:.2f}" for elem in row]) for row in HHT_inv]) +
                    r"\end{bmatrix}"
                )
                st.latex(
                    r"\mathbf{H}^+ = \mathbf{H}^T(\mathbf{H}\mathbf{H}^T)^{-1} = " +
                    r"\begin{bmatrix}" +
                    r" \\".join([" & ".join([f"{elem:.2f}" for elem in row]) for row in H_plus]) +
                    r"\end{bmatrix}"
                )
            except np.linalg.LinAlgError:
                st.error("Nie można obliczyć odwrotności macierzy H·Hᵗ — jest osobliwa.")

        else:
            st.latex(r"\mathbf{H}^+ = (\mathbf{H}^T\mathbf{H})^{-1}\mathbf{H}^T")

            HTH = dot(H_T, H)
            try:
                HTH_inv = inv(HTH)
                H_plus = dot(HTH_inv, H_T)

                st.markdown("#### Wstawienie do wzoru:")
                st.latex(
                    r"\mathbf{H} = " + latex_matrix
                )
                st.latex(
                    r"\mathbf{H}^T\mathbf{H} = " + r"\begin{bmatrix}" +
                    r" \\".join([" & ".join([f"{elem:.2f}" for elem in row]) for row in HTH]) +
                    r"\end{bmatrix}"
                )
                st.latex(
                    r"(\mathbf{H}^T\mathbf{H})^{-1} = " + r"\begin{bmatrix}" +
                    r" \\".join([" & ".join([f"{elem:.2f}" for elem in row]) for row in HTH_inv]) +
                    r"\end{bmatrix}"
                )
                st.latex(
                    r"\mathbf{H}^+ = (\mathbf{H}^T\mathbf{H})^{-1}\mathbf{H}^T = " +
                    r"\begin{bmatrix}" +
                    r" \\".join([" & ".join([f"{elem:.2f}" for elem in row]) for row in H_plus]) +
                    r"\end{bmatrix}"
                )
            except np.linalg.LinAlgError:
                st.error("Nie można obliczyć odwrotności macierzy Hᵗ·H — jest osobliwa.")
    else:
        st.error("Macierz nie jest pełnego rzędu.")
