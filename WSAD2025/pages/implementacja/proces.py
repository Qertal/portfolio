import streamlit as st

st.set_page_config(page_title="Pipeline", layout="wide")

import streamlit as st

# Lewa kolumna — tylko pipeline
col1, colX = st.columns([1, 2])

with col1:
    st.markdown('#### Pipeline działania') 
    st.graphviz_chart("""
    digraph G {
        rankdir=TB;
        node [shape=box, style=rounded, fontsize=12];
        data [label="Zebranie danych"];
        format [label="Zmiana formatu obrazów do 1:1"];
        scale [label="Skalowanie do 448x448"];
        split [label="Podział na treningowe i testowe"];
        pca [label="Ekstrakcja cech (PCA)"];
        train [label="Trenowanie modelu"];
        test [label="Testowanie modelu"];
        data -> format -> scale -> split -> pca -> train -> test;
    }
    """)

with colX:
    # Górne 2 obrazki obok siebie
    img_col1, img_col2 = st.columns(2)

    with img_col1:
        st.markdown('#### Obraz w stanie surowym')
        st.image('pages/implementacja/figure/obrazsurowy.png', 
                 caption='Hej! Jestem Toudi! :D', width=200)

    with img_col2:
        st.markdown('#### Obraz po wstępnym przetwarzaniu')
        st.image('pages/implementacja/figure/obrazzpaskami.jpg', width=275)

    # Obraz PCA wyśrodkowany
    st.markdown("<div style='text-align:center; font-size: 1.1rem; margin-top:1em;'>PCA</div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; justify-content: center;'>", unsafe_allow_html=True)
    st.image('pages/implementacja/figure/PCA.png', width=700)
    st.markdown("</div>", unsafe_allow_html=True)
