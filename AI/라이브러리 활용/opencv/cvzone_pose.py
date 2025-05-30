# 라이브러리 불러오기
from cvzone.PoseModule import PoseDetector
import cv2

cap = cv2.VideoCapture(0)

# 포즈 설정
detector = PoseDetector(
    staticMode=False,
    modelComplexity=1,
    smoothLandmarks=True,
    enableSegmentation=False,
    smoothSegmentation=True,
    detectionCon=0.5,
    trackCon=0.5
)

while True:
    ret, frame = cap.read()

    img = detector.findPose(frame)

    cv2.imshow('pose', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()