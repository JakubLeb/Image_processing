import cv2
import numpy as np

# Wczytanie obrazu
img = cv2.imread("zadanie4.jpg")

# Sprawdzenie wartości przed normalizacją
min_val = np.min(img)
max_val = np.max(img)
print(f"Przed normalizacją - Min: {min_val}, Max: {max_val}")

# Normalizacja obrazu do zakresu 0-255
normalized_img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)

# Sprawdzenie wartości po normalizacji
min_val_after = np.min(normalized_img)
max_val_after = np.max(normalized_img)
print(f"Po normalizacji - Min: {min_val_after}, Max: {max_val_after}")

# Wyświetlenie wyniku
combined_img = np.hstack((img, normalized_img))
cv2.imshow("Obrazy obok siebie", combined_img)
cv2.waitKey(0)
cv2.destroyAllWindows()