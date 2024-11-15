import cv2
import numpy as np
import matplotlib.pyplot as plt

# Wczytanie i przeskalowanie obrazu
img = cv2.imread("malpa.jpg")
img = cv2.resize(img, (250,250))

# Utworzenie histogramu dla każdego kanału koloru (B,G,R)
color = ('b','g','r')
for i,col in enumerate(color):
    # calcHist parametry: [obraz], [indeks kanału], maska, [liczba przedziałów], [zakres wartości]
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr, color=col)
    plt.xlim([0,256])

# Wyświetlenie histogramu
plt.show()

cv2.destroyAllWindows()