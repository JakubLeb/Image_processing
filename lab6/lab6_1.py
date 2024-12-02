import cv2
import numpy as np


img = cv2.imread("malpa.jpg",cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (300,300))

edges1 = cv2.Canny(img,0,100)
edges2 = cv2.Canny(img,100,200)
edges3 = cv2.Canny(img,200,300)


combine = np.hstack((img,edges1,edges2,edges3))
cv2.imshow("Canny", combine)
cv2.waitKey(0)

cv2.destroyAllWindows()