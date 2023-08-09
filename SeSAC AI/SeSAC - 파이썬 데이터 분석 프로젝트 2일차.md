## SeSAC - 파이썬 데이터 분석 프로젝트 2일차

2023.08.09

<br>

### 시작하기 전에

[Python for Data Analysis, 3E](https://wesmckinney.com/book/)

이 책은 2022년 3판으로 python 3.10을 기준으로 한다.

<br>

### 필수 파이썬 라이브러리

1. numpy : numerical python C언어로 구현된 파이썬 라이브러리, 고성능의 수치계산을 위해 제작 
2. pandas : 데이터 조작 및 분석을 위한 파이썬 프로그래밍 언어 용으로 작성된 소프트웨어 라이브러리
3. matplotlib : Python 프로그래밍 언어 및 수학적 확장 NumPy 라이브러리를 활용한 플로팅 라이브러리
4. statsmodels : 데이터를 탐색하고, 통계 모델을 추정하고, 통계 테스트를 수행할 수 있는 Python 패키지

<br>

### (참고) 리눅스 명령어

[리눅스 기본 명령어](https://www.mireene.com/webimg/linux_tip1.htm)

<br>

### python의 import convention 
* 파이썬 커뮤니티는 자주 사용하는 몇가지 모듈에 대해  다음의 네이밍 컨벤션을 사용한다.
``` python
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import statsmodels as sm
```


<br>

### 파이썬을 좀 더 공부하려면 참고하기 좋은 책
![](https://i.imgur.com/Ltvynea.png)

## Ipython과 Jupyter(책47p ~ 55p)

ipython 기초 가이드 참고하기
https://compmath.korea.ac.kr/appmath/PythonIPythonJupyterBasics.html#IPython-%EA%B8%B0%EC%B4%88

<br>

### 파이썬 기초
1. 들여쓰기
* 다른 많은 언어와 다르게 파이썬은 중괄호 대신 공백문자를 사용해 코드를 구조화한다. 통상적으로 4칸 들여쓰기(1 tab)을 사용한다.
2. 모든것은 객체
* 모든 숫자, 문자열, 자료구조, 함수, 클래스, 모듈 등은 파이썬 인터프리터에서 파이썬 객체라 부르는 어떤 상자 안에 저장된다.
3. 주석
* `#`뒤에 오는 글자는 모두 파이썬 인터프리터에서 무시된다. 이 특징을 이용해 주석을 달수 있다. 통상적으로 `#`뒤에 공백을 두번 넣어서 주석으로 사용한다.
``` python
#  나는 주석이에요
print("Hello world!")
```
4. 함수와 객체 메서드 호출
* 함수는 괄호와 0개 **이상**의 인수를 전달해 호출할수 있다.
``` python
result = f(x, y, z) #  인자가 3개인 함수
g() #  인자가 없는 함수
```
5. 변수와 인수 전달
* 변수에 값을 할당하는 것은 한 이름이 하나의 객체로 연결되므로 바인딩(binding)이라 한다.
``` python
a = [1, 2, 3]
b = a # a와 b는 같은 객체인 [1, 2, 3]리스트를 가리킨다.
print(b) #  [1, 2, 3]

a.append(4)
print(b) #  [1, 2, 3, 4]
```
6. 파이썬의 변수에는 고유한 타입이 없다.
* 변수는 할당을 통해 다른 타입의 객체를 참조할 수 있다.
``` python
a = 5
print(type(a)) #  int
a = "foo"
print(type(a)) #  str
```
7. 속성과 메서드
* 파이썬에서 객체는 객체 내부에 저장된 다른 파이썬 객체인 '속성'과 그 객체의 내부 데이터에 접근할 수 있는 함수인 '메서드'를 갖는다. 속성과 메서드는 **obj.attribute_name**문법으로 접근 가능하다.
``` python
In [1] : a = "foo"
In [2] : a.[Tab] # a.를 입력하고 tab을 누른다.
```
8. 덕 타이핑
https://nesoy.github.io/articles/2018-02/Duck-Typing
9. 파이썬의 연산자
https://dingrr.com/blog/post/python-103-%EC%97%B0%EC%82%B0%EC%9E%90%EC%9D%98-8%EA%B0%80%EC%A7%80-%EC%A2%85%EB%A5%98

### 파이썬의 자료형
스칼라 자료형
* 숫자 데이터, 문자열, 불리언(boolean), 날짜와 시간을 다룰 수 있는 몇몇 내장 자료형 등, 이런 단일 값을 담는 타입을 스칼라 자료형이라고 한다.
``` python
None
str
bytes
float
bool
int
```
1. 숫자 자료형
숫자를 위한 주요 자료형은 `int`, `float`다. int는 임의의 숫자를 저장할 수 있고 부동소수점 숫자는 float 자료형으로 나타낸다.
``` python
ival = 17239871 #  int
fval = 7.243 #  float
fval2 = 6.78e-5 #  float
```

2. 문자열
작은따옴표`'`, 큰따옴표`"`로 둘러싸서 문자열을 나타낼 수 있다. 일반적으로 큰 따옴표가 선호된다.
``` python
a = "a quick brown fox jumps over the lazy dog"
b = '0123456789'
```
(참고) f-string
https://blockdmask.tistory.com/429
(참고) 바이트와 유니코드
https://wikidocs.net/194282

3. 불리언
* 파이썬에서 불리언 값은 True, False다. 불리언 값을 숫자로 변환하면 False는 0, True는 1이다.

4. 형변환
``` python
s = "3.14159" #  str
fval = float(s) #  float 형변환
print(int(fval)) #  3, int
print(bool(fval)) # True, bool

```

5. None
* None은 파이썬에서 사용하는 null값이다.

6. 날짜와 시간
* 파이썬 내장 datetime모듈은 datetime, time, date 자료형을 지원한다. 
``` python
from datetime import datetime, date, time # 날짜와 시간, 날짜, 시간
dt = datetime(2011, 10, 29, 20, 30, 21)
dt.day #  29
dt.minute #  30
```

<br>

### 제어 흐름

1. if, elif, else
* if문은 조건을 검사해 True일 경우 if블록 내의 코드를 수행한다.
``` python
x = -5
if x < 5:
	print("It's negative")
```
* if는 부가적으로 하나 이상의 elif, 다른 모든 조건이 False일 경우 수행될 else블록을 갖는다
``` python
if x < 0:
	print("It's negative")
elif x == 0:
	print("Zero")
else:
	print("필기 멈춰")
```
2. for
* 리스트나 튜플 같은 컬렉션이나 이터레이터를 순회한다. for문의 기본 문법은 다음과 같다.
``` python
for value in collection:
	# 여기서 value변수를 사용할수 있다.

seq = [1, 2, 0, 4, 6, 5, 2, 1]
sum_until5 = 0
for val in seq:
	if val == 5:
		break # break예약어를 사용해 빠져나갈수 있다.
	sum_until5 += val
```
3. while
* 조건을 명시하고 해당 조건이 False가 되거나 break문을 사용해서 명시적으로 반복을 끝낼 때 까지 블록 내의 코드를 수행한다.
``` python
x = 256
total = 0
while x > 0:
	if total > 500:
		break
	total += x
	x = x // 2
```
4. pass
* 파이썬에서 아무것도 하지 않음을 나타낸다.
* 또는 아직 구현하지 않은 코드를 나중에 추가하기 위한 placeholder로도 사용한다.
``` python
if x < 0:
	print("It's negative")
elif x == 0:
	#  나중에 여기에 코드 추가해주세요
	pass
else:
	print("필기 멈춰")
```
5. range
* range 함수는 균일한 간격의 연속된 정수를 반환하는 이터레이터를 반환한다.
* range 함수는 임의의 큰 크기로 값을 생성해낼 수 있지만 메모리 사용량은 매우 적다.
``` python
range(10) # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

for i in range(10):
	# i = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
```

<br>

### 내장 자료구조, 함수, 파일

* 튜플, 리스트, 딕셔너리
1. 튜플(tuple)
* 튜플은 한 번 할당되면 변경할 수 없는(immutable) 고정 길이를 갖는 순차 자료형이다.
* 튜플은 소괄호`()`로 감싼다
``` python
tup = (4, 5, 6)
tup = 4, 5, 6 #  괄호를 생략할 수 있다.
tup = tuple('string') #  모든 순차 자료형이나 이터레이터는 tuple메서드를 통해 튜플로 변환할 수 있다.
tup[0] # 대괄호를 이용해 다른 순차 자료형처럼 접근할 수 있다. 
#  -> s
tup = (4, 5, 6) # 튜플에서 값을 분리할 수 있다.
a, b, c = tup

values = 1, 2, 3, 4, 5
a, b, *rest = values #  튜플의 시작 부분에서 값을 일부 끄집어내야 하는 상황에서 *를 사용해 값을 꺼낼수있다
#  -> 1, 2, [3, 4, 5]
```
2. 리스트(list)
* 튜플과는 달리 리스트는 크기나 내용을 변경할 수 있다. 
* 리스트는 대괄호 `[]`나 list 함수를 사용해서 생성한다.
``` python
a_list = [2, 3, 7, None]
tup = ("foo", "bar", "baz")
b_list = list(tup) #  list함수 사용
#  -> ['foo', 'bar', 'baz']
b_list[1] = "peekaboo" #  리스트는 변경이 가능하다.
#  -> ['foo', 'peekaboo', 'baz']
```
3. 딕셔너리(dict)
* 딕셔너리는 파이썬 내장 자료구조 중에 가장 중요한 자료구조다.
* 중괄호 `{}`를 사용해 콜론으로 구분된 키와 값을 둘러싸면 딕셔너리가 생성된다.
``` python
d1 = {"a" : "some value", "b" : [1, 2, 3, 4]} #  :를 기준으로 왼쪽은 키, 오른쪽은 값
d1[7] = "an integer" # 키는 7, "an integer"는 값
# -> {"a" : "some value", "b" : [1, 2, 3, 4], 7: 'an integer'}
d1["b"]
# -> [1, 2, 3, 4]
```

내장 순차 자료형 함수
* 파이썬은 순차 자료형에 사용할 수 있는 유용한 함수를 제공한다.
https://yujuwon.tistory.com/entry/enumeratezipreversed


<br>

### 함수
* 파이썬에서 코드를 재사용하고 조직화하기 위한 가장 중요한 수단
* 함수는 파이썬 명령들의 집합에 이름을 지어 좀 더 가독성이 좋은 코드를 작성할 수 있도록 돕는다.
* 함수는 def 예약어로 정의한다.
https://blockdmask.tistory.com/440

익명(람다) 함수
* 익명(annonymous) 함수 혹은 람다(lambda)함수라고 부르는 단순한 한 문장으로 이루어진 함수를 지원한다.
* lambda 예약어로 익명 함수를 정의하며, 이는 익명 함수를 선언한다 라는 의미다.
``` python
#  일반적인 함수
def short_function(x):
	return x * 2 

#  람다함수
equiv_anon = lambda x: x * 2
```
https://spidyweb.tistory.com/360

<br>
