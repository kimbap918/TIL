## SeSAC - Pandas(1) pandas와 시리즈, 데이터프레임

<br>

### pandas?

파이썬에서 데이터분석을 할 때 가장 많이 쓰이는 라이브러리

표 형태의 데이터를 다루는 다양한 기능을 제공하고 있다.

<br>

### pandas의 장점

- 엑셀, CSV등 다양한 데이터 형식을 지원
- 결측치 처리 기능
- 데이터 형태 바꾸기
- 데이터 삭제 및 추가
- 그룹화, 정렬, 결합
- 시계열 데이터
- 문자열 및 날짜/시간 지원
- 데이터 가시화 : 많은 그래프 처리 라이브러리와 연동

<br>

### CSV

- 엑셀과 연동되는 파일의 형태
- 데이터를 콤마(,) 형태로 구분
- pandas의 read_csv() 함수를 사용한다.

<br>

### TSV

- 데이터를 tab으로 구분한다.
- pandas에서는 TSV파일을 읽어오는 함수는 따로 제공하지 않는다.
- 하지만 read_csv() 함수를 이용하여 TSV파일을 읽어올 수 있다.

<br>

### pandas 불러오기

```python
import pandas as pd

pd.read_csv("파일이름.csv")
# sep = 구분자
# sep = '/t' 탭
pd.read_csv("파일이름.csv", sep = ',')
```

<br>

### 파일 생성/불러오기

```python
f = open("test.txt", 'wt') # write text, 새롭게 쓰는 기능
# f = open("test.txt", 'at') # attach text, 이어쓰기
f.write("hello")
f.close() # 저장하고 끄는 기능
f = open("test.txt", 'rt') # read text
data = f.read()
f.close()
```

<br>

### 시리즈와 데이터프레임

- 표 : 데이터프레임
- 시리즈 : 데이터 프레임에서 각각의 열, 판다스의 pd.Series() 함수를 사용해 시리즈를 생성할 수 있다.

```python
import pandas as pd

dic = {"a" : 1, "b" : 2, "c" : 3}
pd.Series(dic)

->
a    1
b    2
c    3
dtype: int64
```

<br>

### 리스트를 사용해서 시리즈 만들기

```python
box = ['홍길동', '이순신', '아이유']
s = pd.Series(box, index=['가','나','다']) 
pd.Series(box, index=['가','나','다']) 

->
가    홍길동
나    이순신
다    아이유
dtype: object

box = [['홍길동', '남자', 40], ['이순신', '남자', 50], ['아이유', '여자', 20]]
pd.DataFrame(box, columns = ['이름', '성별', '나이'])
# 자료형 확인
type(s)
# 시리즈 행이름 확인
s.index
# 시리즈 값 확인
s.values
```

<br>

### 딕셔너리로 데이터프레임 만들기

```python
dic = {"이름" : ['홍길동', '이순신', '아이유'],
			"성별" : ['남자', '남자', '여자'],
			"나이" : [40, 50, 20]}

df = pd.DataFrame(dic, index = ['A', 'B', 'C'], columns = ['성별', '나이', '이름'])
# 데이터 프레임 행 이름 확인
df.index
```