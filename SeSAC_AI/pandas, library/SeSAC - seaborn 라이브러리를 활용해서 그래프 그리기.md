## SeSAC - seaborn 라이브러리를 활용해서 그래프 그리기

<br>

- seaborn과 matplotlib은 연동이 가능하다.

```python
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1 = sns.histplot(tips['total_bill'])
```

<br>

### 히스토그램

```python
sns.histplot(데이터, bins=막대기개수) # 단변량
```

<br>

### 밀도 함수 그래프

```python
sns.kdeplot(데이터) # 단변량
sns.kdeplot(x = 데이터1, y = 데이터2) # 다변량
```

<br>

### 특정 값 개수 그래프

```python
sns.countplot(데이터)
```

<br>

### 산점도

```python
# x = 열이름 
# data = 데이터 출처
sns.lmplot(x='total_bill', y='tip', data=tips) # 다변량 그래프
```

<br>

### 산점도 + 히스토그램

```python
sns.jointplot(x='total_bill', y='tip', data=tips)
```

<br>

### 평균 막대그래프

```python
sns.barplot(x='time', y='total_bill', data=tips) # 다변량 그래프
```

<br>

### 상자 그래프

```python
sns.boxplot(x='time', y='total_bill', data=tips)
```

<br>

### 바이올린 그래프

```python
sns.violinplot(x='time', y='total_bill', data=tips)
```

<br>

### 관계 그래프

```python
sns.pairplot(tips)
```

<br>

### 다변량 그래프 그리기

- 히스토그램, 밀도 함수 그래프 등에서 특성을 하나만 표시하고 있는 그래프를 단변량(일변량) 그래프라고 한다.

```python
# 매개변수 hue : 색상 추가
# 매개변수 col : 집단 별로 그래프 그리기
# FacetGrid : 집단별로 그래프 그리는 함수
```

<br>

### 그래프 배경 설정

```python
sns.set_style(배경)
```

<br>

## 실습 해보기

<br>

### pandas, seaborn 라이브러리 import

```python
import pandas as pd
import seaborn as sns
```

<br>

### seaborn라이브러리 내의 식당 데이터 load

```python
tips = sns.load_dataset("tips")
tips
```

|  | total_bill | tip | sex | smoker | day | time | size |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 16.99 | 1.01 | Female | No | Sun | Dinner | 2 |
| 1 | 10.34 | 1.66 | Male | No | Sun | Dinner | 3 |
| 2 | 21.01 | 3.50 | Male | No | Sun | Dinner | 3 |
| 3 | 23.68 | 3.31 | Male | No | Sun | Dinner | 2 |
| 4 | 24.59 | 3.61 | Female | No | Sun | Dinner | 4 |
| ... | ... | ... | ... | ... | ... | ... | ... |
| 239 | 29.03 | 5.92 | Male | No | Sat | Dinner | 3 |
| 240 | 27.18 | 2.00 | Female | Yes | Sat | Dinner | 2 |
| 241 | 22.67 | 2.00 | Male | Yes | Sat | Dinner | 2 |
| 242 | 17.82 | 1.75 | Male | No | Sat | Dinner | 2 |
| 243 | 18.78 | 3.00 | Female | No | Thur | Dinner | 2 |

<br>

### 그래프 그려보기

- 히스토그램

```python
sns.histplot(tips['total_bill'])
```

![Untitled (13)](https://github.com/kimbap918/TIL/assets/75712723/37b2c59e-4624-45a8-ac0a-797c44c1d6ba)

- 밀도 함수 그래프(단변량)

```python
sns.kdeplot(tips['total_bill'])
```

![Untitled (14)](https://github.com/kimbap918/TIL/assets/75712723/fbd0adcf-824d-458f-b9d9-940f3c11d299)

- 밀도 함수 그래프(다변량)

```python
sns.kdeplot(x = tips['total_bill'], y = tips['tip'], shade=True)
```

![Untitled (15)](https://github.com/kimbap918/TIL/assets/75712723/a2f0f9b7-bec3-4420-939a-3d8df659c9e6)

- 산점도

```python
sns.lmplot(x='total_bill', y='tip', data=tips)
```

![Untitled (16)](https://github.com/kimbap918/TIL/assets/75712723/66dcc7e5-8d84-4413-b55c-d57bae7e978e)

- 산점도 + 히스토그램

```python
sns.jointplot(x='total_bill', y='tip', data=tips, kind='hex')
```

![Untitled (17)](https://github.com/kimbap918/TIL/assets/75712723/2d44519d-884c-45cf-8087-d10e4b6d0fc5)

- 상자 그래프

```python
sns.boxplot(x='day', y='total_bill', data=tips)
```

![Untitled (18)](https://github.com/kimbap918/TIL/assets/75712723/0dba5c90-705e-4e00-b915-59412cb93658)

- 바이올린 그래프

```python
sns.violinplot(x='sex', y='total_bill', data=tips)
```

![Untitled (19)](https://github.com/kimbap918/TIL/assets/75712723/bb3fd177-9850-4159-89db-d6801d8c0ec1)

- 관계 그래프

```python
# hue로 색상 추가
sns.pairplot(tips, hue='sex')
```

![Untitled (20)](https://github.com/kimbap918/TIL/assets/75712723/cb368498-18ea-4e24-8b40-7a42cebd2313)