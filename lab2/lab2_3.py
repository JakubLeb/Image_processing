import cv2
import numpy as np

# Wczytanie obrazu z pliku "gang.jpg"
img = cv2.imread("gang.jpg")

# Pobranie liczby wierszy (rows), kolumn (cols) oraz kanałów (_channels) z kształtu obrazu
rows, cols, _channels = map(int, img.shape)

# Macierz transformacji M (niewykorzystana w dalszej części kodu, mogłaby zostać usunięta)
M = np.float32([[1,  0, 0], [0, -1, rows], [0,  0, 1]])

# Utworzenie macierzy rotacji dla obrotu obrazu o 60 stopni wokół środka obrazu
# Zmniejszenie skali obrazu do 60% oryginalnego rozmiaru (0.6)
dst = cv2.warpAffine(img, cv2.getRotationMatrix2D((cols/2, rows/2), 60, 0.6), (cols, rows))

# Wyświetlenie obróconego obrazu
cv2.imshow("test", dst)

# Oczekiwanie na dowolny klawisz, aby zamknąć okno
k = cv2.waitKey(0)

# Zniszczenie wszystkich otwartych okienek OpenCV
cv2.destroyAllWindows()
