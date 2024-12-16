import cv2

def detect_and_display_face(img):

    # Konwersja do skali szarości
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Wczytanie klasyfikatora Haarcascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Wykrywanie twarzy
    faces = face_cascade.detectMultiScale(gray_image, 1.1, 9)

    # Rysowanie prostokątów wokół wykrytych twarzy
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Wyświetlenie obrazu z zaznaczoną twarzą
    cv2.imshow("Wykrywanie twarzy", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image = cv2.imread("person.jpg")
detect_and_display_face(image)
