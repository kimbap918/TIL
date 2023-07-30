## SeSAC - 데이터프레임 누락값 처리

<br>

### 누락값

- 비어있는 값
- 누락값이 하나라도 있으면 데이터분석 및 연산이 원활하지 못할 수 있다.
- 누락값은 비교할 수 없다. 단, pd.isnull() 함수로 누락값인지 아닌지 판단 가능하다.

```python
pd.isnull() # 누락값이면 True, 아니면 False 반환
pd.notnull() # 누락값이 아니면 True, 누락값이면 False 반환
```

<br>

### 누락값 개수 구하기

```python
np.count_nonzero(데이터.isnull())
df['Cases_Guinea'].value_counts(dropna=False)
```

<br>

### 누락값 채우기

```python
fillna(값)
fillna(method = 'ffill') # 바로 앞에 있는 값으로 채우는 방법
fillna(method = 'bfill') # 바로 뒤에 있는 값으로 채우는 방법
df.interpolate() # 흐름에 따라서 결측치를 채우는 방법
# 예를들어 2 NaN NaN 8 이라면 흐름을 파악해 2 4 6 8로 채운다
```