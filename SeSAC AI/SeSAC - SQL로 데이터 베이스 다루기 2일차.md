## SeSAC - SQL로 데이터 베이스 다루기 2일차

2023.07.21

---

- 데이터 조작(data manipulation )

<br>

## 04-1 통계로 요약하기

<br>

### 기술통계 구하기

```python
# ns_book6는 데이터프레임 타입이다.
# 데이터타입을 확인할 수 있다.
# ns_book6.info()
ns_book6.describe()
```

|  | 번호 | 발행년도 | 도서권수 | 대출건수 |
| --- | --- | --- | --- | --- |
| count | 379976.000000 | 379976.000000 | 379976.000000 | 379976.000000 |
| mean | 201726.332847 | 2008.516306 | 1.135874 | 11.504629 |
| std | 115836.454596 | 8.780529 | 0.483343 | 19.241926 |
| min | 1.000000 | 1947.000000 | 0.000000 | 0.000000 |
| 25% | 102202.750000 | 2003.000000 | 1.000000 | 2.000000 |
| 50% | 203179.500000 | 2009.000000 | 1.000000 | 6.000000 |
| 75% | 301630.250000 | 2015.000000 | 1.000000 | 14.000000 |
| max | 401681.000000 | 2650.000000 | 40.000000 | 1765.000000 |

```python
# ns_book6에서 도서권수가 0초과인 값을 ns_book7에 저장
ns_book7 = ns_book6[ns_book6['도서권수']>0]

-> 3206
```

```python
# ns_book6에서 도서권수가 0초과인 값을 ns_book7에 저장
ns_book7 = ns_book6[ns_book6['도서권수']>0]
```

```python
# 백분위 중 30% 60% 90%를 출력
ns_book7.describe(percentiles=[0.3, 0.6, 0.9])
```

|  | 번호 | 발행년도 | 도서권수 | 대출건수 |
| --- | --- | --- | --- | --- |
| count | 376770.000000 | 376770.000000 | 376770.000000 | 376770.000000 |
| mean | 202977.476649 | 2008.460076 | 1.145540 | 11.593439 |
| std | 115298.245784 | 8.773148 | 0.473853 | 19.279409 |
| min | 1.000000 | 1947.000000 | 1.000000 | 0.000000 |
| 30% | 124649.700000 | 2004.000000 | 1.000000 | 2.000000 |
| 50% | 204550.500000 | 2009.000000 | 1.000000 | 6.000000 |
| 60% | 243537.400000 | 2011.000000 | 1.000000 | 8.000000 |
| 90% | 361341.100000 | 2018.000000 | 2.000000 | 28.000000 |
| max | 401681.000000 | 2650.000000 | 40.000000 | 1765.000000 |
|  |  |  |  |  |

```python
ns_book7.describe(include='object')
# 여기서 ISBN은 INT일까?
# ns_book7.info()
```

|  | 도서명 | 저자 | 출판사 | ISBN | 세트 ISBN | 부가기호 | 권 | 주제분류번호 | 등록일자 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| count | 376770 | 376770 | 376770 | 376770 | 55866 | 308252 | 61793 | 359792 | 376770 |
| unique | 336408 | 248850 | 21875 | 350810 | 14875 | 17 | 834 | 12467 | 4562 |
| top | 승정원일기 | 세종대왕기념사업회 [편] | 문학동네 | 9788937430299 | 9788937460005 | 0 | 1 | 813.6 | 1970-01-01 |
| freq | 250 | 303 | 4410 | 206 | 702 | 158235 | 13282 | 14816 | 28185 |

<br>

### 평균

<img width="218" alt="스크린샷 2023-07-21 오전 11 19 35" src="https://github.com/kimbap918/TIL/assets/75712723/4afea0f7-2960-4aa9-b453-d027be39524d">

```python
# x는 리스트타입, iterable(셀 수 있는, 순회가능한) 객체다.
x = [10, 20, 30]
sum = 0
for i in range(3):
    sum += x[i]
print("평균:", sum / len(x))

# for i in x:
#     sum += i # sum = sum + i
# print("평균:", sum / len(x))

-> 평균: 20.0
```

```python
# .mean()을 통해 평균을 구할수있다.
ns_book7['대출건수'].mean()

-> 11.593438968070707
```

<br>

### 평균이 가지는 단점?

- 데이터 이상치(outlier)에 취약하다.
- 그렇기 때문에 평균이 아닌 중앙값을 사용한다.

