import cv2
import numpy as np

img = cv2.imread("gang.jpg")
img = cv2.resize(img, (300,300))

filter_img_1 = cv2.bilateralFilter(img, 10, 100, 100)
filter_img_2 = cv2.bilateralFilter(img, 20, 200, 200)
filter_img_3 = cv2.bilateralFilter(img, 30, 250, 250)

combine = np.hstack((img , filter_img_1, filter_img_2, filter_img_3))
cv2.imshow("Obrazy z filtrem median", combine)
cv2.waitKey(0)

cv2.destroyAllWindows()