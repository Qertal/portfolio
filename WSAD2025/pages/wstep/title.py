import streamlit as st

st.set_page_config(page_title="Maszyna uczenia ekstremalnego", layout="wide")

# Stylizacja
st.markdown("""
    <style>
        .main > div {
            padding-top: 5vh;
        }
        .title {
            font-size: 5vw;  /* skalowane względem szerokości okna */
            font-weight: bold;
            text-align: center;
            color: #1f77b4;
        }
        .author {
            font-size: 2vw;
            text-align: center;
            margin-top: 2vh;
        }
        .institute {
            font-size: 1.7vw;
            text-align: center;
            color: #666666;
            margin-top: 0.5vh;
        }
        .footer {
            font-size: 1vw;
            text-align: center;
            margin-top: 8vh;
            color: #999999;
        }

        /* Usunięcie paddingu z kontenera dla maksymalnej szerokości */
        .block-container {
            padding-left: 2rem !important;
            padding-right: 2rem !important;
            max-width: 100% !important;
        }
    </style>
""", unsafe_allow_html=True)

# Treść strony
st.markdown('<div class="title">Maszyna uczenia ekstremalnego<br>i pseudoodwrotności Moore\'a-Penrose\'a</div>', unsafe_allow_html=True)
st.markdown('<div class="author">Paweł Drzyzga</div>', unsafe_allow_html=True)
st.markdown('<div class="institute">Wydział Informatyki i Telekomunikacji<br>Politechnika Krakowska</div>', unsafe_allow_html=True)

st.markdown("""
    <div class="footer">
        Email: <a href="mailto:qertal123@gmail.com">qertal123@gmail.com</a> &nbsp;&nbsp;|&nbsp;&nbsp;
        Linkedin: <a href="https://www.linkedin.com/in/paweldrzyzga/" target="_blank">~/in/paweldrzyzga/</a> &nbsp;&nbsp;|&nbsp;&nbsp;
        Github: <a href="https://github.com/Qertal" target="_blank">~/Qertal</a>
    </div>
""", unsafe_allow_html=True)
