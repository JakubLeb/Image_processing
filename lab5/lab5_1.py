import cv2
import numpy as np

img = cv2.imread("gang.jpg")
img = cv2.resize(img, (300,300))

object5x5 = (5,5)
object9x1 = (9,1)
object1x9 = (1,9)

filter_img_5x5 = cv2.GaussianBlur(img,object5x5,0)
filter_img_9x1 = cv2.GaussianBlur(img,object9x1,0)
filter_img_1x9 = cv2.GaussianBlur(img,object1x9,0)

combine = np.hstack((img , filter_img_5x5, filter_img_9x1, filter_img_1x9))
cv2.imshow("Obrazy z filtrem  Gaussian", combine)
cv2.waitKey(0)

cv2.destroyAllWindows()