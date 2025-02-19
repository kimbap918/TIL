

## 파이썬 벽 부수고 이동하기(BOJ 2206)

<br>

## 문제

N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다. 최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.

만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.

한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.

맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.

<br>

## 입력

첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다. 다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.

<br>

## 출력

첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.

<br>

## 예제 입력 1 

```
6 4
0100
1110
1000
0000
0111
0000
```

## 예제 출력 1 

```
15
```

## 예제 입력 2 

```
4 4
0111
1111
1111
1110
```

## 예제 출력 2 

```
-1
```

<br>

## 📝 풀어보기 

N(세로), M(가로)길이를 입력받는다.

숫자로 된 맵을 N줄에 걸쳐서 입력받아 graph에 저장한다.

visited에 [0]*2 를 M개만큼, N줄에 걸쳐서 저장한다.

visited가 이렇게 3차원 형태의 리스트가 되는 이유는 벽을 부수고 이동하기 위한 카운트 때문이다.

`visited[x][y][0]`에는 해당 좌표의 방문 여부를, `visited[x][y][1]`에는 남은 벽 부수기 카운트를 저장한다.

dx, dy에는 앞, 뒤, 좌, 우 4가지 방위를 체크하기 위한 값을 넣어둔다.

``` python
import sys
from collections import deque
from pprint import pprint
input = sys.stdin.readline


N, M = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
```

<br>

함수 BFS를 정의한다. 인자는 시작지점의 좌표 x, y와 블럭을 부술 수 있는 카운트 cnt다.

deque Q에 시작점의 좌표와 카운트를 삽입하고, 해당 지점을 방문처리한다.

Q에서 좌표와 카운트를 꺼내, x, y, cnt에 각각 저장한다.

만약 x와 y가 graph의 목표 좌표에 도달하면 `visited[x][y][cnt]`를 리턴해준다.

앞, 뒤, 좌, 우를 탐색하면서 해당 범위를 넘으면 건너뛴다.

그래프의 방문하지 않은 좌표가 있고, 벽을 부수지 않고 이동해도 되는 좌표가 있으면 Q에 해당 좌표값과 카운트를 집어넣고 visited의 해당 좌표에 이전 값 +1을 저장한다.

그래프의 이동경로에 벽이 있고(1) 카운트가 남아있다면 해당 좌표와 카운트를 -1 한 값을 Q에 저장한다.

해당위치와 cnt-1에 이전 값 +1을 저장한다.

그외엔 이동할 수 없으므로 -1을 리턴한다.  

``` python
# 시작지점의 좌표 x, y, cnt
def BFS(x, y, cnt):
    Q = deque([[x, y, cnt]])
    visited[x][y][cnt] = 1
    while Q:
        x, y, cnt = Q.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y][cnt]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            # 벽을 부수지 않고 이동하기
            if graph[nx][ny] == 0 and visited[nx][ny][cnt] == 0:
                Q.append([nx, ny, cnt])
                visited[nx][ny][cnt] = visited[x][y][cnt] + 1
            # 벽을 부순다
            if graph[nx][ny] == 1 and cnt == 1:
                Q.append([nx, ny, cnt-1])
                visited[nx][ny][cnt-1] = visited[x][y][cnt] + 1
    return -1


```

<br>

#### 전체코드

``` python
import sys
from collections import deque
from pprint import pprint
input = sys.stdin.readline


N, M = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 시작지점의 좌표 x, y, cnt
def BFS(x, y, cnt):
    Q = deque([[0, 0, 1]])
    visited[x][y][cnt] = 1
    while Q:
        x, y, cnt = Q.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y][cnt]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            # 벽을 부수지 않고 이동하기
            if graph[nx][ny] == 0 and visited[nx][ny][cnt] == 0:
                Q.append([nx, ny, cnt])
                visited[nx][ny][cnt] = visited[x][y][cnt] + 1
            # 벽을 부순다
            if graph[nx][ny] == 1 and cnt == 1:
                Q.append([nx, ny, cnt-1])
                visited[nx][ny][cnt-1] = visited[x][y][cnt] + 1
    return -1

# 시작지점 x,y좌표와 남은 카운트 1
print(BFS(0, 0, 1))
```

<br>



