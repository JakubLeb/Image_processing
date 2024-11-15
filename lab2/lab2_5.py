import cv2

# Wczytanie obrazu z pliku "gang.jpg"
img = cv2.imread("gang.jpg")

# Pobranie liczby wierszy (rows), kolumn (cols) oraz kanałów (_channels) z kształtu obrazu
rows, cols, _channels = map(int, img.shape)

"""
# Alternatywna metoda skalowania za pomocą interpolacji bicubicznej:
# img2x: obraz powiększony dwukrotnie w obu kierunkach
# img4x: obraz powiększony czterokrotnie w obu kierunkach
img2x = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
img4x = cv2.resize(img, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
"""

# Powiększenie obrazu dwukrotnie za pomocą funkcji pyrUp (interpolacja Gaussowska)
img2x = cv2.pyrUp(img)

# Powiększenie obrazu czterokrotnie poprzez kolejne powiększenie img2x
img4x = cv2.pyrUp(img2x)

# Wyświetlenie rozmiarów oryginalnego i powiększonych obrazów
print(f"img={img.shape} , img2x={img2x.shape}, img4x={img4x.shape}")

# Wyświetlenie obrazu powiększonego 2x
cv2.imshow("test", img2x)
k = cv2.waitKey(0)

# Wyświetlenie obrazu powiększonego 4x
cv2.imshow("test", img4x)
k = cv2.waitKey(0)

# Zapisanie powiększonych obrazów do plików
cv2.imwrite('img2x.jpg', img2x)
cv2.imwrite('img4x.jpg', img4x)

# Zniszczenie wszystkich otwartych okienek OpenCV
cv2.destroyAllWindows()
