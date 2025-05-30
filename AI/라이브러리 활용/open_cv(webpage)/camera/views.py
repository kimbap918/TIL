from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse

# 카메라 제어 : OpenCV
import cv2
import dlib
import numpy as np

detector = dlib.get_frontal_face_detector()

class FaceDetector:
    def __init__(self):
        self.detector = dlib.get_frontal_face_detector()
        self.image = None
        self.detections = None

    def load_image(self, image):
        self.image = image

    def detect_faces(self, upsample_num_times=1):
        if self.image is None:
            raise ValueError("Image not loaded.")
        self.detections = self.detector(self.image, upsample_num_times)
        return self.detections

    def draw_faces(self):
        if self.detections is None:
            raise ValueError("No faces.")
        for det in self.detections:
            x, y, w, h = det.left(), det.top(), det.width(), det.height()
            cv2.rectangle(self.image, (x, y), (x + w, y + h), (0, 0, 255), 2)

face_detector = FaceDetector()

# Create your views here.
def index(request):
    return render(request, "./camera/camera.html")

def video_feed(request):
    # return HttpResponse("비디오 영역입니다.")
    return StreamingHttpResponse(stream(request),
    content_type='multipart/x-mixed-replace;boundary=frame')

# 영상을 실시간으로 전송하는 함수
def stream(request):
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            return HttpResponse("카메라 인식에 실패하였습니다.")

        try:
            face_detector.load_image(frame)
            face_cnt = face_detector.detect_faces()
            print("face_cnt =", len(face_cnt))

            face_detector.draw_faces()
        except:
            print("error")

        # 서버에 데이터를 전송하는 방법(스트리밍)
        # 이미지를 binary로 웹에서 전송 가능한 형태로 변환
        image_bytes = cv2.imencode('.jpg', frame)[1].tobytes()
        # 서버로 전송
        yield(b'--frame\r\n'
        b'Content-type:image/jpeg\r\n\r\n' +
        image_bytes + b'\r\n')


        