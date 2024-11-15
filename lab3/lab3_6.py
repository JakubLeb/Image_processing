import cv2
import numpy as np

# Wczytanie obrazu wejściowego
img = cv2.imread("gang.jpg")

# Konwersja obrazu na przestrzeń HSV
img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

# Rozdzielenie na kanały H, S, V
h, s, v = cv2.split(img_hsv)
# Połączenie kanałów w jednym oknie
combined1 = np.hstack((h, s, v))

# Wyświetlanie wyników
cv2.imshow("Obraz w przestrzeni BGR", img)
cv2.waitKey(0)
cv2.imshow("Obraz w przestrzeni HSV", img_hsv)
cv2.waitKey(0)
cv2.imshow("H | S | V", combined1)
cv2.waitKey(0)

cv2.imshow("RGB -> HSV", cv2.cvtColor(img , cv2.COLOR_RGB2HSV))
cv2.waitKey(0)

cv2.imshow("HSV -> RGB", cv2.cvtColor(img_hsv, cv2.COLOR_HSV2RGB))
cv2.waitKey(0)

# Zamknięcie okna
cv2.destroyAllWindows()

