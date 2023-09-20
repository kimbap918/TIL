## SeSAC - 파이썬 데이터 분석 프로젝트 3일차

2023.08.10

<br>

## [PyCon KR 2018] 땀내를 줄이는 Data와 Feature 다루기

<br>

plotnine

[A Grammar of Graphics for Python — plotnine 0.12.2 documentation](https://plotnine.readthedocs.io/en/stable/#)

sklearn

[scikit-learn: machine learning in Python — scikit-learn 1.3.0 documentation](https://scikit-learn.org/stable/)

<br>

### data & Feature

데이터는 대부분 우리에게 원하는 형태로 되어있지 않다.

Data : 우리에게 주어진 날것의 무언가

Feature : 신호와 소음

<br>

### Missing Data 다루기

결측치는 왜 생길까

- 수집이 안됨(무응답, 서버오류)
- 해당 로그 수집을 특정 시기 이후에 시작해서 이전 데이터가 없음
- 특정 상황에서는 필요없어 일부러 남기지 않음
- Human error

<br>


Missingno : 결측치의 시각화

[[Visualization]  - missingno 라이브러리 사용법](https://chunggaeguri.tistory.com/entry/Visualization-missingno-라이브러리-사용법)

<br>


결측치의 종류

1. MCAR : 완전 무작위 결측
2. MAR : 임의적 결측 발생
3. NI : 무시할 수 없는 결측 발생

결측의 종류에 따라 처리해야할 방법이 다르다.

<br>


결측치의 처리 방법

1. 완전제거법(List-wise deletion)
- 가장 보편적
- 결측율이 높을 때 정보의 손실
- 각 변수의 분산을 증가시킨다

2. 단일대체방법(Single Imputation)
- 다양성을 반영하지 못함
- 관측된 자료에 의존하는 문제
- 구간을 나누어 구간별 평균/중앙값/최빈값을 구해서 대체

3. 다중대체방법(Multiple Imputation)
- 결측이 완전 무작위로 발생한다는 가정
- 대체가 가능한 값들의 분포로 부터 추출된 값으로 대체한 완전한 데이터세트를 만들어 대체
  
<br>

### 제거하기(Drop)와 대체하기(Imputation)

결측치 제거하기

- 데체하기 어렵거나 결측비율이 높은 데이터에 사용
- 데체할 필요가 없는 데이터에 사용

```python
df.dropna()
df.dropna(how = 'all')
df.dropna(axis=1, how='all')
df.dropna(thresh=x)
```

결측치 대체하기

scikit-learn Imputer : 평균값, 중앙값, 최빈값으로 결측치를 채워줌

[Scikit-learn Imputer 사용하기: 궁극적인 안내서 – Kanaries](https://docs.kanaries.net/ko/tutorials/Python/how-to-use-scikit-learn-imputer)

predictive_imputer

[predictive_imputer](https://pypi.org/project/predictive_imputer/)

BOW(Bag Of Word), n-gram, TF-IDF

[](https://hleecaster.com/nlp-bag-of-words-concept/)

### Error Data

- 잘못된 위경도 정보가 입력되어 범위를 벗어난 사례
- 같은 데이터에 들어 있는 주소 정보로 위경도를 보정
- 오류 데이터의 경우 참고 할 수 있는 다른 데이터가 있다면 보정
- 예를 들어 급여 정보가 없을 때 보험료를 참고해서 급여를 예측

### Outlier Data

- Error Data와는 다름
- 데이터 혹은 샘플에서 동떨어진 값, 모델에 편향을 줄 수 있다.
- 정상치와 이상치의 기준을 어느 지점으로 할 것인지에 대한 모호함
- 도메인마다 이상치의 기준에 대한 정도가 다르다
- 예를 들어 의료 데이터는 이상치가 중요할 수도 있음
- 국민청원 데이터로 투표수를 예측한다고 할 때 특정 사회적 이슈에 따라 이상치가 발생
- 이상치는 보정, 제거, 대체, 스케일 줄이기 등을 통해 해결

### Feature Selection

- *Feature Selection (특성 선택) 이란 가지고 있는 특성 중에서 훈련에 가장 유용한 특성을 선택하는 것을 말한다*

[[머신러닝] Basic Knowledge of Feature Selection](https://m.blog.naver.com/euleekwon/221464171572)


pandas를 통한 Feature Selection

![](https://i.imgur.com/vvduGIB.png)

<br>

Scikit-learn을 통한 Feature Selection

- 원본 데이터에서 불필요한 Feature 제거
- 필요한 Feature만 선택

```python
# 필요한 모듈에서 VarianceThreshold 클래스를 가져옴
from selearn.feature_selection import VarianceThreshold

# 입력 데이터 X를 정의, 6개의 샘플과 각 샘플은 3개의 이진(binary) 특성을 가진다
X = [[0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 1, 1]]

# VarianceThreshold 객체를 생성. 분산의 최소 임계값은 0.8 * (1 - 0.8)로 설정
# 이 임계값보다 분산이 작은 특성은 제거됨.
sel = VarianceThreshold(threshold=(.8 * (1 - .8)))

# VarianceThreshold 객체를 사용하여 X를 변환
# 분산이 설정한 임계값보다 작은 특성들은 제거된다
transformed_X = sel.fit_transform(X)

# 변환된 데이터를 출력
print(transformed_X)

->
array([[0, 1],
       [1, 0],
       [0, 0],
       [1, 1],
       [1, 0],
       [1, 1]])
```

<br>

### Feature Transform
Univariate transform
* 일변량 비선형 변환
* 대부분의 모델은 각 특성이 정규분포와 비슷할 때좋은 성능
* 오차가 정규분포를 따른다는 가정 하에 정규분포로 만들어 주는 과정이 필요해서 로그변환
* 로그함수의 값을 복원할때는 지수함수를 사용 np.exp(log_feature)
* 정수형 특성에 주로 사용
* 정수 Label Data에도 적용해 볼 수 있다
![](https://i.imgur.com/D2NybZC.png)

<br>

### Feature Scaling
https://bkshin.tistory.com/entry/%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D-8-Feature-Scaling-Feature-Selection
* 어느 한 변수가 분산이 너무 클 때 사용
* 각 변수의 분포를 일정하게 유지하도록
* 회귀분석에서는 스케일링을 적용하든 안 하든 변수의 유의성은 달라지지 않는다

MinMax Scaling
* 어느 한 변수가 분산이 너무 클때 
* 평균을 0 분산을 1로 만들어줌
``` python
from sklearn.preprocessing import MinMaxScaler

data = [[-1, 2], [-0.5, 6], [0, 10], [1, 18]]
scaler = MinMaxScaler()
print(scaler.fit(data))
print('Max : {}'.format(scaler.data_max_))
print(scaler.transform(data))
```
![](https://i.imgur.com/YYmotBP.png)

<br>

PCA
* PCA를 활용한 Feature Scaling의 예
``` python
import numpy as np
from sklearn.decomposition import PCA

# 입력 데이터 X를 정의 6개의 샘플과 각 샘플은 2개의 특성을 가진다
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])

# PCA 객체를 생성 주성분의 개수를 2로 설정
pca = PCA(n_components=2)

# PCA 객체를 사용하여 주성분 분석을 수행
pca.fit(X)

# 설명된 분산의 비율을 출력
print(pca.explained_variance_ratio_)
# [0.99244289 0.00755711]

# 특잇값을 출력
print(pca.singular_values_)
# [6.30061232 0.54980396]

```
