import cv2
import numpy as np

# Wczytanie i przygotowanie obrazów
a = cv2.imread("gang.jpg")
b = cv2.imread("malpa.jpg")
a = cv2.resize(a, (250,250))
b = cv2.resize(b, (250,250))

# Podstawowe operacje arytmetyczne na obrazach
a_add_b = cv2.add(a, b)
a_subtract_b = cv2.subtract(a, b)
b_subtract_a = cv2.subtract(b, a)
a_times_b = cv2.multiply(a, b)
a_divide_b = cv2.divide(a, b + 1)  # +1 aby uniknąć dzielenia przez 0
b_divide_a = cv2.divide(b, a + 1)

# Połączenie obrazów do wyświetlenia
first3 = np.hstack((a_add_b, a_subtract_b, b_subtract_a))
last3 = np.hstack((a_times_b, a_divide_b, b_divide_a))

# Wyświetlenie i zapis wyników
cv2.imshow("Operacje na obrazach", first3)
cv2.waitKey(0)
cv2.imshow("Operacje na obrazach", last3)
cv2.waitKey(0)

# Zapis wyników do plików
cv2.imwrite('zadanie8/a_add_b.jpg',a_add_b)
cv2.imwrite('zadanie8/a_subtract_b.jpg',a_subtract_b)
cv2.imwrite('zadanie8/b_subtract_a.jpg',b_subtract_a)
cv2.imwrite('zadanie8/a_times_b.jpg',a_times_b)
cv2.imwrite('zadanie8/a_divide_b.jpg',a_divide_b)
cv2.imwrite('zadanie8/b_divide_a.jpg',b_divide_a)

cv2.destroyAllWindows()