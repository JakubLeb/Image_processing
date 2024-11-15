import cv2
import numpy as np

# Wczytanie obrazu z pliku "gang.jpg"
img = cv2.imread("gang.jpg")

# Pobranie liczby wierszy (rows), kolumn (cols) oraz kanałów (_channels) z kształtu obrazu
rows, cols, _channels = map(int, img.shape)

# Macierz transformacji do odbicia obrazu w poziomie (oś X)
# Wartości dla osi Y są odwrócone, a oś X pozostaje bez zmian
H = np.float32([[1, 0, 0], [0, -1, rows], [0,  0, 1]])

# Macierz transformacji do odbicia obrazu w pionie (oś Y)
# Wartości dla osi X są odwrócone, a oś Y pozostaje bez zmian
V = np.float32([[-1, 0, cols], [0, 1, 0], [0, 0, 1]])

# Zastosowanie macierzy H do odbicia obrazu w poziomie
reflected_img_horizontally = cv2.warpPerspective(img, H, (int(cols), int(rows)))

# Zastosowanie macierzy V do odbicia obrazu w pionie
reflected_img_vertically = cv2.warpPerspective(img, V, (int(cols), int(rows)))

# Wyświetlenie odbitego w poziomie obrazu
cv2.imshow("test", reflected_img_horizontally)
k = cv2.waitKey(0)

# Wyświetlenie odbitego w pionie obrazu
cv2.imshow("test", reflected_img_vertically)
k = cv2.waitKey(0)

# Zniszczenie wszystkich otwartych okienek OpenCV
cv2.destroyAllWindows()
