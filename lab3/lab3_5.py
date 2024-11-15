import cv2
import numpy as np

# Utworzenie białego obrazu 500x500
img = np.ones((500, 500, 3), dtype=np.uint8) * 255

# Utworzenie czarnego obrazu 500x500
img2 = np.ones((500, 500, 3), dtype=np.uint8)

# Rysowanie czerwonego okręgu
# Parametry: środek (x=100, y=150), promień=50, kolor BGR=(0,0,255), grubość=8
cv2.circle(img, (100, 150), 50, (0, 0, 255), 8)

cv2.circle(img2, (100, 150), 50, (0, 0, 255), 8)

# Rysowanie niebieskiego prostokąta
# Parametry: lewy górny róg (450,100), prawy dolny róg (250,300)
cv2.rectangle(img, (450, 100), (250, 300), (255, 0, 0), 8)

cv2.rectangle(img2, (450, 100), (250, 300), (255, 0, 0), 8)
# Rysowanie zielonego trójkąta
p1 = (100, 450)  # pierwszy wierzchołek
p2 = (150, 350)  # drugi wierzchołek
p3 = (200, 450)  # trzeci wierzchołek

# Rysowanie linii tworzących trójkąt
cv2.line(img, p1, p2, (0, 255, 0), 8)
cv2.line(img, p2, p3, (0, 255, 0), 8)
cv2.line(img, p1, p3, (0, 255, 0), 8)

cv2.line(img2, p1, p2, (0, 255, 0), 8)
cv2.line(img2, p2, p3, (0, 255, 0), 8)
cv2.line(img2, p1, p3, (0, 255, 0), 8)


# Rozdzielenie obrazu na kanały BGR i wyświetlenie ich obok siebie
b1, g1, r1 = cv2.split(img)
combined1 = np.hstack((b1, g1, r1))

b2, g2, r2 = cv2.split(img2)
combined2 = np.hstack((b2, g2, r2))

cv2.imshow("test", img)
cv2.waitKey(0)

cv2.imshow('Blue | Green | Red', combined1)
cv2.waitKey(0)

cv2.imshow("test", img2)
cv2.waitKey(0)

cv2.imshow('Blue | Green | Red', combined2)
cv2.waitKey(0)

#Zapisanie obrazów
cv2.imwrite('zadanie5/obraz_na_bialym_tle.jpg', img)
cv2.imwrite('zadanie5/obraz_na_czarnym_tle.jpg', img2)

cv2.imwrite('zadanie5/biale_tlo_kabal_b.jpg', b1)
cv2.imwrite('zadanie5/biale_tlo_kabal_g.jpg', g1)
cv2.imwrite('zadanie5/biale_tlo_kabal_r.jpg', r1)

cv2.imwrite('zadanie5/czarne_tlo_kabal_b.jpg', b2)
cv2.imwrite('zadanie5/czarne_tlo_kabal_g.jpg', g2)
cv2.imwrite('zadanie5/czarne_tlo_kabal_r.jpg', r2)

cv2.destroyAllWindows()