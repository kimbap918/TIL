## 파이썬 통계학(백준 BOJ 2108)

<br>

> from collections import Counter

## 문제

수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.

1. 산술평균 : N개의 수들의 합을 N으로 나눈 값
2. 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
3. 최빈값 : N개의 수들 중 가장 많이 나타나는 값
4. 범위 : N개의 수들 중 최댓값과 최솟값의 차이

N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

<br>

## 입력

첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 단, N은 홀수이다. 그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.

<br>

## 출력

첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.

둘째 줄에는 중앙값을 출력한다.

셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.

넷째 줄에는 범위를 출력한다.

<br>

## 예제 입력 1 

```
5
1
3
8
-2
2
```

## 예제 출력 1 

```
2
2
1
10
```

## 예제 입력 2 

```
1
4000
```

## 예제 출력 2 

```
4000
4000
4000
0
```

## 예제 입력 3 

```
5
-1
-2
-3
-1
-2
```

## 예제 출력 3 

```
-2
-2
-1
2
```

## 예제 입력 4 

```
3
0
0
-1
```

## 예제 출력 4 

```
0
0
0
1
```

(0 + 0 + (-1)) / 3 = -0.333333... 이고 이를 첫째 자리에서 반올림하면 0이다. -0으로 출력하면 안된다.

<br>

## 📝 풀어보기

📌 `floor` 함수를 사용하기 위해 `math`, 시간초과 방지를 위해 `sys`, 최빈값을 사용하기위한 `Counter` 라이브러리를 사용했다.

수의 개수 `N`을 입력받고 N개의 수를 담기위한 리스트 a를 생성한다.

``` python
import math
import sys
from collections import Counter

input = sys.stdin.readline
N = int(input())
a = [] 
```

<br>

📌 N만큼 반복하면서 a에 수를 입력받고 a를 정렬한다. 

첫번째로, a의 합을 N으로 나눈 후 소숫점 첫째자리를 반올림하여 int로 형변환한 산술평균을 출력한다.

두번째로, N을 2로 나누고 소숫점을 버림한 값이 리스트의 중앙에 위치한 값이므로 중앙값을 출력한다.

세번째로, Counter를 사용해서 최빈값의 횟수와 수를 튜플 형태로 받아낸다. 튜플의 첫번째 요소와 그 다음 요소가 같다면(최빈값의 횟수가 같다면) 두번째로 작은값을 출력하고 그 외엔 최빈값을 출력한다.

네번째로, a 내의 최대값과 최소값의 차이인 범위를 출력한다 .

``` python
for i in range(N):
    a.append(int(input()))
a.sort()
print(int(round((sum(a)/N), 0))) # 1. 산술평균

print(a[math.floor(N/2)]) # 2. 중앙값

cnt_a = Counter(a).most_common()
if len(cnt_a) > 1 and cnt_a[0][1] == cnt_a[1][1]: # 최빈값이 2개 이상이면
    print(cnt_a[1][0]) # 3. 최빈값
else:
    print(cnt_a[0][0]) 

print(max(a) - min(a)) # 4. 범위
```

<br>

#### 전체코드

``` python
import math
import sys
from collections import Counter

input = sys.stdin.readline
N = int(input())
a = [] 

for i in range(N):
    a.append(int(input()))
a.sort()
print(int(round((sum(a)/N), 0))) # 1. 산술평균

print(a[math.floor(N/2)]) # 2. 중앙값

cnt_a = Counter(a).most_common()
if len(cnt_a) > 1 and cnt_a[0][1] == cnt_a[1][1]: # 최빈값이 2개 이상이면
    print(cnt_a[1][0]) # 3. 최빈값
else:
    print(cnt_a[0][0]) 

print(max(a) - min(a)) # 4. 범위
```

