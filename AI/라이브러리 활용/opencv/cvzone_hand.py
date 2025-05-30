# 라이브러리 설치
from cvzone.HandTrackingModule import HandDetector
import cv2

cap = cv2.VideoCapture(0)

detector = HandDetector(
    staticMode=False,
    maxHands=2,
    modelComplexity=1,
    detectionCon=0.5,
    minTrackCon=0.5
)

while True:
    ret, frame = cap.read()

    hands, img = detector.findHands(frame,draw=True,flipType=True)

    # 오른손 왼속 채크
    if hands:
        for hand in hands:
            print(hand['type'])

    cv2.imshow('hand view', img)

    # 특정 키를 누루면 종료
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()