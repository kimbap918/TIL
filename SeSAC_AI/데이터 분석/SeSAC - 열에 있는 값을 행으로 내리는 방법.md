## SeSAC - 열에 있는 값을 행으로 내리는 방법,  행에 있는 값을 열로 올리는 방법

<br>

### melt

- 지정한 열의 데이터를 모두 행으로 내려주는 기능

```python
pd.melt(df, id_vars= ...)
# 예시
pd2 = pd.melt(dfm id_vars = ['religion'], varnames='income', value_names='count')

id_vars # 고정할 열
var_name # 위치를 변경할 열의 이름
value_name # 위치를 변경한 열의 데이터를 저장한 열의 이름
```

<br>

### 열 분할하기

```python
# 분할
시리즈.str.split(기준)
# 예시
ebola_split = ebola2['variable'].str.split("_")
 
# 수집
시리즈.str[인덱스]
# 예시
ebola2['State'] = state
```

<br>

### pivot_table

- melt와는 반대로 행에 있는 값을 열로 올려서 새로운 열을 만드는 기능

```python
df.pivot_table(
index = 고정하고싶은열,
columns = 열로 올리고싶은 열,
values = 새로 올라간 열이 가지게 될 값,
dropna = True/False
)

# 예시
weather2.pivot_table(index = ['id', 'year', 'month', 'day'], 
columns='element', value_name='temp', dropna=False)
```

<br>

### 인덱스 새롭게 다시 만들기

```python
df.reset_index()

# 예시
weather4 = weather3.reset_index()
```