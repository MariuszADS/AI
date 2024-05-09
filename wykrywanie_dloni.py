import cv2
import mediapipe as mp

# Inicjalizacja modułu Mediapipe do wykrywania dłoni
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Inicjalizacja kamery
capture = cv2.VideoCapture(0)

with mp_hands.Hands(static_image_mode=False, min_detection_confidence=0.7, min_tracking_confidence=0.7, max_num_hands=2) as hands:
    while True:
        _, frame = capture.read()

        # Wykrywanie dłoni
        results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Rysowanie punktów (landmarków)
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        cv2.imshow('Wykrywanie dłoni', frame)

        if cv2.waitKey(1) == 27:  # Naciśnięcie klawisza Esc zamyka okno
            break

cv2.destroyAllWindows()
capture.release()