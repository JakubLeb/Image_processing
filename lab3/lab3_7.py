import cv2
import numpy as np

# Wczytanie obrazu wejściowego w skali szarości i zmiana rozmiaru
img = cv2.imread("malpa.jpg", cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (250, 250))

def binary_threshold_testing(img, method, name):
    images = []
    for threshold_value in range(0, 256, 85):
        # Aplikowanie progowania:
        # - threshold_value: wartość progu
        # - 255: maksymalna wartość dla pikseli powyżej progu
        # - method: metoda progowania
        _, binary_img = cv2.threshold(img, threshold_value, 255, method)
        images.append(binary_img)

    # Łączenie obrazów w jeden wiersz
    hstacked_images = np.hstack(images)
    cv2.imshow(name, hstacked_images)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Lista testowanych metod progowania
list_of_methods = [
    cv2.THRESH_BINARY,    # Piksele powyżej progu -> 255, poniżej -> 0
    cv2.THRESH_TRUNC,     # Piksele powyżej progu -> próg, poniżej bez zmian
    cv2.THRESH_TOZERO     # Piksele poniżej progu -> 0, powyżej bez zmian
]
titles = ['THRESH_BINARY', 'THRESH_TRUNC', 'THRESH_TOZERO']

# Testowanie każdej metody progowania
for i in range(len(list_of_methods)):
    binary_threshold_testing(img, list_of_methods[i], titles[i])

cv2.destroyAllWindows()