import cv2
import mediapipe as mp

# Inicjalizacja modułu MediaPipe
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Inicjalizacja kamery
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Konwersja kolorów z BGR do RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Rozpoznanie punktów twarzy na obrazie
    results = face_mesh.process(frame_rgb)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # Rysowanie punktów twarzy
            for landmark in face_landmarks.landmark:
                x, y = int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0])
                cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)

    # Wyświetlenie wynikowego obrazu
    cv2.imshow('Face Mesh', frame)

    # Wyjście z pętli
    if cv2.waitKey(1) == 27:
        break

# Zwolnienie zasobów
cap.release()
cv2.destroyAllWindows()