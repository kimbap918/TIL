

## 파이썬 숨바꼭질4(BOJ 13913)

<br>

## 문제

수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

<br>

## 입력

첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

<br>

## 출력

첫째 줄에 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

둘째 줄에 어떻게 이동해야 하는지 공백으로 구분해 출력한다.

<br>

## 예제 입력 1 

```
5 17
```

## 예제 출력 1 

```
4
5 10 9 18 17
```

## 예제 입력 2 

```
5 17
```

## 예제 출력 2 

```
4
5 4 8 16 17
```

<br>

## 📝 풀어보기 

숨바꼭질(BOJ 1697)에서 동생을 찾는 시간과 함께 동생을 찾는 이동경로를 함께 출력하는 문제다.

이동 경로를 담을 배열을 만들어서 함수를 구현하고 거기에 이동 경로를 담았다.

#### 전체코드

``` python
import sys
from collections import deque
input = sys.stdin.readline

MAX = 100001
N, K = map(int, input().split())
visited = [0] * MAX
move = [0] * MAX
ans = []

def path(x):
    temp = x
    for _ in range(visited[x]+1):
        ans.append(temp)
        temp = move[temp]


def BFS(v):
    Q = deque([v])
    while Q:
        x = Q.popleft()
        if x == K:
            path(x)
            return visited[x]
        for nx in (x+1, x-1, x*2):
            if 0 <= nx < MAX and not visited[nx]:
                Q.append(nx)
                visited[nx] = visited[x]+1
                move[nx] = x

print(BFS(N))
print(*ans[::-1])
```

<br>



