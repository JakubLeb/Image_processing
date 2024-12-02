import cv2
import numpy as np

img = cv2.imread("figury.png")
img = cv2.resize(img, (300, 300))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
# Detekcja krawędzi algorytmem Canny'ego
edges = cv2.Canny(binary, 0, 255)
# Wykrywanie konturów
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# Kopia oryginalnego obrazu do rysowania konturów
contour_img = img.copy()
# Rysowanie konturów na obrazie
cv2.drawContours(contour_img, contours, -1, (0, 255, 0), 2)

combine = np.hstack((img, cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR), contour_img))
cv2.imshow("Oryginalny | Krawedzie | Kontury", combine)
cv2.waitKey(0)
cv2.destroyAllWindows()
