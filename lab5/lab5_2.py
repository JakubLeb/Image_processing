import cv2
import numpy as np

img = cv2.imread("gang.jpg")
img = cv2.resize(img, (300,300))

filter_img_3 = cv2.medianBlur(img, 3)
filter_img_5 = cv2.medianBlur(img, 5)
filter_img_7 = cv2.medianBlur(img, 7)

combine = np.hstack((img , filter_img_3, filter_img_5, filter_img_7))
cv2.imshow("Obrazy z filtrem median", combine)
cv2.waitKey(0)

cv2.destroyAllWindows()