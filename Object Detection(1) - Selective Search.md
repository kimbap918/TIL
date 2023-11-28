## General object detection framework
* Region proposal
	* 먼저, 이미지 내에 물체가 있을 것으로 예상되는 위치를 제안한다. 이 단계에서는 후보 영역을 찾는 데 중점을 두고 있다.
	* 주로 사용되는 알고리즘으로는 Selective Search, EdgeBoxes, R-CNN 계열의 네트워크가 있다.
* Feature extraction and network prediction
	* 이미지 내의 각 제안된 영역에서 특징을 추출하고, 신경망을 사용하여 해당 영역이 어떤 물체인지 예측한다.
	* 주로 사용되는 딥러닝 구조로는 CNN(Convolutional Neural Network)을 사용한 Faster R-CNN, SSD(Single Shot Multibox Detector), YOLO(You Only Look Once) 등이 있다.
* Non-maximum suppression(NMS)
	* 여러 개의 겹치는 박스들 중 가장 적합한 물체를 선택하기 위해 사용된다.
	* 이 기술은 중복된 탐지를 제거하고 가장 정확한 결과를 얻기 위해 필요하다.
	* 바운딩 박스가 겹쳐지는 영역의 유사도를 계산하고 유사하면 합하고, 유사하지 않으면 합하지 않는다.
	* 이 작업은 겹치는 바운딩 박스가 없어질 때 까지 한다.
	* **confidence**
* Evaluation metrics
	* 모델의 성능을 측정하기 위한 지표들로, 주로 IoU(Intersection over Union), Precision, Recall, F1-score 등을 사용한다.
	* 이러한 지표들을 통해 모델이 얼마나 정확하게 물체를 탐지하는지 평가할 수 있다.

## Selective Search
Selective Search는 사람, 물건 등을 구분하는것이 아닌 bounding box 내에 객체가 있을 가능성이 있다.' 정도만 찾는다.
* two page
* single shot detection

