import cv2
import numpy as np

def connect_bg_with_selfie(bg_img, selfie_img, resolution):
    # Zmiana rozmiaru obrazów do takich samych wymiarów
    bg_height, bg_width, bg_channels = bg_img.shape
    selfie_height, selfie_width, selfie_channels = selfie_img.shape

    # Ustalenie wspólnych wymiarów na podstawie parametru resolution
    if resolution == 'max':
        same_height = max(bg_height, selfie_height)
        same_width = max(bg_width, selfie_width)
    elif resolution == 'min':
        same_height = min(bg_height, selfie_height)
        same_width = min(bg_width, selfie_width)
    elif resolution == 'mid':
        same_height = (bg_height + selfie_height) // 2
        same_width = (bg_width + selfie_width) // 2
    else:
        print("Nieprawidłowa wartość parametru resolution")
        return

    # Zmiana rozmiaru obu obrazów do wspólnych wymiarów
    bg_img = cv2.resize(bg_img, (same_width, same_height))
    selfie_img = cv2.resize(selfie_img, (same_width, same_height))

    # Konwersja selfie na przestrzeń kolorów HSV w celu lepszej detekcji zieleni
    hsv_selfie_img = cv2.cvtColor(selfie_img, cv2.COLOR_BGR2HSV)

    # Zdefiniowanie zakresu koloru zielonego (greenscreen)
    lower_green = np.array([35, 50, 50])
    upper_green = np.array([85, 255, 255])

    # Utworzenie maski dla koloru zielonego
    combined_mask = cv2.inRange(hsv_selfie_img, lower_green, upper_green)
    combined_mask = cv2.medianBlur(combined_mask, 7)

    # Sprawdzenie, czy wykryto istotny obszar zieleni
    if np.sum(combined_mask) == 0:
        no_greenscreen = selfie_img.copy()
        cv2.putText(no_greenscreen, 'No greenscreen', (same_width // 2 - 150, same_height // 2),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, lineType=cv2.LINE_AA)
        cv2.imshow("Green Screen", no_greenscreen)
        return

    # Odwrócenie maski w celu zachowania obszarów innych niż zielony
    mask_inv = cv2.bitwise_not(combined_mask)

    # Wyodrębnienie selfie bez zielonego tła
    result = cv2.bitwise_and(selfie_img, selfie_img, mask=mask_inv)

    # Wstawienie obrazu tła w miejsca zielonych obszarów
    result_with_background = np.where(result == 0, bg_img, result)
    result_with_background = result_with_background.astype(np.uint8)

    # Wyświetlenie wyniku
    cv2.imshow("Green Screen", result_with_background)
    return result_with_background

# Wczytanie obrazu tła
bg_img = cv2.imread("bgimg.jpg")

# Wczytanie wideo i przetwarzanie klatek
cap = cv2.VideoCapture("video_without_green_screen.mp4")
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        connect_bg_with_selfie(bg_img, frame, 'min')
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
