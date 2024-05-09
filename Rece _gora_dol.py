import cv2
import mediapipe as mp

# Inicjalizacja MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Kamera
cap = cv2.VideoCapture(0)

# Pętla główna
while True:
    _, image = cap.read()

    # Detekcja pozycji
    results = pose.process(image)

    # Rysowanie szkieletu, jeśli wykryto pozycję
    if results.pose_landmarks is not None:
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        pacha_l = results.pose_landmarks.landmark[11]
        lokiec_l = results.pose_landmarks.landmark[13]
        nadg_l = results.pose_landmarks.landmark[19]
        pacha_p = results.pose_landmarks.landmark[12]
        lokiec_p = results.pose_landmarks.landmark[14]
        nadg_p = results.pose_landmarks.landmark[20]

        lewa_w_gorze = pacha_l.y > lokiec_l.y and lokiec_l.y > nadg_l.y
        prawa_w_gorze = pacha_p.y > lokiec_p.y and lokiec_p.y > nadg_p.y

        text = 'obie rece w dole'
        if lewa_w_gorze and prawa_w_gorze:
            text = 'obie w GORZE'
        elif lewa_w_gorze:
            text = 'LEWA GORA'
        elif prawa_w_gorze:
            text = 'PRAWA GORA'

        image = cv2.putText(image, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0), 2, cv2.LINE_AA)

    # Wyświetlanie wynikowego obrazu w oknie
    cv2.imshow('Detekcja człowieka (Esc - koniec)', image)

    # Wyjście z pętli
    if cv2.waitKey(1) == 27:
        break

# Finalizacja
cap.release()
cv2.destroyAllWindows()