![](https://i.imgur.com/4tYVuvK.png)

1. image segmentation을 실시해서 이를 기반으로 후보 영역을 찾기 위한 seed설정
2. 적절히 통합 해나감


Selective Search는 객체 탐지(Object Detection)를 위한 물체 제안(Region Proposal) 방법 중 하나. 이 방법은 이미지 내에서 물체가 존재할 가능성이 높은 후보 영역(region)을 찾는 데 사용된다.

Selective Search는 다음과 같은 주요 단계로 구성된다:

1. **다양한 스케일 및 텍스처로 이미지 분할**:
    * 입력 이미지를 다양한 스케일과 텍스처로 분할하여 유사한 픽셀 그룹을 형성.

2. **유사한 영역 병합**:
    * 유사도를 기반으로 이미지 내의 영역을 병합하여 큰 영역을 생성한다. 색상, 텍스처, 크기 등의 특징을 고려하여 유사한 영역을 결합합.

3. **영역 병합 후보 생성**:
    * 병합된 영역들을 이용하여 객체 후보 영역을 생성한다. 이 후보 영역은 물체가 있을 것으로 예상되는 영역을 표시하는 데 사용된다.

Selective Search는 이미지 내에 다양한 크기와 모양의 물체가 있을 때, 후보 영역을 제안하여 물체 탐지 모델이 이러한 영역을 분석하고 실제 물체를 인식할 수 있도록 한다. 

이 방법은 R-CNN 계열의 객체 탐지 모델에서 region proposal을 생성하는 데 사용되었으며, 객체 탐지에서 높은 성능을 보이는 방법 중 하나이다.

<br>

### Non-maximum suppression(NMS)
NMS(Non-Maximum Suppression)는 객체 탐지(Object Detection)에서 사용되는 기법 중 하나로, 겹치는 bounding box들을 제거하여 최종 객체를 선택하는 과정에서 confidence(신뢰도) 값을 활용한다.

confidence는 각각의 bounding box가 해당 클래스에 속할 확률을 나타내는 지표다. 일반적으로 객체 탐지 모델은 각 bounding box에 대해 클래스에 속할 확률(confidence score)을 예측하는데, 이 confidence score는 해당 물체가 존재할 확률로 해석될 수 있다.

NMS는 이러한 confidence score를 활용하여 겹치는 bounding box 중에서 물체를 더 잘 표현하는 bounding box를 선택하는 기술이다. 이때 confidence score가 높은 bounding box를 선호하고, 겹치는 bounding box 중에서 높은 confidence score를 가진 bounding box를 선택하고 나머지를 제거하여 최종적으로 중복된 bounding box를 제거한다.

NMS는 일반적으로 다음과 같은 단계로 수행된다.

1. 모든 bounding box를 confidence score에 따라 내림차순으로 정렬한다.
2. 가장 높은 confidence score를 가진 bounding box를 선택하고, 이와 겹치는 다른 bounding box들과 IoU(Intersection over Union)를 계산한다.
3. IoU가 특정 임계값을 넘는(예를 들어, 0.5 이상) bounding box들을 제거한다.
4. 제거한 bounding box를 제외한 나머지 bounding box에 대해 위 과정을 반복한다.

이를 통해 객체 탐지 모델이 겹치는 bounding box들 중 가장 신뢰도가 높은 것을 선택하고, 중복된 예측을 제거하여 정확도를 높이는 데 기여한다.


### IoU의 계산법
![](https://i.imgur.com/RIpUxoa.png)


<br>

## Training R-CNNs(Region-based Convolutional Neural Network)
객체 탐지(Object Detection)를 위한 딥러닝 모델
![](https://i.imgur.com/DaDZhZE.png)


1. **Region Proposal**:
    - R-CNN은 먼저 이미지에서 물체가 있을 것으로 예상되는 후보 영역을 제안하는 과정을 거친다. 이를 위해 Selective Search 등의 알고리즘을 사용하여 후보 영역을 생성한다.

2. **특성 추출(Feature Extraction)**:
    - 후보 영역들을 추출한 후, 각각의 영역을 독립적으로 CNN(Convolutional Neural Network)에 통과시켜 특성을 추출한다. 이는 이미지에서 물체를 식별하기 위한 중요한 단계다.

3. **Region-based CNN**:
    - 추출된 특성을 사용하여 각각의 후보 영역에 대해 분류 작업을 수행한다. 이를 위해 SVM(Support Vector Machine)과 같은 분류기를 사용하거나, FCN(Fully Convolutional Network)을 사용하여 분류한다.

4. **BBox Regression**:
    - 물체의 정확한 경계 상자(bounding box) 위치를 조정하기 위한 회귀(regression) 단계가 있다. 이 단계에서는 경계 상자의 위치와 크기를 조정하여 더 정확한 객체의 위치를 찾는다.

## FAST R-CNNs
Object detection이 느린 R-CNN의 개선된 버전, R-CNN의 속도와 정확도를 향상시키기 위한 몇 가지 개선을 도입
![](https://i.imgur.com/AQvAt4G.png)
1. **엔드-투-엔드 학습(End-to-End Training)**
    - R-CNN과는 달리, Fast R-CNN은 특성 추출 과정에서 여러 번의 CNN(Convolutional Neural Network) 연산을 수행하지 않고 한 번의 CNN 연산을 통해 특성 맵을 얻는다. 이는 모델의 엔드-투-엔드(end-to-end) 학습을 가능하게 한다.

2. **RoI Pooling**:
    - Region of Interest (RoI) Pooling을 도입하여, 후보 영역(region proposals)에 대해 특성 맵의 부분을 추출하고 고정된 크기의 특성 벡터로 변환한다. 이로써 CNN의 출력을 사용하여 객체를 분류하고 경계 상자(bounding box)를 조정할 수 있다.

3. **한 번의 특성 추출**:
    - Fast R-CNN은 이미지에 대해 한 번의 CNN 특성 추출을 수행하므로, R-CNN보다 훨씬 빠르게 작동한다.

4. **분류와 회귀를 동시에 수행**:
    - RoI Pooling을 통해 한 번의 특성 추출을 하고, 추출된 특성을 분류와 회귀 작업에 동시에 사용하여 물체의 존재 여부를 분류하고, 경계 상자의 위치를 조정한다.

Fast R-CNN은 R-CNN에 비해 속도와 정확도 면에서 개선됐으나, 여전히 후보 영역을 제안하는 과정이 느릴 수 있어, 이를 개선하기 위해 후속 모델들인 Faster R-CNN, Mask R-CNN 등이 등장하며 속도와 정확도를 더욱 개선되고 있다.

<br>

### Single-shot detector(SSD)
SSD는 Selective Search와 같은 전통적인 Region Proposal Network(RPN)을 사용하지 않는다. SSD는 객체 탐지를 위한 네트워크 아키텍처로서, 미리 정의된 여러 크기와 종횡비를 가진 Default Box를 사용하여 객체의 위치를 예측한다.

<br>

YOLO(You Only Look Once) 모델은 객체 탐지(Object Detection)를 위해 bounding box의 정보를 예측할 때 중심 좌표(center coordinates)와 상자의 가로 길이(width)와 세로 길이(height)를 제공한다.
각 그리드 셀에 대해 YOLO는 다음을 예측한다.

1. 그리드 셀 내의 물체가 존재할 확률(probability of object presence)
2. bounding box의 중심 좌표 (x, y)
3. bounding box의 가로 길이(width)
4. bounding box의 세로 길이(height)
5. 각 클래스에 대한 신뢰도(확률)


