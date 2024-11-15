import cv2

# Wczytanie obrazu wejściowego
img = cv2.imread("gang.jpg")

# Parametry modyfikacji obrazu:
# alpha - współczynnik kontrastu (>1 zwiększa kontrast, <1 zmniejsza)
# beta - współczynnik jasności (>0 rozjaśnia, <0 przyciemnia)
alpha = 10
beta = 0

# Zastosowanie transformacji jasności i kontrastu: f(x) = alpha * x + beta
new_img = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

# Wyświetlenie wyniku
cv2.imshow("test", new_img)
k = cv2.waitKey(0)

cv2.destroyAllWindows()