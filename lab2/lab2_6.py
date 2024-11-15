import cv2

# Wczytanie obrazu z pliku "gang.jpg"
img = cv2.imread("gang.jpg")

# Pobranie liczby wierszy (rows), kolumn (cols) oraz kanałów (_channels) z kształtu obrazu
rows, cols, _channels = map(int, img.shape)

# Zmniejszenie rozmiaru obrazu do 50% oryginalnego rozmiaru (0.5)
img0_5x = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)

# Zmniejszenie rozmiaru obrazu do 25% oryginalnego rozmiaru (0.25)
img0_25x = cv2.resize(img, None, fx=0.25, fy=0.25, interpolation=cv2.INTER_CUBIC)

"""
# Alternatywna metoda zmniejszania rozmiaru obrazu za pomocą pyrDown:
# img0_5x: obraz zmniejszony o połowę
# img0_25x: obraz zmniejszony do 25% (dwukrotne zmniejszenie)
img0_5x = cv2.pyrDown(img)
img0_25x = cv2.pyrDown(img0_5x)
"""

# Wyświetlenie rozmiarów oryginalnego i zmniejszonych obrazów
print(f"img={img.shape} , img0_5x={img0_5x.shape}, img0_25x={img0_25x.shape}")

# Wyświetlenie obrazu zmniejszonego do 50% oryginalnego rozmiaru
cv2.imshow("test", img0_5x)
k = cv2.waitKey(0)

# Wyświetlenie obrazu zmniejszonego do 25% oryginalnego rozmiaru
cv2.imshow("test", img0_25x)
k = cv2.waitKey(0)

# Zapisanie zmniejszonych obrazów do plików
cv2.imwrite('img0_5x.jpg', img0_5x)
cv2.imwrite('img0_25x.jpg', img0_25x)

# Zniszczenie wszystkich otwartych okienek OpenCV
cv2.destroyAllWindows()
