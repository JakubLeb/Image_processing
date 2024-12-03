import cv2
import numpy as np

img = cv2.imread("gang.jpg")
img = cv2.resize(img, (300, 300))


combine = np.hstack((img))


cv2.imshow("Oryginalny ", combine)
cv2.waitKey(0)
cv2.destroyAllWindows()
