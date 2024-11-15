import cv2
import numpy as np

img = cv2.imread("gang.jpg")
img = cv2.resize(img, (300,300))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

kernel3x3 = np.ones((3,3), np.uint8)
kernel_rect_5x3 = np.ones((5,3), np.uint8)
kernel_circle = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))

dilation3x3  = cv2.dilate( thresh, kernel3x3)
dilation_rect_5x3 = cv2.dilate( thresh, kernel_rect_5x3)
dilation_circle = cv2.dilate( thresh, kernel_circle)

erosion3x3 = cv2.erode( thresh, kernel3x3)
erosion_rect_5x3 = cv2.erode( thresh, kernel_rect_5x3)
erosion_circle = cv2.erode( thresh, kernel_circle)

contoure_1_3x3 = cv2.subtract(dilation3x3, thresh)
contoure_1_rect_5x3 = cv2.subtract(dilation_rect_5x3, thresh)
contoure_1_circle = cv2.subtract(dilation_circle, thresh)

contoure_2_3x3 = cv2.subtract(thresh,erosion3x3)
contoure_2_rect_5x3 = cv2.subtract(thresh,erosion_rect_5x3)
contoure_2_circle =cv2.subtract(thresh,erosion_circle)

contoure_3_3x3 = cv2.subtract(dilation3x3,erosion3x3)
contoure_3_rect_5x3 =cv2.subtract(dilation_rect_5x3,erosion_rect_5x3)
contoure_3_circle = cv2.subtract(dilation_circle, erosion_circle)

combine = np.hstack((thresh,contoure_1_3x3,contoure_1_rect_5x3,contoure_1_circle))
combine1 = np.hstack((thresh,contoure_2_3x3,contoure_2_rect_5x3,contoure_2_circle))
combine2 = np.hstack((thresh,contoure_3_3x3,contoure_3_rect_5x3,contoure_3_circle))

cv2.imshow("Orginalny | 3x3 | 5x3 | circle", combine)
cv2.waitKey(0)
cv2.imshow("Orginalny | 3x3 | 5x3 | circle", combine1)
cv2.waitKey(0)
cv2.imshow("Orginalny | 3x3 | 5x3 | circle", combine2)
cv2.waitKey(0)

cv2.imwrite('zadanie6/contoure_1_3x3.jpg',contoure_1_3x3)
cv2.imwrite('zadanie6/contoure_1_rect_5x3.jpg',contoure_1_rect_5x3)
cv2.imwrite('zadanie6/contoure_1_circle.jpg',contoure_1_circle)

cv2.imwrite('zadanie6/contoure_2_3x3.jpg',contoure_2_3x3)
cv2.imwrite('zadanie6/contoure_2_rect_5x3.jpg',contoure_2_rect_5x3)
cv2.imwrite('zadanie6/contoure_2_circle.jpg',contoure_2_circle)

cv2.imwrite('zadanie6/contoure_3_3x3.jpg',contoure_3_3x3)
cv2.imwrite('zadanie6/contoure_3_rect_5x3.jpg',contoure_3_rect_5x3)
cv2.imwrite('zadanie6/contoure_3_circle.jpg',contoure_3_circle)
cv2.destroyAllWindows()