## 파이썬 최소힙(백준 BOJ 1927)

<br>

## 문제

널리 잘 알려진 자료구조 중 최소 힙이 있다. 최소 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.

1. 배열에 자연수 x를 넣는다.
2. 배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.

프로그램은 처음에 비어있는 배열에서 시작하게 된다.

<br>

## 입력

첫째 줄에 연산의 개수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다. 만약 x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산이고, x가 0이라면 배열에서 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우이다. x는 231보다 작은 자연수 또는 0이고, 음의 정수는 입력으로 주어지지 않는다.

<br>

## 출력

입력에서 0이 주어진 횟수만큼 답을 출력한다. 만약 배열이 비어 있는 경우인데 가장 작은 값을 출력하라고 한 경우에는 0을 출력하면 된다.

<br>

## 예제 입력 1

```
9
0
12345678
1
2
0
0
0
0
32
```

## 예제 출력 1

```
0
1
2
12345678
0
```

<br>

## 📝 풀어보기

📌 먼저 heap관련 라이브러리를 사용하기 위해 `heapq` 를 import하고 연산의 개수가 많으므로 `sys` 를 import하여 readline을 사용한다.

``` python
import heapq
import sys
input = sys.stdin.readline
```

<br>

📌 연산의 개수를 입력할 N과 리스트를 생성한다. 

``` python
N = int(input())
heap = []
```

<br>

📌 N만큼 for문을 돌면서 연산에 대한 정보를 입력받는다.

입력한 값이 0이 아닐 경우에 `heappush` 로 리스트 heap에 n값을 넣고 n이 아닌 경우에는 heap의 길이가 0인경우 0을 출력하고 그외엔 heap의 값을 꺼내며 출력한다.

``` python
for i in range(N):
    n = int(input())
    if n != 0:
        heapq.heappush(heap, n)
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
```

<br>

#### 전체코드

``` python
#9
#0 -> 0이면 가장 작은값 출력하고 제거(heapq.heappop)
#12345678 -> 자연수인 경우 추가(heapq.heappush)
#1
#2
#.. 생략
import heapq
import sys
input = sys.stdin.readline

N = int(input())
heap = []

for i in range(N):
    n = int(input())
    if n != 0:
        heapq.heappush(heap, n)
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
```

