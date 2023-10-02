
<br>

## 텍스트의 벡터화

### Vocabulary의 생성
기계가 알고 있는 단어들의 집합을 단어 집합(Vocabulary)라고 한다.

단어 집합이란 훈련 데이터에 있는 단어들의 중복을 제거한 집합을 의미한다.

![](https://i.imgur.com/qTGs80s.png)

<br>

입력된 모든 텍스트를 정수 시퀀스로 변환하기 위해 단어 집합에 있는 각 단어에는 고유한 정수가 부여된다.

![](https://i.imgur.com/kAk15LJ.png)
![](https://i.imgur.com/OpFS1GU.png)

<br>
### OOV 문제(Out Of Vocabulary Problem)
* 단어 집합에 없는 단어로 인해 생기는 문제
* 이렇게 생긴 단어들을 일괄적으로 하나의 토큰으로 매핑해준다.

![](https://i.imgur.com/IfhRcE9.png)


![](https://i.imgur.com/08IzhqU.png)

<br>
### 벡터화(Vectorization)
1. 벡터화에 신경망을 사용하지 않을 경우
* 단어에 대한 벡터 표현 방법 : one-hot encoding
* 문서에 대한 벡터 표현 방법 : Document Term Matrix, TF-IDF

<br>

2. 벡터화에 신경망을 사용할 경우(2008~2018)
* 단어에 대한 벡터 표현 방법 : 워드 임베딩(Word2Vec, GloVe, FastText, Embedding layer)
* 문서에 대한 벡터 표현 방법 : Doc2Vec, Sent2Vec

<br>

3. 문맥을 고려한 벡터 표현 방법 : ELMO, BERT, GPT, T5 등 (2018~현재)
* Pre-trained Language Model의 시대
* 문서에 대한 벡터 표현 방법 : ELMo, SBERT, BERT의 CLS토큰

<br>

### 벡터화에 신경망을 사용하지 않을 경우
#### 원-핫 인코딩
* 원-핫 인코딩은 전체 단어 집합의 크기를 벡터의 차원으로 가진다.
* 각 단어에 고유한 정수 인덱스를 부여한 후 해당 인덱스의 원소는 1로, 나머지 원소는 0을 가지는 벡터로 변환한다.

![](https://i.imgur.com/GwAto0N.png)
![](https://i.imgur.com/EKxQZZs.png)

<br>

#### 워드 임베딩
* 인공 신경망을 이용하여 단어의 벡터값을 얻는 방법
* 학습 후에는 각 단어 벡터 간의 유사도(의미를 반영)를 계산할 수 있다.
![](https://i.imgur.com/O50A3IG.png)

<br>

#### Document Term Matrix
* DTM은 마찬가지로 벡터가 단어 집합의 크기를 가지며, 대부분의 원소가 0을 가진다
* 각 단어는 고유한 정수 인덱스를 가지며, 해당 단어의 등장 횟수를 해당 인덱스의 값으로 가진다.

![](https://i.imgur.com/6idcr0h.png)

<br>

#### Bag of Words
* 단어들의 가방
* 가방에 문장들의 단어들을 넣고 흔든다면, 단어의 순서는 무의미해진다.
* 단어의 순서는 무시하고 오직 단어의 빈도수에만 집중하는 방법

![](https://i.imgur.com/qtm02BA.png)

<br>

#### TF-IDF(Term Frequency-Inverse Document Frequency)
* 단어 빈도-역 문서 빈도
* DTM(Document Term Matrix)에서 추가적으로 중요한 단어에 가중치를 주는 방식
* TF와 IDF라는 두 값을 곱한 결과다.
* TF-IDF 기준으로 중요한 단어는 값이 Up
* TF-IDF 기준으로 중요하지 않은 값이 Down
* 문서의 유사도, 검색 시스템에서 검색 결과의 순위 등을 구하는 일에 쓰인다.
* 벡터이므로 인공 신경망의 입력으로도 사용 가능하다

TF(d,t) : 특정 문서에서 d에서의 특정 단어 t의 등장 횟수
DF(t) : 특정 단어 t가 등장한 문서의 수
IDF(d, t) : df(t)에 반비례하는 수

![](https://i.imgur.com/QaHRH7N.png)

<br>

**IDF는 DF에 반비례하도록 설계한 후, log를 씌운다.**
$IDF(d,t) = log(\frac{n}{1+DF(t)})$

-> 로그를 사용하지 않으면 IDF의 값이 기하급수적으로 커질 수 있다.

![](https://i.imgur.com/x7KiH20.png)

<br>

* TF-IDF는 모든 문서에서 자주 등장하는 단어는 중요도가 낮다고 판단하며, 특정 문서에서만 자주 등장하는 단어는 중요도가 높다고 판단한다.

* 비교적 자주 쓰이지 않는 단어들조차 희귀 단어들과 비교하면 최소 수백 배는 더 자주 등장한다.
이 때문에 log를 씌워주지 않으면 희귀 단어들에 엄청난 가중치가 부여될 수 있다.

* log를 씌우면 이런 격차를 줄이는 효과가 있다.

![](https://i.imgur.com/eCrognm.png)
![](https://i.imgur.com/3Zy88zZ.png)

<br>

### 벡터화에 신경망을 사용할 경우(2008~2018)
#### Embedding Layer
* 딥러닝 자연어 처리를 하게 될 경우 거의 항상 하게 되는 작업
* 단어 -> 정수 인코딩 -> Embedding Table -> 임베딩 벡터
* 거의 모든 딥러닝 자연어 처리에서 단어를 정수로 바꿔주는 이유가 여기에 있다.
* 신경망 기반의 벡터화이기 때문에 기본적으로 벡터의 값이 학습에 의해 결정된다.


![](https://i.imgur.com/JU92ORd.png)

<br>

* one-hot encoding으로 표현된 단어들은 단어의 의미를 반영한 유사도를 구할 수 없다.
* 워드 임베딩을 사용하면 '선생님' 벡터가 '전화기' 벡터보다 '교사'라는 벡터와 가깝다는 것을 알 수 있다.

![](https://i.imgur.com/cOj0JCC.png)

<br>

#### 워드 임베딩
워드 임베딩은 크게 두 가지로 구분된다.

1. 랜덤 초기화 임베딩
* NNLM(Neural Network Language Model)과 마찬가지로 랜덤값을 가지고 오차를 구하는 과정에서 embedding table을 학습
* NNLM은 이전 단어가 주어졌을 때 다음 단어를 예측하는 학습 과정에서 오차를 줄이면서 학습되었다. 그러나 이와 같은 워드 임베딩 기법은 텍스트 분류, 개체명 인식 등 다양한 NLP태스크에서도 오차를 줄이며 학습할 수 있다.

<br>

2. 사전 훈련된 임베딩(Pre-trained Word Embedding)
* 정해진 특정 알고리즘에 방대한 데이터를 입력으로 학습시킨 후 여러 Task의 입력으로 사용
* 대표적인 알고리즘으로 Word2Vec, FastText, GloVe가 존재한다.

![](https://i.imgur.com/xyCxbzN.png)

<br>
#### Word2Vec
* 단어의 의미를 반영한 임베딩 벡터를 만드는 대표적인 방법
* 벡터가 된 단어들은 이제 '벡터'이므로 서로 연산 또한 가능하다

![](https://i.imgur.com/E9PqiSB.png)

<br>

Word2Vec은 임베딩 그 자체에만 집중하는 모델이다.
![](https://i.imgur.com/kBg6dFP.png)

<br>

* 윈도우 크기가 2일때, Skip-gram은 다음과 같이 데이터셋을 구성한다. 
* Skip-gram은 중심 단어로부터 주변 단어를 예측한다.
* Skip-gram은 모든 존재하는 단어 중 하나의 단어를 예측하는 소프트맥스 문제와 동일하다. 단어 집합의 크기 만큼의 카테고리 중에 1개를 분류해야 한다.
![](https://i.imgur.com/uMnJUEg.png)
![](https://i.imgur.com/9kZqrSp.png)

<br>

실제로는 속도가 너무 느리기 때문에 위와 같이 구현하지는 않는다.

일반적으로 단어 집합의 크기는 수 만 이상이다.

<br>

#### CBOW
* Skip-gram은 중심 단어로부터 주변 단어를 예측하는 모델
* CBOW (Continuous Bag of Words)는 자연어 처리와 워드 임베딩을 위한 모델 중 하나로, 특정 단어를 예측하기 위해 주변 맥락 단어들을 활용하는 모델이다.

![](https://i.imgur.com/d7sGjqk.png)

<br>

#### SGNS(Skip-Gram with Negative Sampling)
* Word2Vec과 같은 워드 임베딩 알고리즘 중 하나
* 주변 단어와 대상 단어 간의 관계를 학습하여 단어를 벡터로 표현
* 예를 들면 "king"이라는 단어 주변에는 "queen", "royal", "throne"같은 단어들이 자주 나타나며, SGNG는 이런 관계를 학습해 "king"의 벡터 표현을 학습한다.

![](https://i.imgur.com/xUgyjC0.png)
![](https://i.imgur.com/MlhfLtv.png)

이 모델의 목적은 중심 단어와 주변 단어를 입력으로 하였을 때, 실제로 이 두 단어의 관계가 이웃의 관계인지를 예측하는 것이다.

주변 단어와 중심 단어 데이터셋에 True를 의미하는 레이블 1을 할당해주고 거짓을 의미하는 샘플도 추가해준다. 이것을 Negative Sample이라고 한다. Negative Sample은 전체 데이터셋에서 랜덤으로 추가해준다.

![](https://i.imgur.com/Awrrqcu.png)


두 개의 Embedding table을 준비한다. 한 테이블은 중심 단어, 한 테이블은 주변 단어를 위한 테이블이다.

![](https://i.imgur.com/hHKtCY2.png)
![](https://i.imgur.com/8uHugMw.png)

<br>
중심 단어와 주변 단어의 내적으로부터 실제값인 1 또는 0을 예측하고 실제값과의 오차를 계산해서 역전파를 통해 두 개의 테이블을 업데이트한다.

![](https://i.imgur.com/75S5V9F.png)

* Embedding vector의 차원을 정하는 것은 사용자의 몫이다.
* CBOW보다는 SGS(Skipgram with Negative Sampling)이 가장 많이 선호된다.
* 작은 윈도우 크기 (2~ 7)을 가질수록, 상호 교환 가능한 단어들이 높은 유사도를 가진다.
* 여기서 상호 교환이 가능하다는 것은 어쩌면 반의어도 포함될 수 있다. Ex) 친절한 <> 불친절한
* 반면, 커다란 윈도우 크기 (7~ 25)는 관련 있는 단어들을 군집하는 효과를 가진다.

![](https://i.imgur.com/VVsz4gy.png)

<br>

* 데이터셋을 위한 Negative Sampling의 비율 또한 성능에 영향을 주는 또 다른 결정요소이다.
* 논문에서는 5-20을 최적의 숫자로 정의하고 있다.
* 데이터가 방대하다면 2-5로 충분하다.

![](https://i.imgur.com/uVZPD92.png)
