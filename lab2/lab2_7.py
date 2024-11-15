import cv2

# Wczytanie obrazu z pliku "gang.jpg"
img = cv2.imread("gang.jpg")

# Pobranie liczby wierszy (rows), kolumn (cols) oraz kanałów (_channels) z kształtu obrazu
rows, cols, _channels = map(int, img.shape)

# Zwiększenie rozmiaru obrazu o 50% (1.5x) w obu kierunkach z użyciem interpolacji bicubicznej
img1_5x = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)

# Wyświetlenie rozmiarów oryginalnego obrazu i powiększonego
print(f"img={img.shape} , img1_5x={img1_5x.shape}")

# Wyświetlenie powiększonego obrazu
cv2.imshow("test", img1_5x)

# Oczekiwanie na dowolny klawisz, aby zamknąć okno
k = cv2.waitKey(0)

# Zapisanie powiększonego obrazu do pliku
cv2.imwrite('img1_5x.jpg', img1_5x)

# Zniszczenie wszystkich otwartych okienek OpenCV
cv2.destroyAllWindows()
