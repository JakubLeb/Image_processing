import cv2

# Wczytaj obraz z pliku 'gang.jpg'
img = cv2.imread("gang.jpg")
# Konwertuj obraz na odcienie szarości
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Wyświetl przetworzony obraz (w odcieniach szarości) w oknie o nazwie "Display window"
cv2.imshow("Display window", gray)
# Czekaj na naciśnięcie dowolnego klawisza
k = cv2.waitKey(0)
# Zamyka wszystkie okna po naciśnięciu klawisza
cv2.destroyAllWindows()