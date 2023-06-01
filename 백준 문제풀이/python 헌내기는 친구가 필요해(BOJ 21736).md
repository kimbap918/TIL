

## 파이썬 양 한마리... 양 두마리...(BOJ 11123)

<br>

## 문제

2020년에 입학한 헌내기 도연이가 있다. 도연이는 비대면 수업 때문에 학교에 가지 못해 학교에 아는 친구가 없었다. 드디어 대면 수업을 하게 된 도연이는 어서 캠퍼스 내의 사람들과 친해지고 싶다. 

도연이가 다니는 대학의 캠퍼스는 N x M 크기이며 캠퍼스에서 이동하는 방법은 벽이 아닌 상하좌우로 이동하는 것이다. 예를 들어, 도연이가 (x, y)에 있다면 이동할 수 있는 곳은 (x+1, y), (x, y+1), (x-1, y), (x, y-1)이다. 단, 캠퍼스의 밖으로 이동할 수는 없다.

불쌍한 도연이를 위하여 캠퍼스에서 도연이가 만날 수 있는 사람의 수를 출력하는 프로그램을 작성해보자.

<br>

## 입력

첫째 줄에는 캠퍼스의 크기를 나타내는 두 정수 N(1 <= N <= 600), M(1 <= M <= 600)이 주어진다.

둘째 줄부터 N개의 줄에는 캠퍼스의 정보들이 주어진다. `O`는 빈 공간, `X`는 벽, `I`는 도연이, `P`는 사람이다. `I`가 한 번만 주어짐이 보장된다.

<br>

## 출력

첫째 줄에 도연이가 만날 수 있는 사람의 수를 출력한다. 단, 아무도 만나지 못한 경우 `TT`를 출력한다.

<br>

## 예제 입력 1 

```
3 5
OOOPO
OIOOX
OOOXP
```

## 예제 출력 1 

```
1
```

## 예제 입력 2 

```
3 3
IOX
OXP
XPP
```

## 예제 출력 2 

```
TT
```

<br>

## 📝 풀어보기

#### DFS

캠퍼스의 크기 N, M을 입력받는다. N은 세로, M은 가로다.

N개의 줄에 걸쳐서 캠퍼스의 정보를 받아 campus에 저장한다.

방문정보를 확인하기 위해 visited에 캠퍼스의 크기만큼 False를 저장해 둔다.

상,하,좌,우 방위탐색을 위해 dx, dy에 좌표를 넣고 학생의 수를 세기 위한 cnt에 0을 저장해둔다.

``` python
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
campus = [list(input().rstrip()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
cnt = 0
```

<br>

캠퍼스의 세로, 가로를 순회하면서 도연이(I)를 발견하고, 방문하지 않았으면 방문처리 후 DFS를 시작한다.

``` python
for i in range(N):
    for j in range(M):
        if campus[i][j] == "I" and not visited[i][j]:
            visited[i][j] = True
            DFS(i, j)
```

<br>

DFS를 정의한다.

상, 하, 좌, 우를 탐색하면서 먼저 탐색범위가 캠퍼스의 범위 내 인지 확인하고, 방문하지 않았으면 다음을 실행한다.

탐색지역이 벽(X)이면 건널수 없으므로 탐색하지 않고 건너뛴다.

탐색지역이 사람(P)이면 탐색 범위 내에서 사람을 찾았으므로 cnt를 1 증가시킨다.

그 외엔 방문하지 않았고, 범위를 벗어나지 않은 경우에 대해 방문처리를 하고 DFS를 수행한다.

``` python
def DFS(i, j):
    global cnt
    
    for k in range(4):
        nx = j + dx[k]
        ny = i + dy[k]

        if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx]:
            if campus[ny][nx] == "X":
                continue
            if campus[ny][nx] == "P":
                cnt += 1
            visited[ny][nx] = True
            DFS(ny, nx)
```

<br>

#### DFS 전체코드

```python
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
campus = [list(input().rstrip()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
cnt = 0

def DFS(i, j):
    global cnt
    
    for k in range(4):
        nx = j + dx[k]
        ny = i + dy[k]

        if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx]:
            if campus[ny][nx] == "X":
                continue
            if campus[ny][nx] == "P":
                cnt += 1
            visited[ny][nx] = True
            DFS(ny, nx)

for i in range(N):
    for j in range(M):
        if campus[i][j] == "I" and not visited[i][j]:
            visited[i][j] = True
            DFS(i, j)

if cnt:
    print(cnt)
else:
    print("TT")
```

<br>

#### BFS 전체코드

``` python
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
campus = [list(input().rstrip()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
cnt = 0

def BFS(i, j):
    global cnt
    Q = deque([[i, j]])

    while Q:
        y, x = Q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx]:
                if campus[ny][nx] == "X":
                    continue
                if campus[ny][nx] == "P":
                    cnt += 1
                visited[ny][nx] = True
                Q.append([ny, nx])

for i in range(N):
    for j in range(M):
        if campus[i][j] == "I" and not visited[i][j]:
            visited[i][j] = True
            BFS(i, j)

if cnt:
    print(cnt)
else:
    print("TT")
```

