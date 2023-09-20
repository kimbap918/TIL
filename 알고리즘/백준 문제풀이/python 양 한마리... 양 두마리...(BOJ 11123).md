

## 파이썬 양 한마리... 양 두마리...(BOJ 11123)

<br>

## 문제

얼마전에 나는 불면증에 시달렸지... 천장이 뚫어져라 뜬 눈으로 밤을 지새우곤 했었지.  그러던 어느 날 내 친구 광민이에게 나의 불면증에 대해 말했더니 이렇게 말하더군. "양이라도 세봐!"  정말 도움이 안되는 친구라고 생각했었지. 그런데 막상 또 다시 잠을 청해보려고 침대에 눕고 보니 양을 세고 있더군... 그런데 양을 세다보니 이걸로 프로그램을 하나 짜볼 수 있겠단 생각이 들더군 후후후... 그렇게 나는 침대에서 일어나 컴퓨터 앞으로 향했지.

*양을 # 으로 나타내고 . 으로 풀을 표현하는 거야. 서로 다른 # 두 개 이상이 붙어있다면 한 무리의 양들이 있는거지. 그래... 좋았어..! 이걸로 초원에서 풀을 뜯고 있는 양들을 그리드로 표현해 보는거야!*

그렇게 나는 양들을 그리드로 표현하고 나니까 갑자기 졸렵기 시작했어. 하지만 난 너무 궁금했지. 내가 표현한 그 그리드 위에 몇 개의 양무리가 있었는지! 그래서 나는 동이 트기 전까지 이 프로그램을 작성하고 장렬히 전사했지. 다음날 내가 잠에서 깨어났을 때 내 모니터에는 몇 개의 양무리가 있었는지 출력되어 있었지.

<br>

## 입력

첫 번째 줄은 테스트 케이스의 수를 나타나는 T를 입력받는다.

이후 각 테스트 케이스의 첫 번째 줄에서는 H,W 를 입력받는다. H는 그리드의 높이이고, W는 그리드의 너비이다. 이후 그리드의 높이 H 에 걸쳐서 W개의 문자로 이루어진 문자열 하나를 입력받는다. 

- 0 < T ≤ 100
- 0 < H, W ≤ 100

<br>

## 출력

각 테스트 케이스마다, 양의 몇 개의 무리로 이루어져 있었는지를 한 줄에 출력하면 된다. 

<br>

## 예제 입력 1

```
2
4 4
#.#.
.#.#
#.##
.#.#
3 5
###.#
..#..
#.###
```

## 예제 출력 1 

```
6
3
```

<br>

## 📝 풀어보기 

DFS, BFS 두가지로 모두 풀이해보았다.

<br>

테스트 케이스 T를 입력받는다.

상하좌우 4방위 탐색을 위해 dx, dy에 좌표값을 저장해둔다.

```python
from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
```

<br>

테스트 케이스 수만큼 반복하면서 양의 무리 수를 셀 cnt, 그리드의 높이 H, 너비 W, 방문여부를 확인할 visited, 그리드의 상태를 graph에 입력받는다.

그리드의 너비 높이만큼 탐색하면서 양(#)을 발견했고, 아직 방문하지 않았다면 방문처리를 하고 BFS를 수행한다. BFS수행 후 양의 무리를 발견했으므로 카운트를 증가시킨다.

``` python
for _ in range(T):
    cnt = 0
    H, W = map(int, input().split())
    visited = [[False] * W for _ in range(H)]
    graph = [list(input().rstrip()) for _ in range(H)]

    for i in range(H):
        for j in range(W):
            if graph[i][j] == '#' and not visited[i][j]:
                visited[i][j] = True
                BFS(i, j)
                cnt += 1
```

<br>

함수 BFS를 정의한다. 

deque Q에 함수를 실행할때 받은 인자 [높이, 너비]를 저장하고 값을 꺼내어 y, x에  저장한다.

상하좌우 4방위를 탐색하면서 탐색범위가 그리드를 벗어나지 않고, 탐색범위에 양이 있으며, 방문하지 않았다면 방문처리를 하고 Q에 해당 좌표를 삽입한다. 이 과정을 반복하고 반복이 종료되면 카운트를 출력한다.

``` python
def BFS(h, w):
    global cnt
    Q = deque([[h, w]])

    while Q:
        y, x = Q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nx < W and 0 <= ny < H and graph[ny][nx] == '#' and not visited[ny][nx]:
                visited[ny][nx] = True
                Q.append([ny, nx])
```

<br>

#### BFS 전체코드

``` python
from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def BFS(h, w):
    global cnt
    Q = deque([[h, w]])

    while Q:
        y, x = Q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nx < W and 0 <= ny < H and graph[ny][nx] == '#' and not visited[ny][nx]:
                visited[ny][nx] = True
                Q.append([ny, nx])


for _ in range(T):
    cnt = 0
    H, W = map(int, input().split())
    visited = [[False] * W for _ in range(H)]
    graph = [list(input().rstrip()) for _ in range(H)]

    for i in range(H):
        for j in range(W):
            if graph[i][j] == '#' and not visited[i][j]:
                visited[i][j] = True
                BFS(i, j)
                cnt += 1
    print(cnt)
```

<br>

#### DFS

<br>

테스트 케이스 T를 입력받는다.

상하좌우 4방위 탐색을 위해 dx, dy에 좌표값을 저장해둔다.

```python
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = int(input())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
```

<br>

테스트 케이스 수만큼 반복하면서 양의 무리 수를 셀 cnt, 그리드의 높이 H, 너비 W, 방문여부를 확인할 visited, 그리드의 상태를 graph에 입력받는다.

그리드의 너비 높이만큼 탐색하면서 양(#)을 발견했고, 아직 방문하지 않았다면 방문처리를 하고 DFS를 수행한다. DFS수행 후 양의 무리를 발견했으므로 카운트를 증가시킨다.

``` python
for _ in range(T):
    cnt = 0
    H, W = map(int, input().split())
    visited = [[False] * W for _ in range(H)]
    graph = [list(input().rstrip()) for _ in range(H)]

    for i in range(H):
        for j in range(W):
            if graph[i][j] == '#' and not visited[i][j]:
                DFS(i, j)
                cnt += 1
    print(cnt)
```

<br>

함수 DFS를 정의한다. 

함수 실행시 들어온 인자값에 해당하는 visited의 좌표를 방문처리하고 4방위를 탐색한다.

방문하는 곳의 좌표가 범위 내에 있고, 양(#)이 있으며, 방문하지 않았다면 해당 좌표를 인자로 해서 재귀적으로 DFS를 수행한다.

반복이 종료된 후 cnt를 출력한다.

``` python
def DFS(h, w):
    visited[h][w] = True

    for i in range(4):
        ny = h + dy[i]
        nx = w + dx[i]
        if 0 <= nx < W and 0 <= ny < H and graph[ny][nx] == '#' and not visited[ny][nx]:
            DFS(ny, nx)
```

<br>

#### DFS 전체코드

```python
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = int(input())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def DFS(h, w):
    visited[h][w] = True

    for i in range(4):
        ny = h + dy[i]
        nx = w + dx[i]
        if 0 <= nx < W and 0 <= ny < H and graph[ny][nx] == '#' and not visited[ny][nx]:
            DFS(ny, nx)

for _ in range(T):
    cnt = 0
    H, W = map(int, input().split())
    visited = [[False] * W for _ in range(H)]
    graph = [list(input().rstrip()) for _ in range(H)]

    for i in range(H):
        for j in range(W):
            if graph[i][j] == '#' and not visited[i][j]:
                DFS(i, j)
                cnt += 1
    print(cnt)

```

