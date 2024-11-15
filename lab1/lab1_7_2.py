import cv2

# Wczytaj obraz z pliku 'gang.jpg'
img = cv2.imread('gang.jpg')

# Rysuje prostokąt na obrazie
# cv2.rectangle(obraz, punkt1, punkt2, kolor, grubość_linii)
# Punkt 1 (0, 250) to lewy górny róg prostokąta
# Punkt 2 (510, 128) to prawy dolny róg prostokąta
# Kolor (255, 255, 0) to żółty, a grubość linii to 15
cv2.rectangle(img, (0, 250), (510, 128), (255, 255, 0), 15)

# Rysuje okrąg na obrazie
# cv2.circle(obraz, środek, promień, kolor, grubość_linii)
# Środek okręgu to (250, 250), promień to 100
# Kolor (255, 0, 255) to fioletowy, a grubość linii to 5
cv2.circle(img, (250, 250), 100, (255, 0, 255), 5)

# Rysuje linię na obrazie
# cv2.line(obraz, punkt1, punkt2, kolor, grubość_linii)
# Punkt 1 to (100, 100), a Punkt 2 to (511, 511)
# Kolor (100, 255, 255) to jasnożółty, a grubość linii to 12
cv2.line(img, (100, 100), (511, 511), (100, 255, 255), 12)

# Wyświetl obraz z narysowanymi kształtami w oknie o nazwie "Zadanie 7"
cv2.imshow("Zadanie 7", img)

# Czekaj na naciśnięcie dowolnego klawisza
k = cv2.waitKey(0)

# Zamyka wszystkie otwarte okna
cv2.destroyAllWindows()
