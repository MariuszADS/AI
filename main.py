# import numpy as np
# import cv2
#
# arr = np.zeros([400, 600, 3])
#
# for i in range(600):
#     arr[:, i, 0] = 255 * i / 600
#
# cv2.arrowedLine(arr, (100,100),(3919,599),(0,255,255))
#
# cv2.imshow("Okienko", arr)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# import numpy as np
# import cv2
#
# # Tworzenie obrazu o wymiarach 400x600 pikseli (wysokość x szerokość x kanały)
# img = np.zeros((400, 600, 3), dtype=np.uint8)
#
# # Rysowanie deski
# cv2.rectangle(img, (50, 300), (550, 380), (0, 255, 0), -1)  # Korpus deski
# cv2.rectangle(img, (120, 230), (160, 300), (0, 0, 255), -1)  # Kółka (czerwone)
# cv2.rectangle(img, (340, 230), (380, 300), (0, 0, 255), -1)  # Kółka (czerwone)
# cv2.rectangle(img, (180, 230), (320, 250), (255, 255, 255), -1)  # Deska (biała)
# cv2.rectangle(img, (180, 250), (320, 270), (0, 0, 255), -1)  # Deska (czerwona)
#
# # Rysowanie osi (strzałki)
# cv2.arrowedLine(img, (150, 100), (150, 230), (255, 0, 0), 5)  # Oś X
# cv2.arrowedLine(img, (150, 400), (150, 270), (255, 0, 0), 5)  # Oś X
#
# cv2.imshow('Skateboard', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



import matplotlib.pyplot as plt
import numpy as np

# Dane geograficzne dla Danii i Szwecji
denmark = (55.6761, 12.5683)
sweden = (59.3293, 18.0686)

# Rysowanie mapy Europy
plt.figure(figsize=(10, 6))
plt.scatter(denmark[1], denmark[0], color='blue', label='Dania')
plt.scatter(sweden[1], sweden[0], color='red', label='Szwecja')
plt.plot([denmark[1], sweden[1]], [denmark[0], sweden[0]], color='green', linestyle='-', linewidth=2, label='Most')

# Dodanie etykiet
plt.text(denmark[1], denmark[0], 'Dania', fontsize=12, ha='right')
plt.text(sweden[1], sweden[0], 'Szwecja', fontsize=12, ha='right')
plt.text((denmark[1] + sweden[1]) / 2, (denmark[0] + sweden[0]) / 2, 'Most', fontsize=12)

# Konfiguracja wykresu
plt.xlabel('Długość geograficzna')
plt.ylabel('Szerokość geograficzna')
plt.title('Mapa Europy z mostem pomiędzy Danią a Szwecją')
plt.legend()

# Wyświetlenie wykresu
plt.grid(True)
plt.show()
