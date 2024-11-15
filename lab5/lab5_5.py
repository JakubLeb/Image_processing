import cv2
import numpy as np

img = cv2.imread("gang.jpg")
img = cv2.resize(img, (300,300))

kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
kernelx2 = kernel * 2
kernelx5 =  kernel * 5
im1 = cv2.filter2D(img, -1, kernel)
im2 = cv2.filter2D(img, -1, kernelx2)
im3 = cv2.filter2D(img, -1, kernelx5)

combine = np.hstack((img , im1, im2, im3))
cv2.imshow("Obrazy z filtrem median", combine)

cv2.waitKey(0)

cv2.destroyAllWindows()