import cv2
import numpy as np

# Wczytanie obrazu z pliku "gang.jpg"
img = cv2.imread("gang.jpg")

# Pobranie liczby wierszy (rows), kolumn (cols) oraz kanałów (_channels) z kształtu obrazu
rows, cols, _channels = map(int, img.shape)

# Macierz transformacji dla przesunięcia obrazu o 100 pikseli w prawo i 50 pikseli w dół
M = np.float32([[1, 0, 100], [0, 1, 50]])

# Przesunięcie obrazu przy użyciu macierzy M
dst = cv2.warpAffine(img, M, (cols, rows))

# Wyświetlenie zmodyfikowanego obrazu w oknie o nazwie "test"
cv2.imshow("test", dst)

# Oczekiwanie na dowolny klawisz, aby zamknąć okno
k = cv2.waitKey(0)

# Zniszczenie wszystkich otwartych okienek OpenCV
cv2.destroyAllWindows()
