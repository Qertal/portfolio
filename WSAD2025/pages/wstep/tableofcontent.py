import streamlit as st

st.set_page_config(page_title="Spis treści - ELM", layout="centered")

# Stylizacja
st.markdown("""
    <style>
        .title {
            font-size: 2em;
            font-weight: bold;
            color: #2e3ec9;
            margin-bottom: 1em;
        }
        .section {
            font-size: 1.3em;
            font-weight: bold;
            color: #1f77b4;
            margin-top: 1em;
        }
        .subpoint {
            margin-left: 1.5em;
            font-size: 1.1em;
        }
    </style>
""", unsafe_allow_html=True)

# Tytuł
st.markdown('<div class="title">Spis treści</div>', unsafe_allow_html=True)

# Spis treści
st.markdown("""
<div class="section">1️⃣ Część teoretyczna</div>
<div class="subpoint">• Sieć neuronowa z pojedynczą warstwą ukrytą (SLFN)</div>
<div class="subpoint">• Macierz neuronów ukrytych</div>
<div class="subpoint">• Rozwiązanie w sensie najmniejszych kwadratów</div>
<div class="subpoint">• Pseudoodwrotności</div>
<div class="subpoint">• Przykłady metod znajdowania pseudoodwrotności</div>
<div class="subpoint">• Filary matematyczne ELM</div>

            
<div class="section">2️⃣ Algorytm ELM</div>
<div class="subpoint">• 3-krokowy algorytm</div>
<div class="subpoint">• Podział algorytmów ELM</div>
<div class="subpoint">• Konkretne zastosowania ELM</div>


<div class="section">3️ Praktyczna implementacja ELM</div>
<div class="subpoint">• O przygotowaniu słów kilka</div>
<div class="subpoint">• Ewaluacja modelu</div>
<div class="subpoint">• Testowanie na "żywym" przykładzie</div>

<div class="section">4️⃣ Podsumowanie</div>
""", unsafe_allow_html=True)
