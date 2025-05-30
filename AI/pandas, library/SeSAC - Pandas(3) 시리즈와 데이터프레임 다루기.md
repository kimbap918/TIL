## SeSAC - Pandas(3) 시리즈와 데이터프레임 다루기

<br>

### 데이터프레임에서 열에 접근하기

```python
df[열]
df[[열1, 열2]]
```

<br>

### 데이터프레임에서 행, 열에 접근하기

- loc : 이름으로 접근
- iloc : 순서로 접근

```python
loc[0]
# 0 10 100 1000이라고 적힌 행에 접근
loc[[0, 10, 100, 1000]]

iloc[0]
# 0 10 100 1000번째 행에 접근
iloc[[0, 10, 100, 1000]]
```

<br>

### 데이터프레임에서 내가 원하는 행만 추출하기

```python
df[조건]
df[(조건1) & (조건2)]
df[(조건1) | (조건2)]

# 예시
df[['이름', '나이', '직업']]
# 직업이 연구원이거나 나이가 나이의 평균보다 큰 값
df[(df['직업'] == '연구원') | (df['나이'] > df['나이'].mean())]
```

<br>

### 데이터프레임의 머리 부분 추출

```python
# 데이터프레임의 앞의 일부분만 출력해서 보여준다
df.head()
# 보여주는 개수를 조절할 수 있다
df.head(n=10)
```

<br>

### 데이터프레임의 꼬리 부분 추출

```python
# 데이터프레임의 뒤의 일부분만 출력해서 
df.tail()
df.tail(n=10)
```

<br>

### 데이터프레임의 모양 확인

```python
df.shape()
```

<br>

### 데이터프레임의 열 자료형 확인

```python
df.dtypes
```

<br>

### 데이터프레임의 정보 확인

```python
df.info()
```

<br>

### 시리즈 통계 함수

```python
s.mean() # 평균
s.std() # 표준편차
s.median() # 중앙값
s.describe() # 기초 통계량
s.max() # 최댓값
s.min() # 최솟값
```

<br>

### 시리즈 중복데이터 삭제

```python
s.drop_duplicates()
df.drop_duplicates()
```

<br>

### 시리즈 특정 값 바꾸기

```python
s.replace(값, 변경값)
```

<br>

### 시리즈 랜덤 샘플 추출

```python
s.sample(n)
```

<br>

### 정렬하기

```python
s.sort_values()
s.sort_values(ascending=False)

# 행 번호
s.sort_index()
s.sort_index(ascending=False)
```

<br>

### 시리즈 프레임화

```python
s.to_frame()
```

<br>

### 시간 데이터 변환

```python
# 문자열로 된 날짜 데이터를 시간 데이터로 변환
pd.to_datetime()

# 예시
pd.to_datetime(df['출생일'])
df['출생일'] = pd.to_datetime(df['출생일'])
```
