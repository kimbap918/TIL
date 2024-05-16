
딥러닝 모델은 training할 때의 속도와 inference할 때의 속도가 달라야한다.

Gradient Episodic Memory
https://arxiv.org/abs/1706.08840



제한된 볼츠만 머신
https://velog.io/@chulhongsung/RBM


![](https://i.imgur.com/GNSDAZu.png)

## Two-stage detector(두 단계 객체 검출 모델)
* 이미지 내의 객체를 찾기 위해 두 단계로 구성된 특정한 객체 검출 모델 유형

![](https://i.imgur.com/k2ZBM5F.png)

이 모델은 일반적으로 두 가지 주요 구성 요소 또는 단계로 이루어져 있다.
1. **지역 제안 네트워크 (RPN):**
    - 첫 번째 단계인 RPN은 객체가 포함될 가능성이 높은 지역 제안 또는 후보 경계 상자를 생성한다. 이미지의 모든 가능한 위치를 철저히 평가하는 대신, RPN은 객체가 포함될 가능성이 있는 잠재적인 영역(바운딩 박스) 세트를 제안한다.
    - RPN은 일반적으로 서로 다른 스케일과 종횡비를 가진 앵커 박스를 사용하여 후보 영역을 제안한다. 훈련 중에 이러한 앵커 박스는 개체에 더 잘 맞도록 조정되고 개선된다.

2. **객체 검출 네트워크:** 
    - 두 번째 단계에서는 RPN에 의해 생성된 지역 제안을 사용하여 상세한 객체 분류 및 바운딩 박스 회귀를 수행한다. 이 단계는 제안된 바운딩 박스를 더 정확하게 조정하고 해당 상자 내의 객체의 클래스 레이블을 결정하는 역할을 한다.
    - 두 번째 단계의 일반적인 아키텍처에는 Faster R-CNN이 포함되며, 이는 제안된 지역에서 특징을 추출하고 분류 및 회귀를 위해 완전 연결 레이어를 사용한다.

Two-stage detector는 Faster R-CNN, Mask R-CNN, Cascade R-CNN 등이 있다.


## Single-shot detector (SSD)
* 기존의 two-stage 모델과는 다른 단일 단계(single shot) 접근 방식을 채택하여 속도와 정확도를 향상시키기 위해 설계된 모델
* Anchor Box와 달리, 그리드가 아닌 픽셀을 사용
![](https://i.imgur.com/E1Iw7Tw.png)
SSD는 Selective Search와 같은 전통적인 Region Proposal Network(RPN)을 사용하지 않는다. SSD는 객체 탐지를 위한 네트워크 아키텍처로서, 미리 정의된 여러 크기와 종횡비를 가진 Default Box를 사용하여 객체의 위치를 예측한다.

기존 two-stage detector는 Feature Map에 따라서 Anchor Box가 같이 줄어들었다.

Singgle-shot detoector는 Anchor Box의 크기를 고정하고, Feature Map이 줄어들면 더 넓은 면적을 파악하는 방식이다. 이것은 Sliding Window 방식과 유사하다.
Feature Map이 줄어들면, 각 픽셀은 더 큰 공간 영역에 대응하게 되어 전체 이미지에서 넓은 영역을 파악하는 효과가 있다.


## YOLO(You Only Look Once)
You Only Look Once (YOLO)는 객체 검출을 위한 딥러닝 알고리즘 중 하나로, 주로 실시간 객체 검출에 사용된다. YOLO는 주로 정확성과 속도 사이의 균형을 맞추는 데 중점을 둔다.

YOLO에서는 Mean Average Precision (mAP)이 일반적인 성능 평가 지표로 사용된다. mAP는 객체 검출 모델의 정확성을 측정하는 데 사용되는 평가 지표 중 하나로, Precision-Recall 곡선의 아래 면적을 평균화하여 계산된다.

### 평균 정밀도(Mean Average Precision, mAP)
* 왜 평균평균정밀도일까?

1. **각 클래스에 대한 AP를 평균내기:** 각 객체 클래스에 대해 정밀도-재현율 곡선 아래의 면적(AP)을 계산하고 이를 각 클래스에 대해 평균화한다.
2. **모든 클래스에 대한 mAP를 계산하기:** 각 클래스의 AP를 다시 평균하여 전체 클래스에 대한 mAP를 얻는다.


### YOLO v1
* YOLO v1은 입력 이미지를 `7*7` 그리드로 나누고 각 그리드의 셀이 하나의 object에 대한 detection을 수행한다.
* Anchor Box가 없다.

### YOLO v2 (YOLO9000)
* Anchor Box 도입
* Anchor Box의 개수는 5개
* V2에서는 각 그리드 셀에서 예측된 경계 상자의 크기와 모양을 미리 정의된 여러 Anchor Box로부터 학습한다.
* 그리드가 v1에 비해 `13*13`로 바꼈다.


### YOLO v3
* YOLOv3의 기본 설정 중 하나는 416x416 픽셀의 이미지를 입력으로 사용한다
![](https://i.imgur.com/oJicvoR.png)

