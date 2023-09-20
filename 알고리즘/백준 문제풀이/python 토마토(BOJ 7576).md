

## 파이썬 토마토(BOJ 7576)

<br>

## 문제

철수의 토마토 농장에서는 토마토를 보관하는 큰 창고를 가지고 있다. 토마토는 아래의 그림과 같이 격자 모양 상자의 칸에 하나씩 넣어서 창고에 보관한다. 

![img](https://upload.acmicpc.net/de29c64f-dee7-4fe0-afa9-afd6fc4aad3a/-/preview/)

창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다. 보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다. 하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향에 있는 토마토를 의미한다. 대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다. 철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다.

토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때, 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라. 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.

<br>

## 입력

첫 줄에는 상자의 크기를 나타내는 두 정수 M,N이 주어진다. M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다. 단, 2 ≤ M,N ≤ 1,000 이다. 둘째 줄부터는 하나의 상자에 저장된 토마토들의 정보가 주어진다. 즉, 둘째 줄부터 N개의 줄에는 상자에 담긴 토마토의 정보가 주어진다. 하나의 줄에는 상자 가로줄에 들어있는 토마토의 상태가 M개의 정수로 주어진다. 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.

토마토가 하나 이상 있는 경우만 입력으로 주어진다.

<br>

## 출력

여러분은 토마토가 모두 익을 때까지의 최소 날짜를 출력해야 한다. 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.

<br>

## 예제 입력 1 

```
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
```

## 예제 출력 1 

```
8
```

## 예제 입력 2

```
6 4
0 -1 0 0 0 0
-1 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
```

## 예제 출력 2 

```
-1
```

## 예제 입력 3 

```
6 4
1 -1 0 0 0 0
0 -1 0 0 0 0
0 0 0 0 -1 0
0 0 0 0 -1 1
```

## 예제 출력 3 

```
6
```

## 예제 입력 4 

```
5 5
-1 1 0 0 0
0 -1 -1 -1 0
0 -1 -1 -1 0
0 -1 -1 -1 0
0 0 0 0 0
```

## 예제 출력 4 

```
14
```

## 예제 입력 5 

```
2 2
1 -1
-1 1
```

## 예제 출력 5 

```
0
```

<br>

## 📝 풀어보기 

BFS를 이용해서 토마토가 모두 익을때 까지 걸리는 일수를 출력하는 문제다.

토마토는 익은 토마토(1)을 기준으로 위, 아래, 좌, 우 4방위로 번져나가면서 익는다.

상자의 가로(M), 세로(N)칸의 수를 입력받는다.

board에 토마토의 상태를 입력받는다. 여기서 1은 익은 토마토, 0은 익지 않은 토마토, -1은 토마토가 없는 칸이다.

BFS를 수행하기 위한 deque와 토마토가 전부 익는 일수를 세기 위한 cnt를 만들어 저장해둔다.

``` python
from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
Q = deque()
cnt = 0
```

<br>

N, M 만큼 순회하면서 board의 순회하는 좌표에 익은토마토(1)가 있다면 Q에 좌표값을 저장해둔다.

BFS를 수행한다. 익은 토마토가 든 좌표를 꺼내 a, b에 저장하고 a, b에 대해 위, 아래, 좌, 우 4방위를 탐색한다.

범위를 넘지 않는곳에 토마토가 있다면, `board[a][b]`에 +1을 더한 값을 탐색하는 좌표에 추가한다. 그리고 Q에 해당 좌표를 추가해준다.

``` python
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            Q.append([i, j])

def BFS():
    while Q:
        a, b = Q.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < N and 0 <= y < M and board[x][y] == 0:
                board[x][y] = board[a][b] + 1
                Q.append([x, y])

BFS()
```

<br>

BFS 수행 후에 board에서 0이 탐색되면 토마토가 익을 수 없는것이기 때문에 -1을 출력한다.

그외엔 cnt를 갱신하고, 익은 토마토 값이 있으므로 cnt-1을 출력한다.

``` python
for i in board:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    cnt = max(cnt, max(i))

print(cnt-1)
```

<br>

#### 전체코드

``` python
from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
Q = deque()
cnt = 0

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            Q.append([i, j])

def BFS():
    while Q:
        a, b = Q.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < N and 0 <= y < M and board[x][y] == 0:
                board[x][y] = board[a][b] + 1
                Q.append([x, y])

BFS()
for i in board:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    cnt = max(cnt, max(i))

print(cnt-1)
```

<br>



