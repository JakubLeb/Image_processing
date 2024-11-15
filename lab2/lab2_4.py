import cv2

# Wczytanie obrazu z pliku "gang.jpg"
img = cv2.imread("gang.jpg")

# Wycięcie fragmentu obrazu z współrzędnych [100:350] w pionie oraz [150:350] w poziomie
dst = img[100:350, 150:350]

# Wyświetlenie wyciętego fragmentu obrazu
cv2.imshow("test", dst)

# Oczekiwanie na dowolny klawisz, aby zamknąć okno
k = cv2.waitKey(0)

# Zniszczenie wszystkich otwartych okienek OpenCV
cv2.destroyAllWindows()
