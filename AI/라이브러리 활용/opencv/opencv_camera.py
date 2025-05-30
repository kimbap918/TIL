import cv2

# 카메라제어
cap = cv2.VideoCapture('./aespa_mv.mp4')
# 카메라의 싸이즈
# (640, 480), (1280, 720)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Esc 키를 누루면 종료 : waitKey(33)
while cv2.waitKey(33) < 0:
    # 카메라에서 이미지를 하나씩 불러옴.
    _, frame = cap.read()
    # 그레이 처리
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Camera 0 (640, 480)", frame)
    cv2.imshow("Camera GRAY (640, 480)", img_gray)

# 종료
cap.release()
cv2.destroyAllWindows()