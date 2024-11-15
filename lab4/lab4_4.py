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


thresh3x3 = cv2.erode(thresh, kernel3x3, iterations=1)
thresh5x5 = cv2.erode(thresh, kernel5x5, iterations=1)
thresh10x10 = cv2.erode(thresh, kernel10x10, iterations=1)

thresh_rect_3x5 = cv2.erode(thresh, kernel_rect_3x5, iterations=1)
thresh_rect_5x3 = cv2.erode(thresh, kernel_rect_5x3, iterations=1)
thresh_rect_10x3 = cv2.erode(thresh, kernel_rect_10x3, iterations=1)

thresh_cross = cv2.erode(thresh, kernel_cross, iterations=1)
thresh_ellip = cv2.erode(thresh, kernel_ellip, iterations=1)
thresh_circle = cv2.erode(thresh, kernel_circle, iterations=1)

combine = np.hstack((thresh , thresh3x3, thresh5x5, thresh10x10))

combine1 = np.hstack((thresh,thresh_rect_3x5,thresh_rect_5x3,thresh_rect_10x3  ))

combine2 = np.hstack((thresh,thresh_cross,thresh_ellip,thresh_circle ))

for x in [3,5,7]:
    thresh3x3 = cv2.dilate(thresh, kernel3x3, iterations=x)
    thresh5x5 = cv2.dilate(thresh, kernel5x5, iterations=x)
    thresh10x10 = cv2.dilate(thresh, kernel10x10, iterations=x)
    combine = np.hstack((thresh, thresh3x3, thresh5x5, thresh10x10))

    thresh_rect_3x5 = cv2.dilate(thresh, kernel_rect_3x5, iterations=x)
    thresh_rect_5x3 = cv2.dilate(thresh, kernel_rect_5x3, iterations=x)
    thresh_rect_10x3 = cv2.dilate(thresh, kernel_rect_10x3, iterations=x)
    combine1 = np.hstack((thresh, thresh_rect_3x5, thresh_rect_5x3, thresh_rect_10x3))

    thresh_cross = cv2.dilate(thresh, kernel_cross, iterations=x)
    thresh_ellip = cv2.dilate(thresh, kernel_ellip, iterations=x)
    thresh_circle = cv2.dilate(thresh, kernel_circle, iterations=x)
    combine2 = np.hstack((thresh, thresh_cross, thresh_ellip, thresh_circle))

    cv2.imshow(f"Iteracja {x}: Orginalny | 3x3 | 5x5 | 10x10", combine)
    cv2.waitKey(0)
    cv2.imshow(f"Iteracja {x}: Orginalny | 3x5 | 5x3 | 10x3", combine1)
    cv2.waitKey(0)
    cv2.imshow(f"Iteracja {x}: Orginalny | cross | ellip | circle", combine2)
    cv2.waitKey(0)


cv2.waitKey(0)



cv2.destroyAllWindows()