

## 파이썬 점프왕 쩰리(BOJ 16173)

<br>

## 문제

‘쩰리’는 점프하는 것을 좋아하는 젤리다. 단순히 점프하는 것에 지루함을 느낀 ‘쩰리’는 새로운 점프 게임을 해보고 싶어 한다. 새로운 점프 게임의 조건은 다음과 같다.

1. ‘쩰리’는 가로와 세로의 칸 수가 같은 정사각형의 구역 내부에서만 움직일 수 있다. ‘쩰리’가 정사각형 구역의 외부로 나가는 경우엔 바닥으로 떨어져 즉시 게임에서 패배하게 된다.
2. ‘쩰리’의 출발점은 항상 정사각형의 가장 왼쪽, 가장 위의 칸이다. 다른 출발점에서는 출발하지 않는다.
3. ‘쩰리’가 이동 가능한 방향은 오른쪽과 아래 뿐이다. 위쪽과 왼쪽으로는 이동할 수 없다.
4. ‘쩰리’가 가장 오른쪽, 가장 아래 칸에 도달하는 순간, 그 즉시 ‘쩰리’의 승리로 게임은 종료된다.
5. ‘쩰리’가 한 번에 이동할 수 있는 칸의 수는, 현재 밟고 있는 칸에 쓰여 있는 수 만큼이다. 칸에 쓰여 있는 수 초과나 그 미만으로 이동할 수 없다.

새로운 게임이 맘에 든 ‘쩰리’는, 계속 게임을 진행해 마침내 최종 단계에 도달했다. 하지만, 게임을 진행하는 구역이 너무 넓어져버린 나머지, 이 게임에서 이길 수 있는지 없는지 가늠할 수 없어졌다. ‘쩰리’는 유능한 프로그래머인 당신에게 주어진 구역에서 승리할 수 있는 지 알아봐 달라고 부탁했다. ‘쩰리’를 도와 주어진 게임 구역에서 끝 점(오른쪽 맨 아래 칸)까지 도달할 수 있는지를 알아보자!

<br>

## 입력

입력의 첫 번째 줄에는 게임 구역의 크기 N (2 ≤ N ≤ 3)이 주어진다.

입력의 두 번째 줄부터 마지막 줄까지 게임판의 구역(맵)이 주어진다.

게임판의 승리 지점(오른쪽 맨 아래 칸)에는 -1이 쓰여있고, 나머지 칸에는 0 이상 100 이하의 정수가 쓰여있다.

<br>

## 출력

‘쩰리’가 끝 점에 도달할 수 있으면 “HaruHaru”(인용부호 없이), 도달할 수 없으면 “Hing” (인용부호 없이)을 한 줄에 출력합니다.

<br>

## 예제 입력 1

```
3
1 1 10
1 5 1
2 2 -1
```

## 예제 출력 1

```
HaruHaru
```

쩰리는 맨 왼쪽 위의 칸에서 출발해 (행, 열)로 나타낸 좌표계로, (1, 1) -> (2, 1) -> (3, 1) -> (3, 3)으로 이동해 게임에서 승리할 수 있다.

## 예제 입력 2

```
3
2 2 1
2 2 2
1 2 -1
```

## 예제 출력 2

```
Hing
```

쩰리는 맨 왼쪽 위의 칸에서 출발하더라도 절대 게임의 승리 지점인 (3, 3)에 도달할 수 없다.

<br>

## 📝 풀어보기 

이 문제는 너비 우선 탐색(BFS), 깊이 우선 탐색(DFS) 두 가지로 풀어볼 수 있다.

DFS의 연습이 부족한것 같아 두가지로 풀 수 있는 문제는 전부 두가지 방법으로 풀어보려고 한다.

<br>

#### BFS로 풀어보기

게임 구역의 크기 N을 입력받고, board의 상태를 입력받아 저장 후, board의 크기와 같은 visited를 저장해둔다.

쩰리는 오른쪽과 아래로만 이동이 가능하다. 그러므로 dx, dy의 좌표를 오른쪽, 아래를 저장해둔다.

