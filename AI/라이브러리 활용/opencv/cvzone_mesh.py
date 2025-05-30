# 라이브러리 불러오기
from cvzone.FaceMeshModule import FaceMeshDetector
import cv2

cap = cv2.VideoCapture(0)

# 얼굴인식 함수
detector = FaceMeshDetector(
    staticMode=False,
    maxFaces=1,
    minDetectionCon=0.5,
    minTrackCon=0.5
)

while True:
    ret, frame = cap.read()

    img, faces = detector.findFaceMesh(frame, draw=True)

    cv2.imshow('mash', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()