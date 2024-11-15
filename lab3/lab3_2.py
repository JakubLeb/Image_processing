import cv2

# Wczytanie obrazu wejściowego
img = cv2.imread("gang.jpg")

# alpha - współczynnik kontrastu (np. 1.0 oznacza brak zmiany)
# beta - współczynnik jasności (np. 0 oznacza brak zmiany)
alpha = 1      # Bez zmiany kontrastu
beta = 100     # Znaczne rozjaśnienie obrazu

# Modyfikacja jasności obrazu
new_img = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

# Wyświetlenie wyniku
cv2.imshow("test", new_img)
k = cv2.waitKey(0)

cv2.destroyAllWindows()