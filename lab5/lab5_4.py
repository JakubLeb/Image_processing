import cv2
import numpy as np

def custom_filter(src, ddepth, iteration_amount):
    for ind in range(iteration_amount):
        kernel_size = 3 + 2 * (ind % 5)
        kernel = np.ones((kernel_size, kernel_size), dtype=np.float32) / (kernel_size * kernel_size)
        src = cv2.filter2D(src, ddepth, kernel)
    return src

img = cv2.imread("gang.jpg")
img = cv2.resize(img, (300, 300))

img_custom_3_iteration = custom_filter(img.copy(), -1, 3)
img_custom_5_iteration = custom_filter(img.copy(), -1, 5)
img_custom_10_iteration = custom_filter(img.copy(), -1, 10)

combine = np.hstack((img, img_custom_3_iteration, img_custom_5_iteration, img_custom_10_iteration))
cv2.imshow("Obrazy z filtrem custom", combine)
cv2.waitKey(0)
cv2.destroyAllWindows()