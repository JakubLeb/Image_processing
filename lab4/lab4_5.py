

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

open_thresh3x3 = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel3x3)
open_thresh5x5 = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel5x5)
open_thresh10x10 = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel10x10)

open_thresh_rect_3x5 = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel_rect_3x5)
open_thresh_rect_5x3 = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel_rect_5x3)
open_thresh_rect_10x3 = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel_rect_10x3)

open_thresh_cross = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel_cross)
open_thresh_ellip = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel_ellip)
open_thresh_circle = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel_circle)

close_thresh3x3 = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel3x3)
close_thresh5x5 = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel5x5)
close_thresh10x10 = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel10x10)

close_thresh_rect_3x5 = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel_rect_3x5)
close_thresh_rect_5x3 = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel_rect_5x3)
close_thresh_rect_10x3 = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel_rect_10x3)

close_thresh_cross = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel_cross)
close_thresh_ellip = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel_ellip)
close_thresh_circle = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel_circle)


open_combine = np.hstack((thresh , open_thresh3x3, open_thresh5x5, open_thresh10x10))

open_combine1 = np.hstack((thresh,open_thresh_rect_3x5,open_thresh_rect_5x3,open_thresh_rect_10x3  ))

open_combine2 = np.hstack((thresh,open_thresh_cross,open_thresh_ellip,open_thresh_circle ))

close_combine = np.hstack((thresh , close_thresh3x3, close_thresh5x5, close_thresh10x10))

close_combine1 = np.hstack((thresh,close_thresh_rect_3x5,close_thresh_rect_5x3,close_thresh_rect_10x3  ))

close_combine2 = np.hstack((thresh,close_thresh_cross,close_thresh_ellip,close_thresh_circle ))

cv2.imshow("Orginalny | 3x3 | 5x5 | 10x10", open_combine)
cv2.waitKey(0)
cv2.imshow("Orginalny | 3x5 | 5x3 | 10x3", open_combine1)
cv2.waitKey(0)
cv2.imshow("Orginalny | cross | ellip | circle", open_combine2)
cv2.waitKey(0)

cv2.imshow("Orginalny | 3x3 | 5x5 | 10x10", close_combine)
cv2.waitKey(0)
cv2.imshow("Orginalny | 3x5 | 5x3 | 10x3", close_combine1)
cv2.waitKey(0)
cv2.imshow("Orginalny | cross | ellip | circle", close_combine2)
cv2.waitKey(0)

cv2.imwrite('zadanie5/open_3x3.jpg',open_thresh3x3)
cv2.imwrite('zadanie5/open_5x5.jpg',open_thresh5x5)
cv2.imwrite('zadanie5/open_10x10.jpg',open_thresh10x10)

cv2.imwrite('zadanie5/open_3x5.jpg',open_thresh_rect_3x5)
cv2.imwrite('zadanie5/open_5x3.jpg',open_thresh_rect_5x3)
cv2.imwrite('zadanie5/open_10x3.jpg',open_thresh_rect_10x3)

cv2.imwrite('zadanie5/open_cross.jpg',open_thresh_cross)
cv2.imwrite('zadanie5/open_ellip.jpg',open_thresh_ellip)
cv2.imwrite('zadanie5/open_circle.jpg',open_thresh_circle)

cv2.imwrite('zadanie5/close_3x3.jpg',close_thresh3x3)
cv2.imwrite('zadanie5/close_5x5.jpg',close_thresh5x5)
cv2.imwrite('zadanie5/close_10x10.jpg',close_thresh10x10)

cv2.imwrite('zadanie5/close_3x5.jpg',close_thresh_rect_3x5)
cv2.imwrite('zadanie5/close_5x3.jpg',close_thresh_rect_5x3)
cv2.imwrite('zadanie5/close_10x3.jpg',close_thresh_rect_10x3)

cv2.imwrite('zadanie5/close_cross.jpg',close_thresh_cross)
cv2.imwrite('zadanie5/close_ellip.jpg',close_thresh_ellip)
cv2.imwrite('zadanie5/close_circle.jpg',close_thresh_circle)
cv2.destroyAllWindows()