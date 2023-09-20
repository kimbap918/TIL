## SeSAC - Pandas(2) 판다스 통계 함수

<br>

### Groupby 함수

판다스에서 제공하는 데이터프레임을 집단별로 나누어주는 함수, 각 집단별로 통계값을 구할 때 유용하게 사용 가능하다.

| 통계 함수 | 설명 |
| --- | --- |
| count | 누락값을 제외한 데이터 수 |
| size | 누락값을 포함한 데이터 수 |
| mean | 평균 |
| std | 표준편차 |
| min | 최소값 |
| max | 최대값 |
| sum | 전체값 |
| var | 분산 |
| describe | 요약 통계량 |
| first | 첫번째 행 |
| last | 마지막 행 |

```python
import pandas as pd

df = pd.read_csv("gapminder.tsv", sep='\t')
df
```

|  | country | continent | year | lifeExp | pop | gdpPercap |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | Afghanistan | Asia | 1952 | 28.801 | 8425333 | 779.445314 |
| 1 | Afghanistan | Asia | 1957 | 30.332 | 9240934 | 820.853030 |
| 2 | Afghanistan | Asia | 1962 | 31.997 | 10267083 | 853.100710 |
| 3 | Afghanistan | Asia | 1967 | 34.020 | 11537966 | 836.197138 |
| 4 | Afghanistan | Asia | 1972 | 36.088 | 13079460 | 739.981106 |
| ... | ... | ... | ... | ... | ... | ... |
| 1699 | Zimbabwe | Africa | 1987 | 62.351 | 9216418 | 706.157306 |
| 1700 | Zimbabwe | Africa | 1992 | 60.377 | 10704340 | 693.420786 |
| 1701 | Zimbabwe | Africa | 1997 | 46.809 | 11404948 | 792.449960 |
| 1702 | Zimbabwe | Africa | 2002 | 39.989 | 11926563 | 672.038623 |
| 1703 | Zimbabwe | Africa | 2007 | 43.487 | 12311143 | 469.709298 |

```python
# 연도별 수명의 평균
df.groupby("year")["lifeExp"].mean()
```

```
year
1952    49.057620
1957    51.507401
1962    53.609249
1967    55.678290
1972    57.647386
1977    59.570157
1982    61.533197
1987    63.212613
1992    64.160338
1997    65.014676
2002    65.694923
2007    67.007423
Name: lifeExp, dtype: float64
```

```python
# 중복을 허용하지 않은 데이터의 고유한 개수
result = df.groupby("continent")["country"].nunique()
result
```

```
continent
Africa      52
Americas    25
Asia        33
Europe      30
Oceania      2
Name: country, dtype: int64
```

```python
# 그래프로 나타내기
result.plot()
```

![Untitled](https://github.com/kimbap918/TIL/assets/75712723/f5c970d8-e1ce-40d2-8f9e-0584259b2410)