[Leaving Google Colab](https://colab.research.google.com/corgiredirector?site=https://gannigoing.medium.com/%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%9D%B4%EC%83%81%EC%B9%98-outlier-%EC%9D%98-%EA%B8%B0%EC%A4%80%EC%9D%80-%EB%AC%B4%EC%97%87%EC%9D%BC%EA%B9%8C-f11f60bf901a&link_redirector=1)

<br>

### 중앙값

```python
ns_book7['대출건수'].median()

-> 6.0

temp_df = pd.DataFrame([1,2,3,4])
temp_df.median()

->
0    2.5
dtype: float64

ns_book7['대출건수'].drop_duplicates().median()

-> 183.0
```

<br>

### 분위수

```python
# 박스 수염 차트?
ns_book7['대출건수'].quantile(0.25)

-> 2.0
```

```python
ns_book7['대출건수'].quantile([0.25,0.5,0.75])

-> 
0.25     2.0
0.50     6.0
0.75    14.0
Name: 대출건수, dtype: float64
```

<br>

### 분산

<img width="209" alt="스크린샷 2023-07-21 오전 10 48 25" src="https://github.com/kimbap918/TIL/assets/75712723/f3d855a7-cc34-4cae-8a9c-b32af1bb0006">

- 잔차(residual)의 제곱의 평균.
- 제곱을 하는 이유는 음수처리를 하기위해

```python
# 분산이 왜 필요할까?
# 평균에서 얼마나 떨어져 있는지를 확인하기 위해서.
# 다만, 떨어진 값을 음수 처리하기 위해 제곱한다.
# 분산이 크면 예측이 어렵다.
ns_book7['대출건수'].var()

-> 371.69563042906674
```

<br>

### 표준 편차

<img width="221" alt="스크린샷 2023-07-21 오전 10 50 26" src="https://github.com/kimbap918/TIL/assets/75712723/8dfb43c2-323d-4634-941c-52c42e73ccec">

```python
ns_book7['대출건수'].std()

-> 19.279409493785508
```

<br>

### 최빈값

```python
ns_book7['도서명'].mode()

-> 
0    승정원일기
Name: 도서명, dtype: object
```

<br>

### 최솟값, 최댓값

```python
ns_book7['대출건수'].min()

-> 0

ns_book7['대출건수'].max()

-> 1765
```

<br>

### 데이터프레임에서 기술통계 구하기

```python
ns_book7.mean(numeric_only=True)

->
번호      202977.476649
발행년도      2008.460076
도서권수         1.145540
대출건수        11.593439
dtype: float64
```

```python
ns_book7.loc[:, '도서명':].mode()
```

|  | 도서명 | 저자 | 출판사 | 발행년도 | ISBN | 세트 ISBN | 부가기호 | 권 | 주제분류번호 | 도서권수 | 대출건수 | 등록일자 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 승정원일기 | 세종대왕기념사업회 [편] | 문학동네 | 2012.0 | 9788937430299 | 9788937460005 | 0 | 1 | 813.6 | 1 | 0 | 1970-01-01 |

<br>

### 넘파이(numpy)의 기술통계 함수

<br>

### 평균 구하기

```python
import numpy as np

np.mean(ns_book7['대출건수'])

-> 11.593438968070707
```

```python
# np의 average 함수는 mean과 다르게 가중치(weights)를 줄수있다.
np.average(ns_book7['대출건수'], weights=1/ns_book7['도서권수'])

-> 10.543612175385386
```

<br>

### 중앙값 구하기

```python
np.median(ns_book7['대출건수'])

-> 6.0
```

<br>

### 최솟값, 최댓값 구하기

```python
np.min(ns_book7['대출건수'])

-> 0

np.max(ns_book7['대출건수'])

-> 1765
```

<br>

### 분위수 구하기

```python
# interpolation 매개변수가 numpy 1.22(python >= 3.8) 버전부터 method로 바뀜
np.quantile(ns_book7['대출건수'], [0.25,0.5,0.75])

-> array([ 2.,  6., 14.])
```

<br>

### 분산 구하기

```python
# var = variance(분산)
np.var(ns_book7['대출건수'])

-> 371.6946438971496
```

<br>

### 표준 편차 구하기

```python
np.std(ns_book7['대출건수'])

-> 19.27938390865096
```

<br>

### 최빈값 구하기

```python
values, counts = np.unique(ns_book7['도서명'], return_counts=True)
max_idx = np.argmax(counts)
values[max_idx]

-> '승정원일기'
```

<br>

### (참고) 키바나(kibana), powerbi

[Kibana: 데이터 탐색, 시각화, 발견 | Elastic](https://www.elastic.co/kr/kibana/)

[다운로드 | Microsoft Power BI](https://powerbi.microsoft.com/ko-kr/downloads/)

<br>

## 04-2 분포 요약하기

<br>

### 산점도 그리기

```python
# 파일 다운로드
import gdown

gdown.download('https://bit.ly/3pK7iuu', 'ns_book7.csv', quiet=False)

# 판다스 라이브러리 import 및 csv로드
import pandas as pd

ns_book7 = pd.read_csv('ns_book7.csv', low_memory=False)
ns_book7.head()
```

|  | 번호 | 도서명 | 저자 | 출판사 | 발행년도 | ISBN | 세트 ISBN | 부가기호 | 권 | 주제분류번호 | 도서권수 | 대출건수 | 등록일자 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1 | 인공지능과 흙 | 김동훈 지음 | 민음사 | 2021 | 9788937444319 | NaN | NaN | NaN | NaN | 1 | 0 | 2021-03-19 |
| 1 | 2 | 가짜 행복 권하는 사회 | 김태형 지음 | 갈매나무 | 2021 | 9791190123969 | NaN | NaN | NaN | NaN | 1 | 0 | 2021-03-19 |
| 2 | 3 | 나도 한 문장 잘 쓰면 바랄 게 없겠네 | 김선영 지음 | 블랙피쉬 | 2021 | 9788968332982 | NaN | NaN | NaN | NaN | 1 | 0 | 2021-03-19 |
| 3 | 4 | 예루살렘 해변 | 이도 게펜 지음, 임재희 옮김 | 문학세계사 | 2021 | 9788970759906 | NaN | NaN | NaN | NaN | 1 | 0 | 2021-03-19 |
| 4 | 5 | 김성곤의 중국한시기행 : 장강·황하 편 | 김성곤 지음 | 김영사 | 2021 | 9788934990833 | NaN | NaN | NaN | NaN | 1 | 0 | 2021-03-19 |

```python
# matplotlib 안에 pyplot을 불러와서 plt로 지정
import matplotlib.pyplot as plt

# scatter 산점도
# scatter는 기본적으로 2개의 인자를 받는데 scatter(x축 값, y축 값)다.
plt.scatter([1,2,3,4], [1,2,3,4])
# show()를 해야 그려준다.
plt.show()
```

![Untitled (3)](https://github.com/kimbap918/TIL/assets/75712723/2cc6a10c-89fc-49b2-81de-ce17cf629b25)

```python
# x축에 번호, y축에 대출건수
plt.scatter(ns_book7['번호'], ns_book7['대출건수'])
plt.show()
```

![Untitled (4)](https://github.com/kimbap918/TIL/assets/75712723/f3fe6f64-221f-45a1-8cae-3a07b10b398c)

```python
plt.scatter(ns_book7['도서권수'], ns_book7['대출건수'])
plt.show()
```

![Untitled (5)](https://github.com/kimbap918/TIL/assets/75712723/e43d52af-0ac5-4743-a229-d550e9c2455c)

```python
# alpha = 투명도, 수치가 높아질수록 진해진다.
plt.scatter(ns_book7['도서권수'], ns_book7['대출건수'], alpha=0.1)
plt.show()
```

![Untitled (6)](https://github.com/kimbap918/TIL/assets/75712723/102ece30-5de6-4963-b1dd-6a03e28c4eb4)

```python
average_borrows = ns_book7['대출건수']/ns_book7['도서권수']
plt.scatter(average_borrows, ns_book7['대출건수'], alpha=0.1)
plt.show()
```

![Untitled (7)](https://github.com/kimbap918/TIL/assets/75712723/7c7c2250-747e-44b7-936b-a886f86b6f67)

<br>

### 히스토그램

- 막대그래프와 히스토그램은 다르다
- 히스토그램은 간격(극간)이 없다
- 둘의 차이를 구분할 필요가 있다

```python
# bins = 구간을 설정한다.
# bins = 5 구간이 5개
plt.hist([0,3,5,6,7,7,9,13], bins=5)
plt.show()
```

![Untitled (8)](https://github.com/kimbap918/TIL/assets/75712723/9535ba0b-2f46-4d99-9008-7cdfcf718aac)

```python
import numpy as np
# 극간을 알기 위해(어디서 끊기는지를 알기 위해) histogram_bin_edges를 사용
np.histogram_bin_edges([0,3,5,6,7,7,9,13], bins=5)

-> array([ 0. ,  2.6,  5.2,  7.8, 10.4, 13. ])
```

```python
# np.random.seed(42)는 NumPy 라이브러리의 난수 생성 함수인 random이나 randn 등을 사용할 때,
# 난수 생성의 시작점을 설정하는 역할을 한다.
# 난수 생성 알고리즘은 사실 의사난수(Pseudorandom)라고 불리는데, 
# 이는 초기값인 시드(seed)를 기반으로 난수를 생성한다. 
# 따라서, 동일한 시드값을 가지고 있다면 항상 같은 난수를 생성하게 된다.

np.random.seed(42)
# 0을 기준으로 한 난수를 1000개 생성
random_samples = np.random.randn(1000)
```

```python
# 난수의 평균과, 표준편차(데이터가 평균 주위에 모여있는 정도)를 출력
print(np.mean(random_samples), np.std(random_samples))

-> 0.01933205582232549 0.9787262077473543
```

<br>

### 왜 seed를 42로 줬을까?(심오함, 중요)

**"삶, 우주, 그리고 모든 것에 대한 궁극적인 질문의 해답"**

[random seed로 42를 사용하는 이유](https://rchoi-19-4-2.tistory.com/159)

<br>

```python
plt.hist(random_samples)
plt.show()
```

![Untitled (9)](https://github.com/kimbap918/TIL/assets/75712723/a9cc9f89-16f9-4749-9f62-4c36d7f59966)

```python
plt.hist(ns_book7['대출건수'])
plt.show()
```

![Untitled (10)](https://github.com/kimbap918/TIL/assets/75712723/0a3708f8-6441-4d35-a660-59d1f337c1a9)

```python
plt.hist(ns_book7['대출건수'])
# 축의 스케일 변경
plt.yscale('log')
plt.show()
```

![Untitled (11)](https://github.com/kimbap918/TIL/assets/75712723/7208427e-c746-43cc-87dc-b575d118b9c4)

```python
plt.hist(ns_book7['대출건수'], log=True)plt.show()
```

![Untitled (12)](https://github.com/kimbap918/TIL/assets/75712723/8f18d7dd-c486-4788-ab1b-eb0b4b54ff44)

```python
plt.hist(ns_book7['대출건수'], bins=100)
plt.yscale('log')
plt.show()
```

![Untitled (13)](https://github.com/kimbap918/TIL/assets/75712723/fd49ee87-0343-4e6d-bfc9-bbd833fe3c0b)

<br>

### 스케일을 바꾸는 작업을 하는 이유?

- 위의 그래프는 x축에 비해 y축이 극단적으로 높기 때문에 차이를 드러내기가 힘들다.
- 그렇기 때문에 한 그래프에서 나타내려면 로그 스케일을 사용하는데 로그 스케일은 **상대적인 비율을 나타내기 때문에** 절대적인 차이가 상대적인 비율로 줄어든 만큼 더 넓은 범위의 값을 나타낼 수 있다.

```python
# 도서명의 길이
title_len = ns_book7['도서명'].apply(len)
# 도서명의 길이를 100개의 구간으로 나눠서 히스토그램으로 찍는다.
plt.hist(title_len, bins=100)
plt.show()

# 도서명이 100글자는..?
```

![Untitled (14)](https://github.com/kimbap918/TIL/assets/75712723/1604a270-6c17-4244-abbc-c9a4a77b5dd7)

```python
plt.hist(title_len, bins=100)
plt.xscale('log')
plt.show()
```

![Untitled (15)](https://github.com/kimbap918/TIL/assets/75712723/3c1fcfe3-9145-4ed8-be27-d788bcef22da)

<br>

### 상자 수염 그림 그리기

- 전체 숫자의 중위값은 주황선
- 상자는 데이터의 25번째 백분위수(하위 25%), 50번째 백분위수(중앙값), 75번째 백분위수(상위 25%)를 나타낸다.  따라서, 상자는 데이터의 중간 50% 범위를 표현하게 된다. 이러한 중간 50% 범위를 '사분위 범위(IQR, Interquartile Range)'라 한다.
- box plot의 사분위 범위(IQR, Interquartile Range)1.5배 구간을 수염으로 표기한다.
- 그 외의 점 구간을 outlier(데이터 이상치)로 나타낸다.
  
    ![스크린샷 2023-07-21 오후 12 57 00](https://github.com/kimbap918/TIL/assets/75712723/2f975d76-ec88-4e20-a591-25f6e6373796)
    

```python
temp = ns_book7[['대출건수', '도서권수']]
```

```python
plt.boxplot(temp)
plt.show()
```

![Untitled (16)](https://github.com/kimbap918/TIL/assets/75712723/d75b414b-2d06-46ec-9828-90a7a71a3019)

```python

plt.boxplot(ns_book7[['대출건수', '도서권수']])
# y축 스케일변경(log)
# 전체 숫자의 중위값은 주황선

# 상자는 데이터의 25번째 백분위수(하위 25%), 
# 50번째 백분위수(중앙값), 75번째 백분위수(상위 25%)를 나타낸다. 
# 따라서, 상자는 데이터의 중간 50% 범위를 표현하게 된다. 
# 이러한 중간 50% 범위를 '사분위 범위(IQR, Interquartile Range)'라 한다.

# box plot의 사분위 범위(IQR, Interquartile Range)1.5배 구간을 수염으로 표기한다.
# 그 외의 점 구간을 outlier(데이터 이상치)로 나타낸다. 
plt.yscale('log')
plt.show()
```

![Untitled (17)](https://github.com/kimbap918/TIL/assets/75712723/bd54386c-21c8-4301-9009-d8235482c6e0)

```python
# 수평으로 그릴때 vert=False
plt.boxplot(ns_book7[['대출건수', '도서권수']], vert=False)
plt.xscale('log')
plt.show()
```

![Untitled (18)](https://github.com/kimbap918/TIL/assets/75712723/2cdcff7c-b71c-4474-96e0-b0c867f0561c)

```python
# whis를 높게 설정하면 멀리까지 있는 outlier 값들을 수염으로 볼수있다.
plt.boxplot(ns_book7[['대출건수', '도서권수']], whis=10)
plt.yscale('log')
plt.show()
```

![Untitled (19)](https://github.com/kimbap918/TIL/assets/75712723/67600bd2-8823-4ddc-92b1-16794234a092)

```python
# 백분위로도 설정이 가능하다.
plt.boxplot(ns_book7[['대출건수','도서권수']], whis=(0,100))
plt.yscale('log')
plt.show()
```

![Untitled (20)](https://github.com/kimbap918/TIL/assets/75712723/196d89ed-5a34-4b5f-a117-db3280f58a12)

<br>

### boxplot 해석해보기

[상자 그림(boxplot), 상자 그림(boxplot) 해석방법](https://codedragon.tistory.com/7012)

<br>

### 판다스 그래프의 함수

### 선점도 그리기

```python
ns_book7.plot.scatter('도서권수', '대출건수', alpha=0.1)
plt.show()
```

![Untitled (21)](https://github.com/kimbap918/TIL/assets/75712723/c14a8ddb-055c-40b8-886a-4481c1ce6a5a)

```python
ns_book7['도서명'].apply(len).plot.hist(bins=100)
plt.show()
```

![Untitled (22)](https://github.com/kimbap918/TIL/assets/75712723/7ef99f19-0397-45e5-830a-b357bffec41a)

<br>

### 상자 수염 그리기

```python
ns_book7[['대출건수', '도서권수']].boxplot()
plt.yscale('log')
plt.show()
```

![Untitled (23)](https://github.com/kimbap918/TIL/assets/75712723/c44c8977-a408-4535-8b23-ae3501155caf)

<br>

## 05-1 맷플롯립(matplotlib) 기본 요소 알아보기

<br>

### Figure 클래스

```python
import gdown

gdown.download('https://bit.ly/3pK7iuu', 'ns_book7.csv', quiet=False)

->
Downloading...
From:https://bit.ly/3pK7iuu
To: /content/ns_book7.csv
100%|██████████| 53.8M/53.8M [00:00<00:00, 158MB/s]
'ns_book7.csv'
```

```python
import pandas as pd

ns_book7 = pd.read_csv('ns_book7.csv', low_memory=False)
ns_book7.head()
```

|      | 번호 | 도서명                               | 저자                        | 출판사     | 발행년도 | ISBN          | 세트 ISBN | 부가기호 | 권   | 주제분류번호 | 도서권수 | 대출건수 | 등록일자   |
| ---- | ---- | ------------------------------------ | --------------------------- | ---------- | -------- | ------------- | --------- | -------- | ---- | ------------ | -------- | -------- | ---------- |
| 0    | 1    | 인공지능과 흙                        | 김동훈 지음                 | 민음사     | 2021     | 9788937444319 | NaN       | NaN      | NaN  | NaN          | 1        | 0        | 2021-03-19 |
| 1    | 2    | 가짜 행복 권하는 사회                | 김태형 지음                 | 갈매나무   | 2021     | 9791190123969 | NaN       | NaN      | NaN  | NaN          | 1        | 0        | 2021-03-19 |
| 2    | 3    | 나도 한 문장 잘 쓰면 바랄 게 없겠네  | 김선영 지음                 | 블랙피쉬   | 2021     | 9788968332982 | NaN       | NaN      | NaN  | NaN          | 1        | 0        | 2021-03-19 |
| 3    | 4    | 예루살렘 해변                        | 이도 게펜 지음, 임재희 옮김 | 문학세계사 | 2021     | 9788970759906 | NaN       | NaN      | NaN  | NaN          | 1        | 0        | 2021-03-19 |
| 4    | 5    | 김성곤의 중국한시기행 : 장강·황하 편 | 김성곤 지음                 | 김영사     | 2021     | 9788934990833 | NaN       | NaN      | NaN  | NaN          | 1        | 0        | 2021-03-19 |

```python
# 맷플롯립 라이브러리를 가져와 plt로 지정
import matplotlib.pyplot as plt

plt.scatter(ns_book7['도서권수'], ns_book7['대출건수'], alpha=0.1)
plt.show()
```

![Untitled (24)](https://github.com/kimbap918/TIL/assets/75712723/c25d29b3-7377-4d31-b51a-91e1bb0f8125)

```python
# rc = run configure
print(plt.rcParams['figure.figsize'])

-> [6.4, 4.8] # 여기서 나오는 값은 inch값 [16.256cm, 12.192cm]
```

```python
plt.figure(figsize=(9, 6))
plt.scatter(ns_book7['도서권수'], ns_book7['대출건수'], alpha=0.1)
plt.show()
```

![Untitled (25)](https://github.com/kimbap918/TIL/assets/75712723/53de6c12-bd13-4d80-a739-419aba529914)

```python
# 1인치당 72개의 점이 찍힌다.
print(plt.rcParams['figure.dpi'])

-> 72
```

```python
plt.figure(figsize=(900/72, 600/72))
plt.scatter(ns_book7['도서권수'], ns_book7['대출건수'], alpha=0.1)
plt.show()
```

![Untitled (26)](https://github.com/kimbap918/TIL/assets/75712723/a1b83a4d-6270-4eba-bf0f-cd73ca37773d)

```python
%config InlineBackend.print_figure_kwargs = {'bbox_inches': None}
plt.figure(figsize=(900/72, 600/72))
plt.scatter(ns_book7['도서권수'], ns_book7['대출건수'], alpha=0.1)
plt.show()
```

![Untitled (27)](https://github.com/kimbap918/TIL/assets/75712723/2ad87287-1cb9-4e12-8623-d3ebef0f7af8)

```python
# {'bbox_inches': 'tight'}
# bounding box 테두리를 공백 없이 찍는다.
%config InlineBackend.print_figure_kwargs = {'bbox_inches': 'tight'}
```

```python
plt.figure(dpi=144)
plt.scatter(ns_book7['도서권수'], ns_book7['대출건수'], alpha=0.1)
plt.show()
```

![Untitled (28)](https://github.com/kimbap918/TIL/assets/75712723/2930a46e-37e4-46c7-a4a9-2d6ae61bff85)

<br>

### rcParams 객체

```python
plt.rcParams['figure.dpi'] = 100
```

```python
plt.rcParams['scatter.marker']

-> 'o'
```

```python
# 보통 '^'(caret) 모양을 많이 사용한다 
plt.rcParams['scatter.marker'] = '*'
```

```python
plt.scatter(ns_book7['도서권수'], ns_book7['대출건수'], alpha=0.1)
plt.show()
```

![Untitled (29)](https://github.com/kimbap918/TIL/assets/75712723/230fe5ab-55b0-4ba8-916a-59d2f530b514)

```python
plt.scatter(ns_book7['도서권수'], ns_book7['대출건수'], alpha=0.1, marker='+')
plt.show()
```

![Untitled (30)](https://github.com/kimbap918/TIL/assets/75712723/3d2c9ba9-9d5a-4444-91d4-d10a0661c569)

<br>

### 여러 개의 서브플롯 출력하기

```python
# 그래프, 축
fig, axs = plt.subplots(2)

# 축의 첫번째 행에는 x축에 도서권수, y축에 대출건수로 산점도를
axs[0].scatter(ns_book7['도서권수'], ns_book7['대출건수'], alpha=0.1)

# 축의 두번째 행에는 히스토그램을
axs[1].hist(ns_book7['대출건수'], bins=100)
# y스케일은 로그스케일로 그린다.
axs[1].set_yscale('log')

fig.show()
```

![Untitled (48)](https://github.com/kimbap918/TIL/assets/75712723/e972b377-e502-48e2-b98b-8ef7aa9179f9)

```python
# 그래프, 축, 좌우로 그리고 옆으로 늘려준다.
# subplot(행의 갯수, 열의 갯수, figsize=(가로인치, 세로인치))
fig, axs = plt.subplots(1, 2, figsize=(10, 4))

# 축의 첫번째 행에는 x축에 도서권수, y축에 대출건수로 산점도를
axs[0].scatter(ns_book7['도서권수'], ns_book7['대출건수'], alpha=0.1)

# 축의 두번째 행에는 히스토그램을
axs[1].hist(ns_book7['대출건수'], bins=100)
# y스케일은 로그스케일로 그린다.
axs[1].set_yscale('log')

fig.show()
```

![Untitled (31)](https://github.com/kimbap918/TIL/assets/75712723/0a466d3c-78c8-4d05-8667-15fce08ae7a9)

```python
fig, axs = plt.subplots(2, figsize=(6, 8))

axs[0].scatter(ns_book7['도서권수'], ns_book7['대출건수'], alpha=0.1)
axs[0].set_title('scatter plot')

axs[1].hist(ns_book7['대출건수'], bins=100)
axs[1].set_title('histogram')
axs[1].set_yscale('log')

fig.show()
```

![Untitled (32)](https://github.com/kimbap918/TIL/assets/75712723/9697a235-a81d-47c3-bdbe-849ff635dfdf)

```python
fig, axs = plt.subplots(1, 2, figsize=(10, 4))

# 축의 첫번째 행에는 x축에 도서권수, y축에 대출건수로 산점도
axs[0].scatter(ns_book7['도서권수'], ns_book7['대출건수'], alpha=0.1)
# 첫번째 행의 제목은 scatter plot
axs[0].set_title('scatter plot')
# 첫번째 행의 x축 라벨은 number of books(도서권수)
axs[0].set_xlabel('number of books')
# 첫번째 행의 y축 라벨은 borrow count(대출건수)
axs[0].set_ylabel('borrow count')

# 축의 두번째 행에는 대출건수에 대한 히스토그램
axs[1].hist(ns_book7['대출건수'], bins=100)
# 축의 두번째 행의 제목은 histogram
axs[1].set_title('histogram')
# y축 스케일을 로그 스케일로
axs[1].set_yscale('log')
# 두번째 행의 x축 라벨은 borrow count(대출건수)
axs[1].set_xlabel('borrow count')
# 두번째 행의 y축 라벨은 frequency(대출빈도)
axs[1].set_ylabel('frequency')

fig.show()
```

![Untitled (33)](https://github.com/kimbap918/TIL/assets/75712723/f6f1357b-4ab2-45e6-b752-20c5f691240c)

<br>

## 05-2 선, 막대 그래프 그리기

<br>

### 연도별 발행 도서 개수 구하기

```python
import gdown

gdown.download('https://bit.ly/3pK7iuu', 'ns_book7.csv', quiet=False)

->
Downloading...
From: https://bit.ly/3pK7iuu
To: /content/ns_book7.csv
100%|██████████| 53.8M/53.8M [00:00<00:00, 68.3MB/s]
'ns_book7.csv
```

```python
import pandas as pd

ns_book7 = pd.read_csv('ns_book7.csv', low_memory=False)
ns_book7.head()
```

|      | 번호 | 도서명                               | 저자                        | 출판사     | 발행년도 | ISBN          | 세트 ISBN | 부가기호 | 권   | 주제분류번호 | 도서권수 | 대출건수 | 등록일자   |
| ---- | ---- | ------------------------------------ | --------------------------- | ---------- | -------- | ------------- | --------- | -------- | ---- | ------------ | -------- | -------- | ---------- |
| 0    | 1    | 인공지능과 흙                        | 김동훈 지음                 | 민음사     | 2021     | 9788937444319 | NaN       | NaN      | NaN  | NaN          | 1        | 0        | 2021-03-19 |
| 1    | 2    | 가짜 행복 권하는 사회                | 김태형 지음                 | 갈매나무   | 2021     | 9791190123969 | NaN       | NaN      | NaN  | NaN          | 1        | 0        | 2021-03-19 |
| 2    | 3    | 나도 한 문장 잘 쓰면 바랄 게 없겠네  | 김선영 지음                 | 블랙피쉬   | 2021     | 9788968332982 | NaN       | NaN      | NaN  | NaN          | 1        | 0        | 2021-03-19 |
| 3    | 4    | 예루살렘 해변                        | 이도 게펜 지음, 임재희 옮김 | 문학세계사 | 2021     | 9788970759906 | NaN       | NaN      | NaN  | NaN          | 1        | 0        | 2021-03-19 |
| 4    | 5    | 김성곤의 중국한시기행 : 장강·황하 편 | 김성곤 지음                 | 김영사     | 2021     | 9788934990833 | NaN       | NaN      | NaN  | NaN          | 1        | 0        | 2021-03-19 |

```python
# value_counts = 값의 중복치를 확인해준다.
# 예를들어, 2012년이 몇번이나 나왔는지 확인해준다 -> 18601번
count_by_year = ns_book7['발행년도'].value_counts()
count_by_year

->
2012    18601
2014    17797
2009    17611
2011    17523
2010    17503
        ...  
2650        1
2108        1
2104        1
2560        1
1947        1
Name: 발행년도, Length: 87, dtype: int64
```

```python
# sort_index()로 년도를 정렬해준다.
count_by_year = count_by_year.sort_index()
count_by_year

->
1947     1
1948     1
1949     1
1952    11
1954     1
        ..
2551     1
2552     2
2559     1
2560     1
2650     1
Name: 발행년도, Length: 87, dtype: int64
```

```python
# 정렬된 것 중 년도의 index값이 2030년 이하인것만 모아서 count_by_year에 저장
count_by_year = count_by_year[count_by_year.index <= 2030]
count_by_year

->
1947        1
1948        1
1949        1
1952       11
1954        1
        ...  
2020    11834
2021     1255
2025        1
2028        1
2030        1
Name: 발행년도, Length: 68, dtype: int64
```

<br>

### 주제별 도서 개수 구하기

```python
import numpy as np

def kdc_1st_char(no):
  if no is np.nan:
    return '-1'
  else:
		# 가져온 string 값의 첫번째만 return
    return no[0]

# 주제분류번호의 값을 가져와서 각각 몇개나 있는지 확인
count_by_subject = ns_book7['주제분류번호'].apply(kdc_1st_char).value_counts()
count_by_subject

->
8     108643
3      80767
5      40916
9      26375
6      25070
1      22647
-1     16978
7      15836
4      13688
2      13474
0      12376
Name: 주제분류번호, dtype: int64
```

<br>

### 선 그래프 그리기

```python
# 맷플롯립 import 후 plt로 지정
import matplotlib.pyplot as plt

plt.rcParams['figure.dpi'] = 100
```

```python
# 년도와 책의 개수
plt.plot(count_by_year.index, count_by_year.values)

plt.title('Books by year')
plt.xlabel('year')
plt.ylabel('number of books')
plt.show()
```

![Untitled (34)](https://github.com/kimbap918/TIL/assets/75712723/8427d3d0-918c-4b54-a280-6edeec7ecddd)

```python
# marker = 년도 별 마커 모양, linestyle = 선의 모양, color = 색깔
plt.plot(count_by_year, marker='.', linestyle=':', color='red')
plt.title('Books by year')
plt.xlabel('year')
plt.ylabel('number of books')
plt.show()
```

![Untitled (35)](https://github.com/kimbap918/TIL/assets/75712723/ba24ab74-ad10-47ed-8e6b-553326892d5b)

```python
# 맷플롯립에서는 '*-g'로 마커모양과 색을 설정할수 있다.
plt.plot(count_by_year, '*-g')
plt.title('Books by year')
plt.xlabel('year')
plt.ylabel('number of books')
plt.show()
```

![Untitled (50)](https://github.com/kimbap918/TIL/assets/75712723/c9ecca74-78a0-4099-8341-824a94708d83)

```python
plt.plot(count_by_year, '*-g')
plt.title('Books by year')
plt.xlabel('year')
plt.ylabel('number of books')
# 1947년부터 2030년까지 10년 단위로
plt.xticks(range(1947, 2030, 10))
# [::5]모든 값에 대해서 5개씩 건너뛰면서 가져온다.
# 이 때문에 그래프 마커에 숫자가 5칸 단위로 나타나고있다.
for idx, val in count_by_year[::5].items():
  # 값을 찍는 함수
	# annotate(그래프에 나타날 문자열, (텍스트가 나타날 x, y 좌표))
  plt.annotate(val, (idx, val))
plt.show()
```

![Untitled (51)](https://github.com/kimbap918/TIL/assets/75712723/ef5cd493-8506-441c-9c02-2b5c11851b38)

```python
plt.plot(count_by_year, '*-g')
plt.title('Books by year')
plt.xlabel('year')
plt.ylabel('number of books')
plt.xticks(range(1947, 2030, 10))
for idx, val in count_by_year[::5].items():
  plt.annotate(val, (idx, val), xytext=(idx+1, val+10))
plt.show()
```

![Untitled (53)](https://github.com/kimbap918/TIL/assets/75712723/084e9657-c102-4ad3-90d8-50d4f5504c76)

```python
plt.plot(count_by_year, '*-g')
plt.title('Books by year')
plt.xlabel('year')
plt.ylabel('number of books')
plt.xticks(range(1947, 2030, 10))
for idx, val in count_by_year[::5].items():
  plt.annotate(val, (idx, val), xytext=(2, 2), textcoords='offset points')
plt.show()
```

![Untitled](../43cddcb5-47a6-49f5-8077-aa12af408770_Export-21243d02-0f6f-467c-9f58-f7646aa84b44/SeSAC - SQL로 데이터 베이스 다루기 2일차 48b2181603724ac9bb2826ba7e82b80a/Untitled 37.png)

<br>

### 막대 그래프 그리기

```python
# bar(x축, y축)
plt.bar(count_by_subject.index, count_by_subject.values)
plt.title('Books by subject')
plt.xlabel('subject')
plt.ylabel('number of books')
for idx, val in count_by_subject.items():
  plt.annotate(val, (idx, val), xytext=(0, 2), textcoords='offset points')
plt.show()
```

![Untitled](../43cddcb5-47a6-49f5-8077-aa12af408770_Export-21243d02-0f6f-467c-9f58-f7646aa84b44/SeSAC - SQL로 데이터 베이스 다루기 2일차 48b2181603724ac9bb2826ba7e82b80a/Untitled 38.png)

```python
plt.bar(count_by_subject.index, count_by_subject.values, width=0.7, color='blue')
plt.title('Books by subject')
plt.xlabel('subject')
plt.ylabel('number of books')
for idx, val in count_by_subject.items():
	# offsetpoint를 잡아서 막대의 숫자 표기 위치를 조정함.
	# va = 정렬, color = 색
  plt.annotate(val, (idx, val), xytext=(0, 2), textcoords='offset points', fontsize=8, va='center', color='green')
plt.show()
```

![Untitled](../43cddcb5-47a6-49f5-8077-aa12af408770_Export-21243d02-0f6f-467c-9f58-f7646aa84b44/SeSAC - SQL로 데이터 베이스 다루기 2일차 48b2181603724ac9bb2826ba7e82b80a/Untitled 39.png)

```python
plt.barh(count_by_subject.index, count_by_subject.values, height=0.7, color='blue')
plt.title('Books by subject')
plt.xlabel('number of books')
plt.ylabel('subject')
for idx, val in count_by_subject.items():
		# annotate의 찍히는 x, y좌표를 바꿈
    plt.annotate(val, (val, idx), xytext=(2, 0), textcoords='offset points',
                 fontsize=8, va='center', color='green') # 가운데 정렬, 색은 초록
plt.show()
```

![Untitled](../43cddcb5-47a6-49f5-8077-aa12af408770_Export-21243d02-0f6f-467c-9f58-f7646aa84b44/SeSAC - SQL로 데이터 베이스 다루기 2일차 48b2181603724ac9bb2826ba7e82b80a/Untitled 40.png)

<br>

### 이미지 출력하고 저장하기

```python
import sys

if 'google.colab' in sys.modules:
  !wget https://bit.ly/3wrj4xf -O jupiter.png
```

```python
# 이미지를 불러올때 imread사용
img = plt.imread('jupiter.png')
img.shape

# 가로, 세로, 픽셀의 이미지값(RGB)
-> (1561, 1646, 3)

plt.imshow(img)
plt.show()
```

![Untitled](../43cddcb5-47a6-49f5-8077-aa12af408770_Export-21243d02-0f6f-467c-9f58-f7646aa84b44/SeSAC - SQL로 데이터 베이스 다루기 2일차 48b2181603724ac9bb2826ba7e82b80a/Untitled 41.png)

```python
plt.figure(figsize=(8, 6))
plt.imshow(img)
# 축을 제거함. 
# 매트플롯에서는 이미지도 차트로 표시하기때문에 축이 나온다.
plt.axis('off')
plt.show()
```

![Untitled](../43cddcb5-47a6-49f5-8077-aa12af408770_Export-21243d02-0f6f-467c-9f58-f7646aa84b44/SeSAC - SQL로 데이터 베이스 다루기 2일차 48b2181603724ac9bb2826ba7e82b80a/Untitled 42.png)

```python
from PIL import Image

pil_img = Image.open('jupiter.png')
plt.figure(figsize=(8, 6))
plt.imshow(pil_img)
plt.axis('off')
plt.show()
```

![Untitled](../43cddcb5-47a6-49f5-8077-aa12af408770_Export-21243d02-0f6f-467c-9f58-f7646aa84b44/SeSAC - SQL로 데이터 베이스 다루기 2일차 48b2181603724ac9bb2826ba7e82b80a/Untitled 43.png)

```python
import numpy as np

arr_img = np.array(pil_img)
arr_img.shape

-> (1561, 1646, 3)

# 저장
plt.imsave('jupiter.jpg', arr_img)
```

<br>

### 그래프를 이미지로 저장하기

```python
plt.rcParams['savefig.dpi']

-> 'figure'
```

```python
plt.barh(count_by_subject.index, count_by_subject.values, height=0.7, color='blue')
plt.title('Books by subject')
plt.xlabel('number of books')
plt.ylabel('subject')
for idx, val in count_by_subject.items():
    plt.annotate(val, (val, idx), xytext=(2, 0), textcoords='offset points',
                 fontsize=8, va='center', color='green')
# 그림으로 저장
# savefig('제목')
plt.savefig('books_by_subject.png')
plt.show()
```

![Untitled](../43cddcb5-47a6-49f5-8077-aa12af408770_Export-21243d02-0f6f-467c-9f58-f7646aa84b44/SeSAC - SQL로 데이터 베이스 다루기 2일차 48b2181603724ac9bb2826ba7e82b80a/Untitled 44.png)

```python
# 이미지 불러오기
pil_img = Image.open('books_by_subject.png')
plt.figure(figsize=(8, 6))
plt.imshow(pil_img)
plt.axis('off')
plt.show()
```

<br>



## 과제2 - 데이터 기초 통계와 그래프

- 주관적으로 작성되어 틀릴 수 있습니다.

### 조건

```
1. 화일을 읽어 옵니다. 

2. 모든 데이터에 대하여 기초 통계량을 알아 봅시다. 

3. 알콜도수(alcohol)가 x축 당도(resdual sugar)가 y  축인  산점도를 그리되 마커는 삼각형을 이용합니다. 

4. 당도(resdual sugar)가 x축으로된 히스토 그램을 그리되 구간은 5개로 합니다.  

5. 3번과 4번 그래프는 서브플롯을 이용하여 1행 2열로 그리되 가로 세로는 20:8설정 합니다. 즉 가로로 긴 형태로 구성합니다. 

6. 모든 그래프는 x, y 축에 레이블이 있어야 합니다. 그래프 타이틀은 안 넣어도 됩니다. 

코드 구성한 노트북 화일을 제출 합니다.
```

```python
# 1. 파일 읽어오기
import pandas as pd

ns_alc = pd.read_csv('/content/winequality-white.csv', sep=';', low_memory=False, )
ns_alc.head()
```

|      | fixed acidity | volatile acidity | citric acid | residual sugar | chlorides | free sulfur dioxide | total sulfur dioxide | density | pH   | sulphates | alcohol | quality |
| ---- | ------------- | ---------------- | ----------- | -------------- | --------- | ------------------- | -------------------- | ------- | ---- | --------- | ------- | ------- |
| 0    | 7.0           | 0.27             | 0.36        | 20.7           | 0.045     | 45.0                | 170.0                | 1.0010  | 3.00 | 0.45      | 8.8     | 6       |
| 1    | 6.3           | 0.30             | 0.34        | 1.6            | 0.049     | 14.0                | 132.0                | 0.9940  | 3.30 | 0.49      | 9.5     | 6       |
| 2    | 8.1           | 0.28             | 0.40        | 6.9            | 0.050     | 30.0                | 97.0                 | 0.9951  | 3.26 | 0.44      | 10.1    | 6       |
| 3    | 7.2           | 0.23             | 0.32        | 8.5            | 0.058     | 47.0                | 186.0                | 0.9956  | 3.19 | 0.40      | 9.9     | 6       |
| 4    | 7.2           | 0.23             | 0.32        | 8.5            | 0.058     | 47.0                | 186.0                | 0.9956  | 3.19 | 0.40      | 9.9     | 6       |

```python
# 2. 모든 데이터에 대하여 기초 통계량을 알아보기
ns_alc.describe()
```

|       | fixed acidity | volatile acidity | citric acid | residual sugar | chlorides   | free sulfur dioxide | total sulfur dioxide | density     | pH          | sulphates   | alcohol     | quality     |
| ----- | ------------- | ---------------- | ----------- | -------------- | ----------- | ------------------- | -------------------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| count | 4898.000000   | 4898.000000      | 4898.000000 | 4898.000000    | 4898.000000 | 4898.000000         | 4898.000000          | 4898.000000 | 4898.000000 | 4898.000000 | 4898.000000 | 4898.000000 |
| mean  | 6.854788      | 0.278241         | 0.334192    | 6.391415       | 0.045772    | 35.308085           | 138.360657           | 0.994027    | 3.188267    | 0.489847    | 10.514267   | 5.877909    |
| std   | 0.843868      | 0.100795         | 0.121020    | 5.072058       | 0.021848    | 17.007137           | 42.498065            | 0.002991    | 0.151001    | 0.114126    | 1.230621    | 0.885639    |
| min   | 3.800000      | 0.080000         | 0.000000    | 0.600000       | 0.009000    | 2.000000            | 9.000000             | 0.987110    | 2.720000    | 0.220000    | 8.000000    | 3.000000    |
| 25%   | 6.300000      | 0.210000         | 0.270000    | 1.700000       | 0.036000    | 23.000000           | 108.000000           | 0.991723    | 3.090000    | 0.410000    | 9.500000    | 5.000000    |
| 50%   | 6.800000      | 0.260000         | 0.320000    | 5.200000       | 0.043000    | 34.000000           | 134.000000           | 0.993740    | 3.180000    | 0.470000    | 10.400000   | 6.000000    |
| 75%   | 7.300000      | 0.320000         | 0.390000    | 9.900000       | 0.050000    | 46.000000           | 167.000000           | 0.996100    | 3.280000    | 0.550000    | 11.400000   | 6.000000    |
| max   | 14.200000     | 1.100000         | 1.660000    | 65.800000      | 0.346000    | 289.000000          | 440.000000           | 1.038980    | 3.820000    | 1.080000    | 14.200000   | 9.000000    |

```python
import matplotlib.pyplot as plt
# 3. 알콜도수가 x축, 당도가 y축인 산점도를 그리되, 마커는 삼각형
plt.figure(figsize=(9, 6))
plt.rcParams['scatter.marker'] = '^'
plt.scatter(ns_alc['alcohol'], ns_alc['residual sugar'], alpha=0.1)
plt.show()
```

![Untitled](../6feabf97-cddc-4e11-b1cb-1671e8270861_Export-db50adc7-5aed-4221-b4b6-16a7ca7f93b8/SeSAC - SQL로 데이터 베이스 다루기 2일차 48b2181603724ac9bb2826ba7e82b80a/Untitled 46.png)

```python
# 4. 당도(resdual sugar)가 x축으로된 히스토 그램을 그리되 구간은 5개
plt.hist(ns_alc['residual sugar'], bins=5)
plt.show()
```



```python
# 5. 3번과 4번 그래프는 서브플롯을 이용하여 1행 2열로 그리되 가로 세로는 20:8설정 
# 가로로 긴 형태로 구성

fig, axs = plt.subplots(1, 2, figsize=(20, 8))

axs[0].scatter(ns_alc['alcohol'], ns_alc['residual sugar'], alpha=0.1)
axs[1].hist(ns_alc['residual sugar'], bins=5)

# 6. 모든 그래프는 x, y 축에 레이블이 있어야 한다.
axs[0].set_xlabel('alcohol')
axs[0].set_ylabel('residual sugar')

axs[1].set_xlabel('residual sugar')
axs[1].set_ylabel('alcohol')

fig.show()
```

![Untitled](SeSAC%20-%20SQL%E1%84%85%E1%85%A9%20%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%87%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%89%E1%85%B3%20%E1%84%83%E1%85%A1%E1%84%85%E1%85%AE%E1%84%80%E1%85%B5%202%E1%84%8B%E1%85%B5%E1%86%AF%E1%84%8E%E1%85%A1%2048b2181603724ac9bb2826ba7e82b80a/Untitled%2048.png)





