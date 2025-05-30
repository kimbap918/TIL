import torch

# 모델 불러오기 : Pre-Trained Model
model = torch.hub.load("ultralytics/yolov5", "yolov5s")

# 셈플 이미지
img = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/2023_MMA_IVE.jpg/960px-2023_MMA_IVE.jpg"

# 예측 : Predict
results = model(img)

# 결과 확인
results.print() # 콘솔에 출력
results.show() # 화면에 표시
results.save() # 저장
