import cv2
import numpy as np

img = cv2.imread("gang.jpg",cv2.IMREAD_COLOR)
img = cv2.resize(img, (300,300))

src =cv2.GaussianBlur(img,(3,3),0)
src_gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)

edges1 = cv2.Laplacian(src_gray,cv2.CV_16S,ksize=1)
edges2 = cv2.Laplacian(src_gray,cv2.CV_16S,ksize=3)
edges3 = cv2.Laplacian(src_gray,cv2.CV_16S,ksize=5)


a = cv2.convertScaleAbs(edges1)
b = cv2.convertScaleAbs(edges2)
c = cv2.convertScaleAbs(edges3)


combine = np.hstack((a,b,c))
cv2.imshow("Laplacian", combine)
cv2.imshow("",img)
cv2.waitKey(0)

cv2.destroyAllWindows()