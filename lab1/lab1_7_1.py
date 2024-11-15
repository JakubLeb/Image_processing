import cv2

import cv2

# Wczytaj obraz z pliku 'gang.jpg'
img = cv2.imread('gang.jpg')

# Rysuje prostokąt na obrazie
# cv2.rectangle(obraz, punkt1, punkt2, kolor, grubość_linii)
# Punkt 1 (384, 0) to lewy górny róg prostokąta
# Punkt 2 (510, 128) to prawy dolny róg prostokąta
# Kolor (0, 255, 0) to zielony, a grubość linii to 3
cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

# Rysuje okrąg na obrazie
# cv2.circle(obraz, środek, promień, kolor, grubość_linii)
# Środek okręgu to (447, 63), promień to 63
# Kolor (0, 0, 255) to czerwony, a -1 oznacza wypełnienie okręgu
cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)

# Rysuje linię na obrazie
# cv2.line(obraz, punkt1, punkt2, kolor, grubość_linii)
# Punkt 1 to (0, 0) (lewy górny róg), a Punkt 2 to (511, 511) (prawy dolny róg)
# Kolor (255, 0, 0) to niebieski, a grubość linii to 5
cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

# Wyświetl obraz z narysowanymi kształtami w oknie o nazwie "Zadanie 7"
cv2.imshow("Zadanie 7", img)

# Czekaj na naciśnięcie dowolnego klawisza
k = cv2.waitKey(0)

# Zamyka wszystkie otwarte okna
cv2.destroyAllWindows()
