import cv2
import mediapipe as mp

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Camera
cap = cv2.VideoCapture(0)

# Main loop
while True:
    _, image = cap.read()

    # Convert image from BGR to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Detect pose
    results = pose.process(image_rgb)

    # Draw skeleton and check poses
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Check poses
        poses = []
        right_arm = results.pose_landmarks.landmark[15].y
        left_shoulder = results.pose_landmarks.landmark[0].y
        poses.append("Litera L" if right_arm - left_shoulder < 0 else "-")

        left_arm = results.pose_landmarks.landmark[0].y
        right_arm = results.pose_landmarks.landmark[14].y
        poses.append("Litera P" if right_arm - left_arm < 0 else "-")

        head_nose = results.pose_landmarks.landmark[0].y
        left_shoulder = results.pose_landmarks.landmark[12].y
        poses.append("Glowa po lewej" if left_shoulder - head_nose < 0 else "-")

        # Check if all poses are correct
        if all(pose!= "-" for pose in poses):
            wynik = "Sukces!"
        else:
            wynik = ", ".join(poses)

        # Display result
        frame = cv2.putText(image, wynik, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

    # Display output image
    cv2.imshow('Detekcja człowieka (Esc - koniec)', image)

    # Exit loop
    if cv2.waitKey(1) == 27:
        break

# Finalize
cap.release()
cv2.destroyAllWindows()