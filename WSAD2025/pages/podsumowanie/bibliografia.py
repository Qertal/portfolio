import streamlit as st

st.set_page_config(page_title="Bibliografia", layout="wide")

# Styl
st.markdown("""
    <style>
        .ref-box {
            border-left: 4px solid #1f77b4;
            padding: 1em;
            margin-bottom: 1em;
            background-color: #f9f9f9;
            border-radius: 5px;
        }
        .ref-title {
            font-weight: bold;
            font-size: 16px;
        }
        .ref-detail {
            font-size: 15px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("📚 Bibliografia")

# Bibliografia – lista
references = [
    {
        "label": "[1]",
        "authors": "Guang-Bin Huang, Qin-Yu Zhu, Chee-Kheong Siew",
        "title": "Extreme learning machine: Theory and applications",
        "source": "Elsevier, Neurocomputing, 70, 2006, pp. 489–501."
    },
    {
        "label": "[2]",
        "authors": "Shuxia Lu, Xizhao Wang, Guiqiang Zhang, Xu Zhou",
        "title": "Effective algorithms of the Moore-Penrose inverse matrices for extreme learning machine",
        "source": "IOS Press, Intelligent Data Analysis, 19, 2015, pp. 743–760."
    },
    {
        "label": "[3]",
        "authors": "Jian Wang, Siyuan Lu, Shui-Hua Wang, Yu-Dong Zhang",
        "title": "A review on extreme learning machine",
        "source": "Springer, Multimedia Tools and Applications, 2022, pp. 41611–41660."
    },
    {
        "label": "[4]",
        "authors": "Roger Penrose",
        "title": "On best approximate solution of linear matrix equations",
        "source": "Proceedings of the Cambridge Philosophical Society, 52(1), 1956, pp. 17–19."
    },
    {
        "label": "[5]",
        "authors": "Irina Perfilieva, Nicolas Madrid, Manuel Ojeda-Aciego, Piotr Artiemjew, Agnieszka Niemczynowicz",
        "title": "A Critical Analysis of the Theoretical Framework of the Extreme Learning Machine",
        "source": 'arXiv, preprint 2406.17427, 2024. <br>Dostępne na stronie: <a href="https://arxiv.org/abs/2406.17427" target="_blank">arxiv.org</a>, dostęp na dzień: 01.11.2024.'
    },
    {
        "label": "[6]",
        "authors": "Weiying Xie, Yunsong Li, Yide Ma",
        "title": "Breast mass classification in digital mammography based on extreme learning machine",
        "source": "Elsevier, Neurocomputing, 173, 2015, pp. 930–941."
    },
    {
        "label": "[7]",
        "authors": "Materiały z wykładów Dr Marcina Skrzyńskiego",
        "title": "Algebra Stosowana, kierunek Matematyka Stosowana, specjalność Analiza Danych, semestr IV",
        "source": "Pseudorozwiązanie, uogólnione macierze Moore'a-Penrose'a."
    },
    {
        "label": "[8]",
        "authors": "Ljubiša Milačić, Srdan Jovic, Tanja Vujović, Jovica Miljković",
        "title": "Application of artificial neural network with extreme learning machine for economic growth estimation",
        "source": "Physica A: Statistical Mechanics and its Applications, 465, 2017, pp. 285–288."
    },
    {
        "label": "[9]",
        "authors": "Svetlana Sokolov-Mladenović, Milos Milovančević, Igor Mladenović, Meysam Alizamir",
        "title": "Economic growth forecasting by artificial neural network with extreme learning machine based on trade, import and export parameters",
        "source": "Computers in Human Behavior, 65, 2016, pp. 43–45."
    },
    {
        "label": "[10]",
        "authors": "Goran Rakic, Dragana Milenkovic, Sonja Vujovic, Tanja Vujovic",
        "title": "Information system for e-GDP based on computational intelligence approach",
        "source": "Physica A: Statistical Mechanics and its Applications, 513, 2019, pp. 418–423."
    }
]

# Wyświetlenie każdej pozycji
for ref in references:
    st.markdown(
        f"""
        <div class="ref-box">
            <div class="ref-title">{ref['label']} {ref['title']}</div>
            <div class="ref-detail">{ref['authors']}<br>{ref['source']}</div>
        </div>
        """,
        unsafe_allow_html=True
    )
