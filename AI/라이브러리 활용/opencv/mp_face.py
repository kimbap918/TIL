# 1. 라이브러리 불러오기
import cv2
import mediapipe as mp

# 2. mediapipe 초기화
mp_face = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

cap.set(3, 1280)
cap.set(4, 720)

with mp_face.FaceDetection(
    model_selection=0,
    min_detection_confidence=0.5
) as face_detection:
    while(True):
        ret, frame = cap.read()

        if not ret:
            print("카메라가 존재하지 않습니다.")
            exit()

        # cv2.imshow('video input', frame)

        # 얼굴 인식
        frame.flags.writeable = False
        # 입력된 이미지를 BGR -> RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # cv2.imshow('rgb video', image)
        face_result = face_detection.process(image)
        # print(face_result)

        face_image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if face_result.detections:
            for detection in face_result.detections:
                print(detection)
                mp_drawing.draw_detection(face_image, detection)

        cv2.imshow('face detection', face_image)

        # ESC키가 검출되면 종료
        key = cv2.waitKey(30) & 0xff
        if key == 27:
            break

# 메모리 해재
cap.release()
cv2.destroyAllWindows()