``` python
import sys
from collections import deque
input = sys.stdin.readline


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dx = [1, 0]
dy = [0, 1]
```

<br>

BFS를 정의한다.

Q에 쩰리의 시작점인 0, 0을 삽입해둔다.

Q에서 꺼낸 값을 x, y에 저장하고 `board[x][y]`의 값이 -1이라면 마지막 지점에 도착한 것이므로 "HaruHaru"를 출력하고 반복을 탈출한다.

쩰리가 밟게 되는 발판에는 이동할 거리가 적혀있다. `board[x][y] `의 값을 dist에 저장해두고 오른쪽과 왼쪽 아래를 탐색한다.

시작지점인 x 값 + (오른쪽 이동 * 이동 거리) 값을 nx에 저장한다. ny또한 원리가 같다.

nx, ny가 보드를 벗어나지 않고, `[nx][ny]`를 방문하지 않았다면 해당 지점의 방문여부를 True로 변경하고 Q에 nx, ny 값을 추가한다.

그 외엔 도착점에 도달 할 수 없으므로 "Hing"을 출력한다.

```python
def BFS():
    Q = deque([[0, 0]])

    while Q:
        x, y = Q.popleft()
        if board[x][y] == -1:
            print("HaruHaru")
            exit(0)
        
        dist = board[x][y] 

        for i in range(2):
            nx = x + dx[i] * dist
            ny = y + dy[i] * dist

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = True
                Q.append([nx, ny])

    print("Hing")
```

<br>

#### BFS 전체코드

``` python
import sys
from collections import deque
input = sys.stdin.readline


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dx = [1, 0]
dy = [0, 1]


def BFS():
    Q = deque([[0, 0]])


    while Q:
        x, y = Q.popleft()
        if board[x][y] == -1:
            print("HaruHaru")
            exit(0)
        
        dist = board[x][y] 

        for i in range(2):
            nx = x + dx[i] * dist
            ny = y + dy[i] * dist

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = True
                Q.append([nx, ny])

    print("Hing")

BFS()                
```

<br>

#### DFS로 풀어보기

게임 구역의 크기 N을 입력받고, board의 상태를 입력받아 저장 후, board의 크기와 같은 visited를 저장해둔다.

``` python
import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
```

<br>

함수 DFS를 정의한다.

x, y가 범위를 넘지 않고, 해당 좌표가 방문하지 않았다면 방문처리를 하고, x좌표에 이동거리인`board[x][y]` 를 더해준 값을 DFS 실행한다.

y좌표에도 이동거리인 `board[x][y]`를 더해준 값을 DFS실행한다. 범위를 벗어나는 경우에는 리턴을 한다.

 `board[x][y]`가 -1인 경우에는 마지막에 도착을 한것이기 때문에 방문여부를 True로 바꿔주고 리턴한다.

```python
def DFS(x, y):
    if 0 <= x < N and 0 <= y < N and visited[x][y] == False:
        visited[x][y] = True        

        DFS(x+board[x][y], y)
        DFS(x, y+board[x][y])
    else:
        return

    if board[x][y] == -1:
        visited[x][y] = True
        return
```

<br>

DFS를 실행하고 visited의 맨 끝이 True라면, 목적지에 도달한것이기 때문에 "HaruHaru"를 출력하고, 그외엔 "Hing"을 출력한다.

``` python
DFS(0, 0)
        
if visited[-1][-1] == True:
    print("HaruHaru")
else:
    print("Hing")
```

<br>

#### DFS 전체코드

```python
import sys
from collections import deque
input = sys.stdin.readline


def DFS(x, y):
    if 0 <= x < N and 0 <= y < N and visited[x][y] == False:
        visited[x][y] = True        

        DFS(x+board[x][y], y)
        DFS(x, y+board[x][y])
    else:
        return

    if board[x][y] == -1:
        visited[x][y] = True
        return


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]



DFS(0, 0)
        
if visited[-1][-1] == True:
    print("HaruHaru")
else:
    print("Hing")
```

