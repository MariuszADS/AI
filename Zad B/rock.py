# import cv2
# import mediapipe as mp
#
# mp_pose = mp.solutions.pose
# pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
# mp_drawing = mp.solutions.drawing_utils
#
# cap = cv2.VideoCapture(0)
#
# right_score = 0
# left_score = 0
#
# def get_hand_gesture(results, side):
#     if side == "right":
#         if results.pose_landmarks:
#             right_hand = results.pose_landmarks.landmark[15].x
#             right_shoulder = results.pose_landmarks.landmark[0].x
#             if right_hand < right_shoulder:
#                 return "rock"
#     elif side == "left":
#         if results.pose_landmarks:
#             left_hand = results.pose_landmarks.landmark[14].x
#             left_shoulder = results.pose_landmarks.landmark[0].x
#             if left_hand < left_shoulder:
#                 return "rock"
#
#     return None
#
# while True:
#     _, image = cap.read()
#
#     image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#
#     results = pose.process(image_rgb)
#
#     if results.pose_landmarks:
#         mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
#
#         right_gesture = get_hand_gesture(results, "right")
#         left_gesture = get_hand_gesture(results, "left")
#
#         if right_gesture and left_gesture:
#             if right_gesture == "rock" and left_gesture == "scissors":
#                 right_score += 1
#             elif right_gesture == "scissors" and left_gesture == "paper":
#                 right_score += 1
#             elif right_gesture == "paper" and left_gesture == "rock":
#                 right_score += 1
#             elif right_gesture == "rock" and left_gesture == "paper":
#                 left_score += 1
#             elif right_gesture == "scissors" and left_gesture == "rock":
#                 left_score += 1
#             elif right_gesture == "paper" and left_gesture == "scissors":
#                 left_score += 1
#
#     cv2.putText(image, f"Right Score: {right_score}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
#     cv2.putText(image, f"Left Score: {left_score}", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
#
#     cv2.imshow('Rock, Paper, Scissors Game', image)
#
#     if cv2.waitKey(1) == 27:
#         break
#
# cap.release()
# cv2.destroyAllWindows()

# ======================================================================================================================

import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

right_score = 0
left_score = 0

def get_hand_gesture(results, side):
    if side == "right":
        if results.pose_landmarks:
            right_hand = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST.value].x
            right_shoulder = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x
            if right_hand < right_shoulder:
                return "rock"
            else:
                return "scissors"  # Assuming the other gesture is "scissors"
    elif side == "left":
        if results.pose_landmarks:
            left_hand = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST.value].x
            left_shoulder = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x
            if left_hand < left_shoulder:
                return "rock"
            else:
                return "scissors"  # Assuming the other gesture is "scissors"

    return None

while True:
    success, image = cap.read()

    if not success:
        print("Ignoring empty camera frame.")
        continue

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    results = pose.process(image_rgb)

    if results.pose_landmarks:
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        right_gesture = get_hand_gesture(results, "right")
        left_gesture = get_hand_gesture(results, "left")

        if right_gesture and left_gesture:
            if (right_gesture == "rock" and left_gesture == "scissors") or \
               (right_gesture == "scissors" and left_gesture == "paper") or \
               (right_gesture == "paper" and left_gesture == "rock"):
                right_score += 1
            elif (right_gesture == "rock" and left_gesture == "paper") or \
                 (right_gesture == "scissors" and left_gesture == "rock") or \
                 (right_gesture == "paper" and left_gesture == "scissors"):
                left_score += 1

    cv2.putText(image, f"Right Score: {right_score}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.putText(image, f"Left Score: {left_score}", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow('Rock, Paper, Scissors Game', image)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()