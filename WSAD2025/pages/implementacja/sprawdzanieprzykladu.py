import streamlit as st
from pages.implementacja.ELM import ELM
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import cv2
from pages.implementacja.przetwarzanie import format_image_to_square
import numpy as np
from PIL import Image
from sklearn.decomposition import PCA

if "file_to_test" not in st.session_state:
    st.session_state.file_to_test = None

if "formatted_image" not in st.session_state:
    st.session_state.formatted_image = None

if "image_flat" not in st.session_state:
    st.session_state.image_flat = None

if "image_flat_pca" not in st.session_state:
    st.session_state.image_flat_pca = None

# if "uploader_key" not in st.session_state:
#     st.session_state.uploader_key = "uploader_0"



with open('pages/implementacja/data/pca.pkl', 'rb') as file:
    pca = pickle.load(file)

with open('pages/implementacja/data/elm.pkl', 'rb') as file:
    elm_model = pickle.load(file)


col1, col2 = st.columns([3,3])
with col1: 
    st.session_state.file_to_test = st.file_uploader(
        label="Prześlij obraz swojego przyjaciela",
        type=['jpg', 'png'],
        accept_multiple_files=False,
        # key=st.session_state.uploader_key,
        help="Wybierz obrazek swojego pupila, aby sprawdzić co to za zwierzak"
    )

    if st.session_state.file_to_test is not None:  # spr czy plik przeslany
        # st.info("Przesyłanie pliku...")
        
        # # zajebisty pasek od postepu XD
        # progress_bar = st.progress(0) 

        # for progress in range(0, 101, 10):
        #     time.sleep(0.5)
        #     progress_bar.progress(progress)

        st.success("Plik przesłany!!")
        st.image(st.session_state.file_to_test, caption="Twój obraz", width=450)

with col2:
    if st.session_state.file_to_test is not None: 
        if st.button('Wstępne przetwarzanie bez PCA', key='button2'):
            file_bytes = np.asarray(bytearray(st.session_state.file_to_test.read()), dtype=np.uint8)
            image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)    
            st.session_state.formatted_image = format_image_to_square(image, target_size=(448, 448))
            # cv2.imwrite('figure/main.jpg', formatted_image)
            # with st.spinner("Przetwarzanie..."):
            #     import time
            #     time.sleep(3)
            # st.success("Wstępne przetwarzanie zakończone!")
            
        if st.session_state.formatted_image is not None:    
            st.image(st.session_state.formatted_image, caption="Obraz 1:1 (448x448)", channels="BGR")


         
            if st.button('Sprawdź co jest na obrazie!', key='button3'):
                # st.error("Czy na pewno przesłałeś obraz i go sformatowałeś?")
                # image = Image.open('figure/main.jpg')
                st.session_state.image_flat = np.array(st.session_state.formatted_image).reshape(1,-1).astype(np.float16)/255
                st.session_state.image_flat_pca = pca.transform(st.session_state.image_flat)
                pred = elm_model.pred(st.session_state.image_flat_pca)
                if pred[0] > 0.5:
                    st.markdown('<div style="border: 2px solid #4CAF50; padding: 1em; border-radius: 10px; text-align: center; font-size: 40px;">🐶 Na obrazku jest <strong>pies</strong></div>', unsafe_allow_html=True)

                else:
                    st.markdown('<div style="border: 2px solid #2196F3; padding: 1em; border-radius: 10px; text-align: center; font-size: 40px;">🐱 Na obrazku jest <strong>kot</strong></div>',unsafe_allow_html=True)

with st.sidebar:
    if st.button("Reset zmiennych", key="reset"):
        # Resetowanie zmiennych
        st.session_state.formatted_image = None
        st.session_state.file_to_test = None
        st.session_state.image_flat = None
        st.session_state.image_flat_pca = None

                # zmień key, aby wymusić reset file_uploader
                # st.session_state.uploader_key = f"uploader_{np.random.randint(10000)}"