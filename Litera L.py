import cv2
import mediapipe as mp

# Inicjalizacja MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Kamera
cap = cv2.VideoCapture(0)
# Lub film
#cap = cv2.VideoCapture('film z kamery od ulicy')

# Pętla główna
while True:
    _, image = cap.read()

    # Konwersja obrazu z BGR na RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Detekcja pozycji
    results = pose.process(image_rgb)

    # Rysowanie szkieletu, jeśli wykryto pozycję
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        right_arm = results.pose_landmarks.landmark[15].y
        left_shoulder = results.pose_landmarks.landmark[0].y

        wynik = "Litera L" if right_arm - left_shoulder < 0 else "-"
        frame = cv2.putText(image, wynik, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)


    # Wyświetlanie wynikowego obrazu w oknie
    cv2.imshow('Detekcja człowieka (Esc - koniec)', image)

    # Wyjście z pętli
    if cv2.waitKey(1) == 27:
        break

# Finalizacja
cap.release()
cv2.destroyAllWindows()