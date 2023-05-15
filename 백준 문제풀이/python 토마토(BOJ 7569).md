

## 파이썬 토마토(BOJ 7569)

<br>

## 문제

철수의 토마토 농장에서는 토마토를 보관하는 큰 창고를 가지고 있다. 토마토는 아래의 그림과 같이 격자모양 상자의 칸에 하나씩 넣은 다음, 상자들을 수직으로 쌓아 올려서 창고에 보관한다.

![img](https://upload.acmicpc.net/c3f3343d-c291-40a9-9fe3-59f792a8cae9/-/preview/)

창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다. 보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다. 하나의 토마토에 인접한 곳은 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향에 있는 토마토를 의미한다. 대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다. 철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지 그 최소 일수를 알고 싶어 한다.

토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때, 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라. 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.

<br>

## 입력

첫 줄에는 상자의 크기를 나타내는 두 정수 M,N과 쌓아올려지는 상자의 수를 나타내는 H가 주어진다. M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다. 단, 2 ≤ M ≤ 100, 2 ≤ N ≤ 100, 1 ≤ H ≤ 100 이다. 둘째 줄부터는 가장 밑의 상자부터 가장 위의 상자까지에 저장된 토마토들의 정보가 주어진다. 즉, 둘째 줄부터 N개의 줄에는 하나의 상자에 담긴 토마토의 정보가 주어진다. 각 줄에는 상자 가로줄에 들어있는 토마토들의 상태가 M개의 정수로 주어진다. 정수 1은 익은 토마토, 정수 0 은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다. 이러한 N개의 줄이 H번 반복하여 주어진다.

토마토가 하나 이상 있는 경우만 입력으로 주어진다.

<br>

## 출력

여러분은 토마토가 모두 익을 때까지 최소 며칠이 걸리는지를 계산해서 출력해야 한다. 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.

<br>

## 예제 입력 1 

```
5 3 1
0 -1 0 0 0
-1 -1 0 1 1
0 0 0 1 1
```

## 예제 출력 1 

```
-1
```

## 예제 입력 2 

```
5 3 2
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 0
```

## 예제 출력 2 

```
4
```

## 예제 입력 3 

```
4 3 2
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1
-1 -1 -1 -1
1 1 1 -1
```

## 예제 출력 3 

```
0
```

<br>

## 📝 풀어보기 

기존의 토마토(BOJ 7576)의 문제가 3차원으로 확장된 문제다.

M(상자의 가로 칸), N(상자의 세로 칸), H(상자의 높이)를 입력받는다.

board에는 토마토의 상태를 입력받는다. 토마토의 상태는 0(익지 않은 상태), 1(익은 상태), -1(토마토가 없음)이 있다.

visited에는 해당 위치를 방문했는지 기록한다. 기본값으로 토마토가 들어갈 수 있는 칸 만큼 False를 저장해둔다.

방문 여부를 탐색하기 위한 좌표에 dz가 추가되었다. 탐색범위는 순서대로 오른쪽, 왼쪽, 앞, 뒤, 위, 아래다.

``` python
from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())
board = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[list(False for _ in range(M)) for _ in range(N)] for _ in range(H)]
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
Q = deque()
```

<br>

높이, 세로, 가로 순으로 순회하면서 해당 좌표에 익은 토마토가 있는지, 해당 좌표가 방문하지 않았는지 확인한다.

토마토가 익었고, 좌표를 방문하지 않았다면 해당 좌표의 방문여부를 True로 바꾸고 Q에 좌표를 추가한다.

``` python
# N = 가로칸(x축)
# M = 세로칸(y축)
# H = 높이(z축)
for i in range(H): # 높이
    for j in range(N): # 세로
        for k in range(M): # 가로
            if board[i][j][k] == 1 and visited[i][j][k] == False:
                visited[i][j][k] = True
                Q.append([i, j, k])


```

<br>

함수 BFS를 선언한다.

Q에 담아둔 좌표를 꺼내서 꺼낸 좌표를 기준으로 6방위를 탐색한다.

탐색하는 좌표가 범위를 벗어나면 건너뛰고, 탐색하는 좌표의 토마토가 익지 않았고 방문하지 않은곳이라면 해당 좌표의 방문여부를 True로 바꾸고 해당좌표에 1을 추가한다. 그리고 탐색한 좌표를 다시 Q에 저장하고 모든 탐색이 끝날때까지 반복한다. 

``` python
# (높이, 세로, 가로)
def BFS():
    while Q:
        a, b, c = Q.popleft()
        for l in range(6):
            z = a + dz[l] # 높이
            y = b + dy[l] # 세로
            x = c + dx[l] # 가로

            # 탐색 범위를 넘어서면 건너뛴다.
            if 0 > x or x >= M or 0 > y or y >= N or 0 > z or z >= H:
                continue
            if board[z][y][x] == 0 and visited[z][y][x] == False:
                visited[z][y][x] = True
                board[z][y][x] = board[a][b][c] + 1
                Q.append([z, y, x])
```

<br>

BFS를 수행한다.

cnt는 토마토가 익는 날짜를 기록하기 위해 0을 저장해둔다.

토마토의 익은 날짜와 상태가 저장된 board리스트를 순회하면서 만약, k == 0(토마토가 익지 않은 상태)가 발견된다면, 토마토는 모두 익지 못하는 상황이기 때문에 -1을 출력하고 종료한다.

그외엔 각 토마토가 든 판(j)에서 가장 오래 익은 토마토의 날짜를 찾아내고, cnt와 비교하여 더 큰 값으로 갱신한다.

마지막으로 익은 토마토가 처음부터 1인 상태였으므로, cnt에서 1을 뺀 값을 출력한다.

``` python
BFS() # (높이, 세로, 가로)
cnt = 0
for i in board:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        cnt = max(cnt, max(j))

print(cnt-1)
```

<br>

#### 전체코드

``` python
from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())
board = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[list(False for _ in range(M)) for _ in range(N)] for _ in range(H)]
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
Q = deque()

# (높이, 세로, 가로)
def BFS():
    while Q:
        a, b, c = Q.popleft()
        for l in range(6):
            z = a + dz[l] # 높이
            y = b + dy[l] # 세로
            x = c + dx[l] # 가로

            # 탐색 범위를 넘어서면 건너뛴다.
            if 0 > x or x >= M or 0 > y or y >= N or 0 > z or z >= H:
                continue
            if board[z][y][x] == 0 and visited[z][y][x] == False:
                visited[z][y][x] = True
                board[z][y][x] = board[a][b][c] + 1
                Q.append([z, y, x])

# N = 가로칸(x축)
# M = 세로칸(y축)
# H = 높이(z축)
for i in range(H): # 높이
    for j in range(N): # 세로
        for k in range(M): # 가로
            if board[i][j][k] == 1 and visited[i][j][k] == False:
                visited[i][j][k] = True
                Q.append([i, j, k])


BFS() # (높이, 세로, 가로)
cnt = 0
for i in board:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        cnt = max(cnt, max(j))

print(cnt-1)
```

<br>



