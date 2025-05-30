################################################################################
# 프로젝트명 : YOLO v5 위험동물 판별 프로그램
# 제작기간 : 20221201 ~ 20221206
# 제작팀 : 팀명(010-1234-5678, 12345678@google.com)
# 사용언어 : Python 3.9, YoloV5, OpenCV
# 사용라이브러리 : pafy(Youbtube 연동), winsound(경보음)
# 기타 내용 : 곰 class 21(bear), 인식률 20%
################################################################################

import torch
import numpy as np
import cv2
import pafy
from time import time # 프로세스 동작시간 계산 (끝시간 - 시작시간)
import winsound

# 영상파일 불러오기
url = 'bear.mp4'

# 영상 불러오기
# video = pafy.new(url)
# print(f'영상제목 : {video.title}')

# play = video.getbest(preftype='mp4')
cap = cv2.VideoCapture(url)

# YOLO v5 모델 불러오기
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
model.conf = 0.2
model.classes = [21]

# print(model.names)

while cv2.waitKey(33) < 0 :
    start_time = time()
    ret, frame = cap.read()
    # print('ret =', ret)

    # 영상 프레임 크기
    x_shape = frame.shape[1]
    y_shape = frame.shape[0]
    # print(f'X 크기 = {x_shape}, Y 크기 = {y_shape}')

    results = model(frame)
    # CPU가 64비트니까 numpy도 64비트로 바꿔야 함
    labels, cord = results.xyxy[0][ : , -1].cpu().numpy(), results.xyxyn[0][ : , : -1].cpu().numpy()
    # print(results.xyxyn[0]) # xyxyn은 좌표정보를 찾는 것
    # print('label =', labels)
    # print('cord =', cord)

    # 집 바운딩박스 처리
    cv2.rectangle(frame, (150, 130), (580, 470), (0,255, 0), 2)

    if len(labels) > 0 :
        # print('라벨 :', labels)
        # print('객체명 :', model.names[int(labels)])

        # bounding box 작업하기
        # print('cord =', cord)
        
        # 실제 크기
        x1 = int(cord[0][0] * x_shape)
        y1 = int(cord[0][1] * y_shape)
        x2 = int(cord[0][2] * x_shape)
        y2 = int(cord[0][3] * y_shape)
        # print(f'x1 = {x1}, y1 = {y1}, x2={x2}, y2={y2}')

        # 바운딩 박스 그리기
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
        # 객체명 표시하기
        names_title = model.names[labels[0]] + f'({x1},{y1},{x2},{y2})'
        cv2.putText(frame, names_title, (x1, y1-10), cv2.FONT_HERSHEY_COMPLEX, 0.9, (0, 0, 255), 2)

        # 곰이 집 범위 내 접근 시 경고 알림
        if(x1 <= 580) :
            cv2.rectangle(frame, (150, 130), (580, 470), (0, 0, 255), 2)
            cv2.putText(frame, 'WARNING', (150, 130), cv2.FONT_HERSHEY_COMPLEX, 0.9, (0, 0, 255), 2)
            winsound.Beep(
                frequency=440, # Hz
                duration=500  # milliseconds
            )

    end_time = time()
    fps = round(1/np.round(end_time - start_time, 3), 2)
    # print(f'프레임 속도 = {fps}')
    cv2.putText(frame, f'fps : {fps}', (15, 30), cv2.FONT_HERSHEY_COMPLEX, 0.9, (0, 0, 255), 2)
    cv2.imshow('Video', frame)

cap.release()
cv2.destroyAllWindows()