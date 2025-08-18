import cv2
import numpy as np

def format_image_to_square(image, target_size=(448, 448)):
    """
    Formatuje obraz do kwadratowego formatu o zadanym rozmiarze, zachowując proporcje.
    
    Parametry:
    - image (np.array): Obraz wejściowy w formacie NumPy array.
    - target_size (tuple): Docelowy rozmiar (szerokość, wysokość) w pikselach.
    
    Zwraca:
    - np.array: Obraz sformatowany do kwadratu o zadanym rozmiarze.
    """
    #################################################################################

    if image is None:
        raise ValueError("Obraz nie może być pusty")
    
    #################################################################################
    # pobranie rozmiarów obrazu
    #################################################################################
    h, w, _ = image.shape

    #################################################################################
    # skalowanie obrazu
    #################################################################################

    scale = min(target_size[0] / h, target_size[1] / w)
    new_size = (int(w * scale), int(h * scale))
    img_resized = cv2.resize(image, new_size, interpolation=cv2.INTER_AREA)
    #################################################################################
    #liczenie marginesów
    #################################################################################

    top = (target_size[1] - new_size[1]) // 2
    bottom = target_size[1] - new_size[1] - top
    left = (target_size[0] - new_size[0]) // 2
    right = target_size[0] - new_size[0] - left

    #################################################################################
    # dodanie marginesów
    #################################################################################
    
    img_padded = cv2.copyMakeBorder(
        img_resized, top, bottom, left, right, cv2.BORDER_CONSTANT, value=[0, 0, 0]
    )

    return img_padded
