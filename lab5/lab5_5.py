import cv2
import numpy as np

def sharpen_gaussian(img):
    sharpened = cv2.GaussianBlur(img, (0, 0), 3)
    sharpened = cv2.addWeighted(img, 1.5, sharpened, -0.5, 0)
    return sharpened

def sharpen_laplacian(img):
    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    sharpened = img + laplacian
    return sharpened.astype(np.uint8)

def sharpen_custom(img):
    kernel = np.array([[-1, -1, -1],
                      [-1, 9, -1],
                      [-1, -1, -1]])
    sharpened = cv2.filter2D(img, -1, kernel)
    return sharpened

img = cv2.imread("gang.jpg")
img = cv2.resize(img, (300, 300))

sharpened_gaussian = sharpen_gaussian(img.copy())
sharpened_laplacian = sharpen_laplacian(img.copy())
sharpened_custom = sharpen_custom(img.copy())

combine = np.hstack((img, sharpened_gaussian, sharpened_laplacian, sharpened_custom))
cv2.imshow("Image Sharpening Techniques", combine)
cv2.waitKey(0)
cv2.destroyAllWindows()