import cv2

# Wczytanie pliku .BMP
bmp = cv2.imread("sample.bmp")
# Wczytanie pliku .JPG
jpg = cv2.imread("gang.jpg")
# Wczytanie pliku .PNG
png = cv2.imread("spash.png")
# Wczytanie pliku .GIF (jako VideoCapture)
gif = cv2.VideoCapture("giphy.gif")

# Wyświetlanie pliku .BMP
cv2.imshow("Display window", bmp)
k = cv2.waitKey(0)
# Wyświetlanie pliku .JPG
cv2.imshow("Display window", jpg)
k = cv2.waitKey(0)
# Wyświetlanie pliku .PNG
cv2.imshow("Display window", png)
k = cv2.waitKey(0)

# Wyświetlanie animowanego pliku .GIF jako sekwencji klatek
while(gif.isOpened()):
    ret, frame = gif.read()
    if ret == True:
        # Wyświetl każdą klatkę
        cv2.imshow('Frame', frame)
        # Czekaj 25ms na każdą klatkę (animacja), naciśnięcie 'q' przerywa
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        # Zakończ, gdy nie ma więcej klatek
        break
# Zwolnienie zasobów związanych z plikiem GIF
gif.release()
# Zamyka wszystkie otwarte okna
cv2.destroyAllWindows()
