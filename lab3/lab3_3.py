import cv2
import numpy as np

# Wczytanie obrazów wejściowych
img1 = cv2.imread("gang.jpg")
rows1, cols1, *channels1 = map(int, img1.shape)

img2 = cv2.imread("malpa.jpg")
rows2, cols2, *channels2 = map(int, img2.shape)

# Przeskalowanie drugiego obrazu do wymiarów pierwszego
img2x = cv2.resize(img2, None, fx=cols1/cols2, fy=rows1/rows2, interpolation=cv2.INTER_CUBIC)

# Współczynniki blendowania:
# alpha - waga pierwszego obrazu
# beta - waga drugiego obrazu
# gamma - składnik dodawany do każdego piksela (rozjaśnienie/przyciemnienie)
alpha = 0.5
beta = 1.0 - alpha
gamma = 0

# Połączenie obrazów: dst = alpha*img1 + beta*img2 + gamma
dst = cv2.addWeighted(img1, alpha, img2x, beta, gamma)

# Wyświetlenie wyniku
cv2.imshow("test", dst)
k = cv2.waitKey(0)

cv2.destroyAllWindows()