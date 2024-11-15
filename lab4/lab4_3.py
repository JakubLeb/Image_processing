import cv2
import numpy as np

img = cv2.imread("gang.jpg")
img = cv2.resize(img, (300,300))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

kernel3x3 = np.ones((3,3), np.uint8)
kernel5x5 = np.ones((5,5), np.uint8)
kernel10x10 = np.ones((10,10), np.uint8)

kernel_rect_3x5 = np.ones((3,5), np.uint8)
kernel_rect_5x3 = np.ones((5,3), np.uint8)
kernel_rect_10x3 = np.ones((10,3), np.uint8)

kernel_cross = np.array([
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0]], dtype=np.uint8)
kernel_ellip = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
kernel_circle = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(7,7))

thresh3x3 = cv2.dilate(thresh, kernel3x3, iterations=1)
thresh5x5 = cv2.dilate(thresh, kernel5x5, iterations=1)
thresh10x10 = cv2.dilate(thresh, kernel10x10, iterations=1)

thresh_rect_3x5 = cv2.dilate(thresh, kernel_rect_3x5, iterations=1)
thresh_rect_5x3 = cv2.dilate(thresh, kernel_rect_5x3, iterations=1)
thresh_rect_10x3 = cv2.dilate(thresh, kernel_rect_10x3, iterations=1)

thresh_cross = cv2.dilate(thresh, kernel_cross, iterations=1)
thresh_ellip = cv2.dilate(thresh, kernel_ellip, iterations=1)
thresh_circle = cv2.dilate(thresh, kernel_circle, iterations=1)

combine = np.hstack((thresh, thresh3x3, thresh5x5, thresh10x10))

combine1 = np.hstack((thresh, thresh_rect_3x5, thresh_rect_5x3, thresh_rect_10x3))

combine2 = np.hstack((thresh, thresh_cross, thresh_ellip, thresh_circle))

combine = np.hstack((thresh , thresh3x3, thresh5x5, thresh10x10))

combine1 = np.hstack((thresh,thresh_rect_3x5,thresh_rect_5x3,thresh_rect_10x3  ))

combine2 = np.hstack((thresh,thresh_cross,thresh_ellip,thresh_circle ))


cv2.imshow("Orginalny | 3x3 | 5x5 | 10x10", combine)
cv2.waitKey(0)
cv2.imshow("Orginalny | 3x5 | 5x3 | 10x3", combine1)
cv2.waitKey(0)
cv2.imshow("Orginalny | cross | ellip | circle", combine2)
cv2.waitKey(0)

cv2.imwrite('zadanie3/dilate3x3.jpg',thresh3x3)
cv2.imwrite('zadanie3/dilate5x5.jpg',thresh5x5)
cv2.imwrite('zadanie3/dilate10x10.jpg',thresh10x10)

cv2.imwrite('zadanie3/dilate3x5.jpg',thresh_rect_3x5)
cv2.imwrite('zadanie3/dilate5x3.jpg',thresh_rect_5x3)
cv2.imwrite('zadanie3/dilate10x3.jpg',thresh_rect_10x3)

cv2.imwrite('zadanie3/dilate_cross.jpg',thresh_cross)
cv2.imwrite('zadanie3/dilate_ellip.jpg',thresh_ellip)
cv2.imwrite('zadanie3/dilate_circle.jpg',thresh_circle)
cv2.destroyAllWindows()

cv2.destroyAllWindows()