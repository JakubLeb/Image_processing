import cv2
import numpy as np
import random

def add_noise(img):
    row, col, *channels = img.shape
    num_pixels = random.randint(300, 10000)

    for i in range(num_pixels):
        x = random.randint(0, col - 1)
        y = random.randint(0, row - 1)
        img[y, x] = 255

    num_pixels = random.randint(300, 10000)
    for i in range(num_pixels):
        x = random.randint(0, col - 1)
        y = random.randint(0, row - 1)
        img[y, x] = 0

    return img

img = cv2.imread("gang.jpg")
img = cv2.resize(img, (300, 300))

noisy_img = add_noise(img.copy())

gaussian_blur = cv2.GaussianBlur(noisy_img, (3, 3), 0)
median_blur = cv2.medianBlur(noisy_img, 3)
bilateral_blur = cv2.bilateralFilter(noisy_img, 15, 95, 95)

combine = np.hstack((noisy_img,gaussian_blur,median_blur,bilateral_blur))
cv2.imshow("obrazy", combine)

cv2.waitKey(0)
cv2.destroyAllWindows()