

## 파이썬 단지번호붙이기(BOJ 2667)

<br>

## 문제

<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

![img](https://www.acmicpc.net/upload/images/ITVH9w1Gf6eCRdThfkegBUSOKd.png)

## 입력

첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

<br>

## 출력

첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

<br>

## 예제 입력 1

```
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
```

## 예제 출력 1 

```
3
7
8
9
```

<br>

## 📝 풀어보기 

BFS로 풀었다.

<br>

BFS로 풀기 위해 deque를 import했다.

입력된 값이 잘 들어갔는지 확인하기 위해 pprint를 import했다.

dx, dy는 탐색하는 현 지점에서 위, 아래 좌, 우 4방위를 살펴보기 위해 저장해두는 좌표다.

``` python
from collections import deque
from pprint import pprint
import sys
input = sys.stdin.readline

# 탐색 좌표
# 위, 아래, 우, 좌
# (0, 1), (0, -1), (1, 0), (-1, 0)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
```

<br>

지도의 크기 N을 입력받는다.

graph에 N줄에 해당하는 단지의 자료를 담는다.

graph의 가로, 세로 전부를 순회하면서 순회하는 영역이 1일 경우에 BFS를 수행한 값을 cnt에 담을것이다.

```python
N = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
# pprint(graph)

cnt = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            cnt.append(bfs(graph, i, j))
```

<br>

BFS를 구현한다.

BFS의 구현 방법은 이전의 너비 우선 탐색(BOJ 24444)과 방법이 거의 같다.

그래프와, 그래프의 좌표(a,b)가 들어오면 deque에 좌표를 담고, while문에서 좌표를 꺼내 4방위를 탐색한다.

여기서 좌표가 그래프의 범위를 벗어나면 안되므로 조건문을 건다.

탐색하는 좌표가 1이라면 `graph[nx][ny]`를 0으로 바꾸고, deque에 nx, ny값을 담고 카운트를 1 증가시킨다.

```python
def bfs(graph, a, b):
    length = len(graph)
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= length or ny < 0 or ny >= length:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count
```

<br>

카운트를 정렬하고, 총 단지 수와 단지 내 집 수를 출력한다.

```python
# 오름차순 정렬
cnt.sort()
# 총 단지 수 출력
print(len(cnt))
# 단지 내 집 수 출력
for i in range(len(cnt)):
    print(cnt[i])
```

<br>

#### 전체코드

``` python
from collections import deque
from pprint import pprint
import sys
input = sys.stdin.readline

# 탐색 좌표
# 위, 아래, 우, 좌
# (0, 1), (0, -1), (1, 0), (-1, 0)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(graph, a, b):
    length = len(graph)
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= length or ny < 0 or ny >= length:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count


N = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
# pprint(graph)

cnt = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            cnt.append(bfs(graph, i, j))

# 오름차순 정렬
cnt.sort()
# 총 단지 수 출력
print(len(cnt))
# 단지 내 집 수 출력
for i in range(len(cnt)):
    print(cnt[i])
```

