import cv2
import numpy as np

img = cv2.imread("gang.jpg", cv2.IMREAD_COLOR)
img = cv2.resize(img, (300, 300))

src = cv2.GaussianBlur(img, (3, 3), 0)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# Sobel z różnymi wartościami parametru ksize
edges_k1 = cv2.Sobel(src_gray, cv2.CV_16S, 1, 0, ksize=1)
edges_k3 = cv2.Sobel(src_gray, cv2.CV_16S, 1, 0, ksize=3)
edges_k5 = cv2.Sobel(src_gray, cv2.CV_16S, 1, 0, ksize=5)
# Konwersja do skali 8-bitowej
abs_edges_k1 = cv2.convertScaleAbs(edges_k1)
abs_edges_k3 = cv2.convertScaleAbs(edges_k3)
abs_edges_k5 = cv2.convertScaleAbs(edges_k5)

combine = np.hstack((abs_edges_k1, abs_edges_k3, abs_edges_k5))

cv2.imshow("Sobel ksize=1 | ksize=3 | ksize=5", combine)
cv2.imshow("Oryginalny obraz", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
