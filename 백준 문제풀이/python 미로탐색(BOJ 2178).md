## python 미로탐색(백준 BOJ 2178)

<br>

BFS의 사용

## 문제

N×M크기의 배열로 표현되는 미로가 있다.

| 1    | 0    | 1    | 1    | 1    | 1    |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 1    | 0    | 1    | 0    | 1    | 0    |
| 1    | 0    | 1    | 0    | 1    | 1    |
| 1    | 1    | 1    | 0    | 1    | 1    |

미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

<br>

## 입력

첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 **붙어서** 입력으로 주어진다.

<br>

## 출력

첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.

<br>

## 예제 입력 1

```
4 6
101111
101010
101011
111011
```

## 예제 출력 1

```
15
```

## 예제 입력 2

```
4 6
110110
110110
111111
111101
```

## 예제 출력 2

```
9
```

## 예제 입력 3

```
2 25
1011101110111011101110111
1110111011101110111011101
```

## 예제 출력 3

```
38
```

## 예제 입력 4

```
7 7
1011111
1110001
1000001
1000001
1000001
1000001
1111111
```

## 예제 출력 4

```
13
```

<br>

## 📝 풀어보기

📌 sys를 import하여 readline을 사용한다.

N개의 행, M개의 열만큼 입력받고 board 리스트를 생성해서 N개의 행만큼 입력해서 저장한다. 

``` python
import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 배열크기 N*M
board = []

# 배열입력
for _ in range(N):
    board.append(list(input()))
```

<br>

📌 배열을 int형으로 선언하고, 상하좌우 탐색을 위한 리스트를 생성한다. queue에는 시작 좌표를 저장해둔다.

배열을 int형으로 선언하지 않으면 이후 계산에 TypeError가 생긴다.

``` python
# 배열을 int형으로 선언
board[0][0] = 1

# 델타탐색(상하좌우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 시작좌표
queue = [[0,0]]
```

<br>

📌 queue가 빌때까지 반복하면서 x, y에 queue의 첫번째 리스트의 첫번째 요소, 첫번째 리스트의 두번째 요소를 각각 담고 queue를 삭제시킨다.

상하좌우 좌표값을 x와 y에 합산하여 nx, ny에 넣고 nx, ny가 범위 내에 있으면  `board[nx][ny]`값이 "1"일때 [nx, ny] 좌표값을 queue에 넣어주고 보드의 1인 값을 1씩 점점 늘려준다.

마지막으로 최종 보드 좌표값을 출력한다.

``` python
# BFS 시작
while queue:
    x, y = queue[0][0], queue[0][1]
    del queue[0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and ny >= 0 and nx < N and ny < M:
            if board[nx][ny] == "1":
                queue.append([nx, ny])
                board[nx][ny] = board[x][y] + 1
                
print(board[N-1][M-1])
```

<br>

#### 전체 코드

``` python
import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 배열크기 N*M
board = []

# 배열입력
for _ in range(N):
    board.append(list(input()))

# 배열을 int형으로 선언
board[0][0] = 1

# 델타탐색(상하좌우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 시작좌표
queue = [[0,0]]

# BFS 시작
while queue:
    x, y = queue[0][0], queue[0][1]
    del queue[0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and ny >= 0 and nx < N and ny < M:
            if board[nx][ny] == "1":
                queue.append([nx, ny])
                board[nx][ny] = board[x][y] + 1
                
print(board[N-1][M-1])
```

