import cv2

# Wczytaj obraz z pliku 'gang.jpg'
image = cv2.imread('gang.jpg')

# Pobierz tekst od użytkownika do umieszczenia na zdjęciu
text = input("Podaj tekst do umieszczania na zdjęcie: ")

# Umieść tekst na obrazie
# cv2.putText(obraz, tekst, położenie, font, skala_fontu, kolor, grubość_tekstu)
image = cv2.putText(image, text, (20, 200), cv2.FONT_HERSHEY_DUPLEX, 3, (125, 246, 55), 3)

# Wyświetl obraz z dodanym tekstem w oknie o nazwie "Zadanie 6"
cv2.imshow("Zadanie 6", image)

# Czekaj na naciśnięcie dowolnego klawisza
k = cv2.waitKey(0)

# Zamyka wszystkie otwarte okna
cv2.destroyAllWindows()
