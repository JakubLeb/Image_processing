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


cap = cv2.VideoCapture("video_person.mp4")
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        frame = cv2.resize(frame, (640, 480))
        detect_and_display_face(frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()