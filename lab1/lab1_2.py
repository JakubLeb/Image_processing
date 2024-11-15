import cv2


# Wczytaj obraz z pliku 'gang.jpg'
img = cv2.imread("gang.jpg")
# Zapisz ten sam obraz pod nazwą 'same_gang.jpg'
cv2.imwrite('same_gang.jpg', img)