import cv2
import numpy as np
def custom_filter(src,ddepth,ind,iteration_amount):
    while ind  != iteration_amount:

        kernel_size = 3 + 2 * (ind % 5)
        kernel = np.ones((kernel_size, kernel_size), dtype=np.float32)
        kernel /= (kernel_size * kernel_size)

        dst = cv2.filter2D(src, ddepth, kernel)

        ind += 1
    return dst

img = cv2.imread("gang.jpg")
img = cv2.resize(img, (300,300))

img_custom_3_iteration = custom_filter(img,-1,0,3)
img_custom_5_iteration = custom_filter(img,-1,0,5)
img_custom_10_iteration = custom_filter(img,-1,0,10)

combine = np.hstack((img , img_custom_3_iteration , img_custom_5_iteration, img_custom_10_iteration))
cv2.imshow("Obrazy z filtrem median", combine)

cv2.waitKey(0)

cv2.destroyAllWindows()