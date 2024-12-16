import cv2
import numpy as np

def connect_bg_with_selfie(bg_img, selfie_img, resolution, edge_method):
    # Zmiana rozmiaru obrazów
    bg_height, bg_width, bg_channels = bg_img.shape
    selfie_height, selfie_width, selfie_channels = selfie_img.shape

    if (resolution == 'max'):
        same_height = max(bg_height, selfie_height)
        same_width = max(bg_width, selfie_width)
    elif (resolution == 'min'):
        same_height = min(bg_height, selfie_height)
        same_width = min(bg_width, selfie_width)
    elif (resolution == 'mid'):
        same_height = (bg_height + selfie_height) // 2
        same_width = (bg_width + selfie_width) // 2
    else:
        print("Błędna wartość zmiennej resolution")
        return 0

    # Zmiana rozmiaru obu obrazów do wspólnych wymiarów
    bg_img = cv2.resize(bg_img, (same_width, same_height))
    selfie_img = cv2.resize(selfie_img, (same_width, same_height))

    # Konwersja obrazu do przestrzeni kolorów HSV
    hsv_selfie_img = cv2.cvtColor(selfie_img, cv2.COLOR_BGR2HSV)

    # Zdefiniowanie zakresu kolorów zielonego ekranu
    lower_green = np.array([35, 50, 50])
    upper_green = np.array([85, 255, 255])

    # Utworzenie maski dla zieleni
    combined_mask = cv2.inRange(hsv_selfie_img, lower_green, upper_green)

    # Wygładzanie krawędzi maski różnymi metodami
    if edge_method == 'gaussian':
        combined_mask = cv2.GaussianBlur(combined_mask, (7, 7), 0)
        _, combined_mask = cv2.threshold(combined_mask, 127, 255, cv2.THRESH_BINARY)

    elif edge_method == 'median':
        combined_mask = cv2.medianBlur(combined_mask, 5)

    elif edge_method == 'morphological':
        kernel = np.ones((11, 11), np.uint8)
        combined_mask = cv2.morphologyEx(combined_mask, cv2.MORPH_OPEN, kernel)
        combined_mask = cv2.morphologyEx(combined_mask, cv2.MORPH_CLOSE, kernel)

    else:
        print("Nieznana metoda wygładzania krawędzi")
        return 0

    # Odwrócenie maski
    mask_inv = cv2.bitwise_not(combined_mask)

    # Wyodrębnienie selfie bez zielonego tła
    result = cv2.bitwise_and(selfie_img, selfie_img, mask=mask_inv)

    # Wstawienie tła w miejsca, gdzie była zieleń
    result_with_background = np.where(result == 0, bg_img, result)

    # Konwersja wyniku do formatu uint8
    result_with_background = result_with_background.astype(np.uint8)

    # Wyświetlenie wyniku
    cv2.imshow(f"Green Screen - {edge_method}", result_with_background)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return result_with_background


# Wczytanie obrazów
bg_img = cv2.imread("bgimg.jpg")
selfie_img = cv2.imread("selfie.jpg")

# Testowanie różnych metod wygładzania krawędzi
methods = ['gaussian', 'median', 'morphological']

for method in methods:
    connect_bg_with_selfie(bg_img, selfie_img, 'max', edge_method=method)