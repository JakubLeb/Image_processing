import cv2
import numpy as np


def connect_bg_with_selfie(bg_img, selfie_img, frame_img):
    # Zmiana rozmiaru obrazów
    same_height = 800
    same_width = 800

    # Zmiana rozmiaru wszystkich obrazów
    bg_img = cv2.resize(bg_img, (same_width, same_height))
    selfie_img = cv2.resize(selfie_img, (same_width, same_height))
    frame_img = cv2.resize(frame_img, (same_width, same_height))

    # Konwersja obrazu do przestrzeni kolorów HSV dla lepszej detekcji zieleni
    hsv_selfie_img = cv2.cvtColor(selfie_img, cv2.COLOR_BGR2HSV)

    # Zdefiniowanie zakresu kolorów zielonego ekranu
    lower_green = np.array([35, 50, 50])
    upper_green = np.array([85, 255, 255])

    # Utworzenie maski dla zieleni
    combined_mask = cv2.inRange(hsv_selfie_img, lower_green, upper_green)

    # Odwrócenie maski, aby zachować obszary inne niż zielony
    mask_inv = cv2.bitwise_not(combined_mask)

    # Wyodrębnienie selfie bez zielonego tła
    result = cv2.bitwise_and(selfie_img, selfie_img, mask=mask_inv)
    # Wstawienie tła w miejsca, gdzie była zieleń
    result_with_background = np.where(result == 0, bg_img, result)
    # Konwersja wyniku do formatu uint8
    result_with_background = result_with_background.astype(np.uint8)


    # Nakładanie ramki
    if frame_img.shape[2] == 4:  # Sprawdzenie, czy obraz ma kanał alfa
        alpha_channel = frame_img[:, :, 3]  # Kanał alfa
        rgb_channels = frame_img[:, :, :3]  # Kanały RGB

        # Skalowanie kanału alfa do zakresu 0-1
        alpha_mask = alpha_channel / 255.0

        # Nałożenie ramki z uwzględnieniem przezroczystości
        for c in range(3):  # Dla każdego kanału kolorów (R, G, B)
            result_with_background[:, :, c] = (
                    alpha_mask * rgb_channels[:, :, c] +
                    (1 - alpha_mask) * result_with_background[:, :, c]
            ).astype(np.uint8)

    # Wyświetlenie wyniku
    cv2.imshow("Green Screen with Frame", result_with_background)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return result_with_background


# Wczytanie obrazów
bg_img = cv2.imread("bgimg.jpg")
selfie_img = cv2.imread("selfie.jpg")
frame_img = cv2.imread("frame_for_img.png", cv2.IMREAD_UNCHANGED)  # Wczytanie z kanałem alfa

# Wywołanie funkcji
connect_bg_with_selfie(bg_img, selfie_img, frame_img)