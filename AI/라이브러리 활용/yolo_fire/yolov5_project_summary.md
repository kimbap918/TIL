
# YOLOv5 기반 객체 검출 프로젝트 정리

---

## ✅ 1. YOLO vs CNN

| 구분        | CNN                      | YOLO                          |
|-------------|---------------------------|-------------------------------|
| 사용 목적   | 이미지 분류               | 객체 탐지 (실시간 감지)       |
| 처리 방식   | 전체 이미지 → 단일 라벨   | 이미지 한 번에 여러 객체 탐지 |
| 속도        | 느릴 수 있음              | 매우 빠름 (You Only Look Once) |

---

## ✅ 2. 설치 및 가상환경 설정

```bash
conda create -n p38_cnn python=3.8 -y
conda activate p38_cnn
git clone https://github.com/ultralytics/yolov5.git
cd yolov5
pip install -r requirements.txt
```

---

## ✅ 3. 객체 감지 실행 예시

```bash
python detect.py --weights yolov5s.pt --source ./source/fire.mp4
```

### 🔹 Confidence 설정
```bash
python detect.py --weights yolov5s.pt --source aespa.mp4 --conf 0.2
```

### 🔹 특정 클래스만 탐지
```bash
python detect.py --weights yolov5s.pt --source fire.mp4 --classes 15
```

---

## ✅ 4. 라벨링 툴 (LabelImg)

```bash
pip install labelimg
cd labeling
labelimg
```

- `.jpg` : 이미지 파일  
- `.xml`, `.json` : 라벨 정보 파일 (YOLO 형식으로 저장 가능)

---

## ✅ 5. Custom 학습용 데이터셋 구조

```
dataset/
├── train/
├── val/
└── test/
```

- `data.yaml` 예시:

```yaml
train: ./dataset/train/images
val: ./dataset/val/images

nc: 1
names: ['fire']
```

---

## ✅ 6. Google Colab 학습 명령어

```python
!python train.py --img 416 --batch 16 --epochs 300 \
--data /content/data.yaml \
--cfg ./models/yolov5s.yaml \
--weights yolov5s.pt \
--name fire_yolov5s_results
```

### 🔹 학습 결과 압축

```python
!zip -r /content/fire_result.zip /content/runs/train/fire_yolov5s_results/
```

---

## ✅ 7. GPU가 없는 환경에서 실행 문제 해결

```python
import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath
```

---

## ✅ 8. 실서비스 응용 구조 예시 (AI Access)

```
회원 사진 업로드 (5장)
→ 전처리
→ 임베딩 (face_recognition)
→ 벡터 DB (FAISS 등)
→ 유사도 비교 후 승인/비승인 판단
```

---

## ✅ 기타

- YouTube 영상 다운로드:  
  https://www.ssyoutube.com/watch?v=영상ID  
- `labelImg`로 라벨링 후 `.xml` → YOLO 형식으로 변환 필요 시 자동 변환 스크립트 사용 가능

