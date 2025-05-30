
<br>

## FastText
* Word2Vec의 개량 알고리즘으로 Subword를 고려한 알고리즘
* Word2Vec은 하나의 단어에 고유한 벡터를 할당하므로 단어의 형태학적 특징을 반영할 수 없다.

예를 들어 훈련데이터에서 eat은 많이 등장해서 학습이 충분히 잘 되었지만 eating은 잘 등장하지 않아서 제대로 된 임베딩 값을 얻지 못한다고 해보자.

![](https://i.imgur.com/q0Yu02H.png)

분명히 둘 다 공통적인 내부 단어를 갖고 있는데, 이를 활용할 수는 없을까?

<br>

### Word2Vec의 대표적인 문제점 두 가지
1. OOV(Out-of-Vocabulary) 문제

	Word2Vec의 Vocabulary에 "tensor"와 "flow"가 있더라도 "tensorflow"라는 단어가 Vocabulary에 없다면 "tensorflow"의 벡터값을 얻을 수 없다.

<br>

2. 형태학적 특징을 반영할 수 없다.

	eat, eats, eaten, eater, eating과 같은 단어들은 eat이라는 동일한 어근을 가진다.
	하지만 Word2vec에서는 각 단어는 각 벡터의 값을 가질뿐이다.


<br>

#### FastText
* FastText는 단어를 Character 단위의 n-gram으로 간주한다.
* n을 몇으로 하느냐에 따라서 단어가 얼마나 분리되는지가 결정된다.

단어 'eating'을 예로 들어보자.

1. 단어 eating에 시작과 끝을 의미하는 `<`, `>`를 추가한다.

	eating -> `<eating>` 

<br>

2. n-gram을 기반으로 단어를 분리한다. Ex) n=3

	` 3-grams <ea eat ati tin ing ng>`

<br>

3. 주로 n은 범위로 설정해준다. Ex) n: 3~6
![](https://i.imgur.com/kaaOdRc.png)

<br>

4. 훈련 데이터를 N-gram의 셋으로 구성했다면 훈련 자체는 SGNS와 동일하다. 단, Word가 아니라 subwords들이 최종 학습 목표이며 이들의 합을 Word의 vector로 간주한다. 즉, 단어 eating은 아래와 같이 n-gram들의 합으로 나타낸다.
![](https://i.imgur.com/suhhOXG.png)

<br>

5. FastText의 훈련 과정을 이해해보자. 여기서는 SGNS를 사용한다. 우리의 목표는 중심 단어 eating과 주변 단어 am과 food로 부터 SGNS를 학습하는 것이다.
![](https://i.imgur.com/1vbhlPJ.png)

<br>

6. 중심 단어 eating을 기준으로 주변 단어 am과 food로 데이터셋을 구축한다.
![](https://i.imgur.com/9k6x8UW.png)

<br>

7. Negative Sampling이므로 실제 주변 단어가 아닌 단어들도 필요하다.
![](https://i.imgur.com/pbjimFo.png)

<br>

8. SGNS 자체는 동일하다. 

	eating과 am 그리고 food의 내적값에 시그모이드 함수를 지난 값은 10이 되도록 학습. 
	
	eating과 paris 그리고 eating과 earth의 내적값에 시그모이드 함수를 지난 값은 0이 되도록 학습
![](https://i.imgur.com/Vv6VkKx.png)

<br>

단어 Orange에 대해서 FastText를 학습했다고 해보자. n의 범위는 2~5로 한다.

![](https://i.imgur.com/15MW6lI.png)

<br>

그 후 Oranges라는 OOV 또는 희귀 단어가 등장했다고 해보자. Orange의 n-gram 벡터들을 이용하여 Oranges의 벡터값을 얻는다.

![](https://i.imgur.com/wN4QNqb.png)

Q. 단어에 `<,>`를 왜 할까?

단어 양끝에 `<,>`를 해주지 않으면 실제로 독립적인 단어와 특정 단어의 n-gram인 경
우를 구분하기 어렵다. 예를 들어 where의 n-gram 중 하나인 her도 존재하지만 독립적인 단어 her 또한 Vocabulary에 존재할 수 있기 때문이다.

이 때, 독립적인 단어 her는 `<her>`가 됨으로써 where 내의 her와 구분할 수 있다.

<br>

#### 한국어에서의 FastText
한국어는 다양한 용언 형태를 가진다. Word2Vec의 경우 다양한 용언 표현들이 서로 독립된 단어로 표현된다.

예) 동사 원형이 '모르다' 인 경우
> 모르네, 모르더라, 몰라야, 몰랐다, 모르겠으나, 몰라, 모르겠니, 모르면서 등

한국어의 경우에는 이를 대응하기 위해 FastText의 n-gram 단위를 자모 단위로 하기도 한다.

예) ㅁㅗㄹ


## GloVe(Global Vectors for Word Representation)
* 자연어 처리에서 사용되는 워드 임베딩 (word embedding) 알고리즘 중 하나.
* GloVe는 단어의 분산 표현을 학습하기 위해 통계적 정보를 기반으로 하는 방법
* Document Term Matrix와 마찬가지로 고차원을 가지는 행렬 표현 방법.
* Window 크기에 따라서 행렬의 값이 결정된다는 특징을 가지고 있다.

![](https://i.imgur.com/ex1ifED.png)

다음의 3개의 예시 문장에 대해서 윈도우 크기가 1일 때를 보여준다.
* 일반적으로는 윈도우 크기는 5-10이다.
* 동시 등장 행렬은 기본적으로 대칭 행렬이다.

<br>

![](https://i.imgur.com/9p8nNXQ.png)
![](https://i.imgur.com/rAkXFjW.png)

GloVe의 특징

1. **윈도우 기반의 동시 등장 행렬 생성**: GloVe는 학습 데이터(코퍼스)를 기반으로 윈도우 기반의 동시 등장 행렬을 생성한다. 이 행렬은 단어 간의 동시 등장 빈도를 나타내며, 각 행과 열은 단어를 나타낸다. 행렬의 각 원소는 해당 단어 쌍의 동시 등장 횟수를 나타낸다.
    
2. **동시 등장 확률 정의**: 이 동시 등장 행렬을 사용하여 GloVe는 단어 쌍 간의 동시 등장 확률을 정의한다. 이 확률은 두 단어가 함께 나타나는 빈도와 관련이 있으며, GloVe는 이 확률을 최적화하는 방향으로 모델을 학습한다.
    
3. **Dense한 Vector 학습**: GloVe는 단어의 분산 표현인 밀집(dense) 벡터를 학습한다. 이 벡터는 단어의 의미를 포함하며, 단어 간의 의미적 유사성과 관계를 캡처한다.
    
4. **목적 함수 최적화**: GloVe의 목적 함수는 동시 등장 확률과 벡터 임베딩 간의 관계를 최적화하려는 것이다. 이 목적 함수는 모델이 학습 데이터의 통계 정보를 가장 잘 모사하도록 한다.

GloVe는 Word2Vec과 달리 특별한 손실 함수를 사용하여 행렬 분해 방법을 활용하는데, 
Word2Vec이 전체 통계 정보를 충분히 활용하지 못하는 문제를 개선하는 중요한 특징 중 하나이다.

<br>

### Word Embedding의 한계
1. 동형어, 다의어에 대해서는 제대로 훈련되지 않는다.
2. 단순히 주변 단어만을 고려하므로 문맥을 고려한 의미를 담고있지는 않다.

