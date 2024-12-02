import cv2
import numpy as np

img = cv2.imread("gang.jpg")
img = cv2.resize(img, (300, 300))

# Zastosowanie filtru Gaussa (zmniejsza ilość krawędzi przez wygładzanie obrazu)
gaussian_blur = cv2.GaussianBlur(img, (15, 15), 0)

# Inny filtr do porównania
median_blur = cv2.medianBlur(img, 15)


combine = np.hstack((img, gaussian_blur, median_blur))


cv2.imshow("Oryginalny | Gaussian Blur | Median Blur", combine)
cv2.waitKey(0)
cv2.destroyAllWindows()
