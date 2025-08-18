import streamlit as st

st.set_page_config(layout="wide")

keywords = [
    "ELM", "SLFN", "Macierz H", "Pseudoodwrotność", "Sieć neuronowa", "Moore-Penrose",
    "Warstwa ukryta", "Układ równań", "Odwracalność", "Losowość wag", "Efektywność"
]

style = """
<style>
.bubble-cloud {
    position: relative;
    width: 100%;
    height: 600px;

    border-radius: 20px;
    margin-top: 30px;
    overflow: hidden;
}

.center-title {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 40px;
    font-weight: bold;
    color: #333;
    z-index: 1;
}

.bubble {
    position: absolute;
    padding: 10px 20px;
    border-radius: 25px;
    background-color: #e0e0e0;
    color: #000;
    font-weight: bold;
    box-shadow: 2px 2px 6px rgba(0,0,0,0.2);
    transition: transform 0.3s;
    z-index: 0;
}

.bubble:hover {
    transform: scale(1.1);
    background-color: #d0d0ff;
}

/* Rozrzucenie bąbelków wokół środka */
.b0 { top: 10%; left: 25%; }
.b1 { top: 20%; left: 70%; }
.b2 { top: 35%; left: 10%; }
.b3 { top: 15%; left: 50%; }
.b4 { top: 30%; left: 80%; }
.b5 { top: 65%; left: 20%; }
.b6 { top: 75%; left: 65%; }
.b7 { top: 75%; left: 35%; }
.b8 { top: 55%; left: 80%; }
.b9 { top: 30%; left: 40%; }
.b10 { top: 50%; left: 10%; }
</style>
"""

html = "<div class='bubble-cloud'>"
html += "<div class='center-title'>Podsumowanie</div>"
for i, word in enumerate(keywords):
    html += f"<div class='bubble b{i}'>{word}</div>"
html += "</div>"

# Wyświetlenie w Streamlit
st.markdown(style + html, unsafe_allow_html=True)
