import cv2

# Wczytaj obraz z pliku 'gang.jpg'
img = cv2.imread("gang.jpg")
# Wyświetl obraz w oknie o nazwie "Display window"
cv2.imshow("Display window", img)
# Czekaj na naciśnięcie klawisza. Funkcja cv2.waitKey(0) oczekuje na dowolny klawisz.
# Wartość '0' oznacza nieskończone czekanie (do momentu naciśnięcia klawisza).
k = cv2.waitKey(0)
# Zamyka wszystkie okna, gdy zostanie naciśnięty dowolny klawisz.
cv2.destroyAllWindows()