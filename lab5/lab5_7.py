import cv2
import numpy as np

img = cv2.imread("gang.jpg")
img = cv2.resize(img, (300, 300))

mean = 0
sigma = 25
gaussian_noise = np.random.normal(mean, sigma, img.shape).astype(np.float32)
noisy_img = cv2.add(img.astype(np.float32), gaussian_noise)
noisy_img = np.clip(noisy_img, 0, 255).astype(np.uint8)

gaussian_blur = cv2.GaussianBlur(noisy_img, (5, 5), 5)
median_blur = cv2.medianBlur(noisy_img, 7)
bilateral_blur = cv2.bilateralFilter(noisy_img, 9, 100, 100)

combine = np.hstack((noisy_img, gaussian_blur, median_blur, bilateral_blur))
cv2.imshow("Comparison", combine)
cv2.waitKey(0)
cv2.destroyAllWindows()