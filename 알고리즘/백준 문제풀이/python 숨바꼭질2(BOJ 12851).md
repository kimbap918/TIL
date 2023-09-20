

## 파이썬 숨바꼭질2(BOJ 12851)

<br>

## 문제

수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 그리고, 가장 빠른 시간으로 찾는 방법이 몇 가지 인지 구하는 프로그램을 작성하시오.

<br>

## 입력

첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

<br>

## 출력

첫째 줄에 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

둘째 줄에는 가장 빠른 시간으로 수빈이가 동생을 찾는 방법의 수를 출력한다.

<br>

## 예제 입력 1 

```
5 17
```

## 예제 출력 1

```
4
2
```

<br>

## 📝 풀어보기 

숨바꼭질(BOJ 1697)에서 수빈이가 동생을 찾는 방법의 수 까지 계산하여 출력하는 문제다.

수빈이의 위치가 동생의 위치와 같아졌을 때(x==K) 바로 시간을 반환하지 않고 nx가 범위 내에 있을 때,

해당 위치에 도착한 시간이 0이거나 arr[nx] == arr[x]+1일때 값을 추가하도록 조건문을 변경했다.

#### 전체코드

``` python
import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
MAX = 100001
arr = [0] * MAX
cnt_ans = 0
cnt_way = 0

def BFS(v):
    global cnt_ans
    global cnt_way

    Q = deque([v])

    while Q:
        x = Q.popleft()
        count = arr[x]

        if x == K:
            cnt_way += 1
            cnt_ans = count 
            continue

        # X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
        # 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.
        # 기존 위치에서 이동하는 위치는 3가지
        for nx in (x-1, x+1, x*2):
            # x-1, x+1 x*2이 범위를 벗어나면 안된다.
            if 0 <= nx < MAX:
                if arr[nx] == 0 or arr[nx] == arr[x]+1:
                    arr[nx] = count + 1
                    Q.append(nx)

BFS(N)
print(cnt_ans)
print(cnt_way)
```

