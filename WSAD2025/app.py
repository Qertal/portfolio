import streamlit as st
from pages.implementacja.ELM import ELM


def home_page():
    st.title("Home")

def about_page():
    st.title("About")

def help_page():
    st.title("Help")

#streamlit page
home = st.Page(home_page, title="Home",icon=":material/home:")
about = st.Page(about_page, title="About",icon=":material/settings:")
help = st.Page(help_page, title="Help",icon=":material/help:")

# Informacje wstępne

tytulowa = st.Page("pages/wstep/title.py", title="Wstęp", icon=":material/flag:")
spistresci = st.Page("pages/wstep/tableofcontent.py", title="Spis treści", icon=":material/list:")

# Część teoretyczna

slfn = st.Page("pages/teoria/SLFN.py", title="SLFN", icon=":material/layers:")
macierzH = st.Page("pages/teoria/macierzH.py", title="Macierz H", icon=":material/grid_on:")
mss = st.Page("pages/teoria/mss.py", title="Pseudorozwiązanie", icon=":material/functions:")
pseudoinverse = st.Page("pages/teoria/pseudoinverse.py", title="Pseudoodwrotność", icon=":material/sync_alt:")
filaryELM = st.Page("pages/teoria/filaryELM.py", title="Filary ELM", icon=":material/domain:")
kalkulator = st.Page("pages/teoria/kalkulator.py", title="Kalkulator", icon=":material/calculate:")

# Algorytmy i zastosowania

threestepalgo = st.Page("pages/algozasto/3stepalgo.py", title="Algorytm 3 kroków", icon=":material/filter_3:")
podzialalgo = st.Page("pages/algozasto/podzialalgo.py", title="Podział algorytmów", icon=":material/call_split:")
zastosowania = st.Page("pages/algozasto/zastosowania.py", title="Zastosowania", icon=":material/apps:")

# Praktyczna implementacja

proces = st.Page("pages/implementacja/proces.py", title="Proces", icon=":material/settings:")
ewaluacja = st.Page("pages/implementacja/ewaluacja.py", title="Ewaluacja", icon=":material/bar_chart:")
sprawdzenieprzykladu = st.Page("pages/implementacja/sprawdzanieprzykladu.py", title="Sprawdzenie przykładu", icon=":material/check_circle:")

# Podsumowanie

podsumowanie = st.Page("pages/podsumowanie/podsumowanie.py", title="Podsumowanie", icon=":material/notes:")
bibliografia = st.Page("pages/podsumowanie/bibliografia.py", title="Bibliografia", icon=":material/menu_book:")

#navigation
# #without sections
# pg = st.navigation([home, about, help, info])
    


#without sections
pg = st.navigation({
    "Informacje wstępne":[tytulowa,spistresci],
    "Część teoretyczna": [slfn,macierzH,mss,pseudoinverse,kalkulator,filaryELM],
    "Algorytmy i zastosowania":[threestepalgo,podzialalgo,zastosowania],
    "Praktyczna implementacja":[proces,ewaluacja,sprawdzenieprzykladu],
    "Podsumowanie":[podsumowanie,bibliografia]
    })



pg.run()