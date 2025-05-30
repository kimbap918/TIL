
<br>

### (참고)자연어 처리의 학습 순서

1. Tokenization (토큰화) & Stemming (어간 추출) 
2. BOW (Bag of Words), TF-IDF (Term Frequency-Inverse Document Frequency)
3. Basic models
4. Word embeddings (단어 임베딩)
5. LSTM (Long Short-Term Memory), GRU (Gated Recurrent Unit), Attention models
6. Transformers `(2017)"Attention Is All You Need"`
7. BERT (Bidirectional Encoder Representations from Transformers) `(2018) "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding"`

<br>

## 자연어(Natural Language)

자연어란, 우리가 일상 생활에서 사용하는 언어.

자연어 처리(Natural Language Processing)란, 이러한 자연어의 의미를 분석하여 컴퓨터가 처리할 수 있도록 하는 일.

-> 음성인식, 요약, 번역, 텍스트 분류, 감성 분석, 챗봇 등

<br>

### 한국어의 자연어 처리

#### 한국어의 특징

1. 한국어의 자연어 처리는 영어보다 훨씬 어렵다. 한국어는 **교착어** 이기 때문이다.
* 교착어 : 단어 형태가 어간(Stem)에 접사(Affix)가 붙어 이루어진 언어
* 영어는 어순에 따라 단어의 문법적 기능이 정해지는 고립어다.

	예시 : "가다" (to go)의 어간은 "가"이며 여러 가지 접사를 추가함으로써 다양한 형태의 단어를 만들 수 있다. `"가요" (goes), "갑니다" (go), "가서" (and go)`

<br>

2. 한국어는 띄어쓰기가 잘 지켜지지 않는다.
* 한국어는 띄어쓰기가 어렵고, 지키지 않더라도 쉽게 읽을 수 있다.
* 대부분의 데이터에서 띄어쓰기가 잘 지켜지지 않는 경향이 있다.

<br>

3. 주어 생략은 물론 어순 또한 중요하지 않다.
* 같은 의미의 문장을 다음과 같이 쓸 수 있다.
1) 나는 운동을 했어. 체육관에서
2) 나는 체육관에서 운동을 했어
3) (나는) 체육관에서 운동했어
4) 나는 운동을 체육관에서 했어

이는 언어 모델이 자연어를 처리할 때 혼란을 주는 요소가 된다.

<br>


### 토큰화(Tokenization)
* 기계에게 어느 구간까지가 문장이고, 단어인지 알려주는 것
* 텍스트를 작은 단위로 나누는 과정이며, 이러한 작은 단위를 토큰(token)이라고 한다.
* 토큰의 단위는 `문장`, `단어`, `형태소`  등의 다양한 단위가 존재하며, 토큰의 단위가 단어 인 경우 단어 토큰화라고 한다.
* 텍스트를 모델이 이해하기 쉬운 형태로 분해하는 기초 단계로, 텍스트 처리 작업의 첫 번째 단계로 자주 수행한다.

	Hello, how are you?"라는 문장을 토큰화하면 ["Hello", ",", "how", "are", "you", "?"]와 같이 나눌수 있다.

<br>

#### 단어 토큰화에 대한 고민
의미가 동일한 아래 세 문장에 대해서 띄어쓰기 단위로 단어를 나눠보자.

We're Avengers!! -> ['We're', 'Avengers!!']

We are Avengers!! -> ['We', 'are', 'Avengers!!']

We are Avengers -> ['We', 'are', 'Avengers']

<br>

특수 문자가 토큰화에 방해가 된다고 해서 모든 특수 문자를 제거하는 규칙을 넣는다면?

$45.55 -> 45 55 -> ['45', '55']

Ph.D -> Ph D -> ['Ph', 'D']

IP 192.168.56.31  -> ['IP 192', '168', '56', '31']

위처럼 특수 문자 제거로 인해 본래 의미를 상실하는 경우가 발생할것이다. 토큰화 작업은 상당히 섬세하게 규칙을 설계해야 한다.

<br>

#### 토크나이저

영어의 토크나이저

1. TreebankWordTokenizer
* Penn Treebank Tokenization 규칙을 따르는 단어 토크나이저
* 하이픈(-)으로 구성된 단어는 하나로 유지
* doesn't같이 아포스트로피로 '접어'가 함께하는 단어는 분리

2. NLTK Tokenizer
* 문장의 토큰화에 사용하는 토크나이저 

<br>

한국어의 토크나이저

1. KSS
* https://github.com/hyunwoongko/kss

교착어인 한국어의 특성으로 인해 한국어는 토크나이저로 형태소 분석기를 사용하는 것이 보편적이다.

형태소 분석기는 다양하게 존재하므로 원하는 task에 맞는 형태소 분석기를 선택한다.

* Mecab : 연산속도가 빠르고 분석 성능도 준수하여 선호도가 높음. 
* Khali : 가장 최근에 나온 분석기로 딥러닝 기반 형태소 분석기.
* KOMORAN : 오탈자에 강건한 형태소 분석기. 
* Soynlp :  학습 기반으로 복합 명사를 잘 추출해낼 수 있음.
 
<br>

형태소 분석기 결과 비교
![](https://i.imgur.com/8yawjS2.png)

<br>

### 정수 인코딩(Integer Encoding)
* 단어 토큰화 또는 형태소 토큰화를 했다면 그 다음으로는 각 단어에 고유한 정수를 부여한다.
* 이 작업은 중복이 허용되지 않는 모든 단어들의 집합을 만든다.
* 이것을 단어 집합이라고 하며 이를 기반으로 문서를 정수로 인코딩한다.

![](https://i.imgur.com/bp19AAg.png)

<br>

### 패딩(Padding)
* 모든 문장에 대해서 정수 인코딩을 수행하였을 때 길이는 서로 다를 수 있다.
* 이 때에 가상의 단어를 추가하여 길이를 맞춰준다.
* 이 과정을 통해 기계가 병렬 연산을 할수 있다.

![](https://i.imgur.com/mfmUNxl.png)


