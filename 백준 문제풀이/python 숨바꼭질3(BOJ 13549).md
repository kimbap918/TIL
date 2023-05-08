

## 파이썬 숨바꼭질3(BOJ 13549)

<br>

## 문제

수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

<br>

## 입력

첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

<br>

## 출력

수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

<br>

## 예제 입력 1 

```
5 17
```

## 예제 출력 1 

```
2
```

<br>

## 힌트

수빈이가 5-10-9-18-17 순으로 가면 2초만에 동생을 찾을 수 있다.

<br>

## 📝 풀어보기 

숨바꼭질2(BOJ 12851)에서 걸어서 이동할때와 순간이동할때의 가중치가 다르다.

푸는 방법이 데이크스트라와 BFS가 있어서 두 가지 방법으로 풀었다.

<br>

#### 데이크스트라(Dijkstra)

``` python
import sys
import math
from heapq import heappush, heappop
input = sys.stdin.readline
INF = math.inf

# 걸어서 갈 때와 순간이동으로 갈 때의 가중치가 다르므로 다익스트라 알고리즘을 사용
N, K = map(int, input().split())
MAX = 100001
dist = [INF] * MAX
heap = []

def dijkstra(n, k):
    if k <= n:
        print(n-k)
        return
    
    heappush(heap, [0, n])
    while heap:
        w, x = heappop(heap)
        for nx in (x+1, x-1, x*2):
            if 0 <= nx < MAX:
                # 순간 이동은 0초, 걸어서 갈땐 1초
                if nx == x*2 and dist[nx] == INF:
                    dist[nx] = w
                    heappush(heap, [w, nx])
                elif dist[nx] == INF:
                    dist[nx] = w + 1
                    heappush(heap, [w+1, nx])
    print(dist[k])

dijkstra(N, K)
```

<br>

#### BFS

```python
import sys
from collections import deque
input = sys.stdin.readline
visited = [0] * MAX

def BFS(v):
    Q = deque([v])
    while Q:
        x = Q.popleft()
        if x == K:
            return visited[x]
        for nx in (x+1, x-1, x*2):
            if 0 <= nx < MAX and not visited[nx]:
                # 순간이동은 0초, 걸어서 갈땐 1초
                if nx == x*2:
                    visited[nx] = visited[x]
                    Q.append(nx)
                else:
                    visited[nx] = visited[x]+1
                    Q.append(nx)

print(BFS(N))
```

