

## 파이썬 나이트의 이동(BOJ 7562)

<br>

## 문제

체스판 위에 한 나이트가 놓여져 있다. 나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다. 나이트가 이동하려고 하는 칸이 주어진다. 나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?

![img](https://www.acmicpc.net/upload/images/knight.png)

<br>

## 입력

입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.

각 테스트 케이스는 세 줄로 이루어져 있다. 첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다. 체스판의 크기는 l × l이다. 체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다. 둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.

<br>

## 출력

각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 출력한다.

<br>

## 예제 입력 1

```
3
8
0 0
7 0
100
0 0
30 50
10
1 1
1 1
```

## 예제 출력 1 

```
5
28
0
```

<br>

## 📝 풀어보기 

dx, dy 의 좌표는 위의 그림에서 초록색 부분으로 표시된 나이트의 이동경로 좌표다.

체스에서 나이트는 1칸을 전진한 후 좌, 우로 1칸을 이동한다.

```python
import sys
from collections import deque
input = sys.stdin.readline

# 나이트의 이동 경로 8가지
dx = [-1, 1, 2, 2, 1, -1, -2, -2]
dy = [2, 2, 1, -1, -2, -2, -1, 1]
```

<br>

테스트 케이스의 수(T)를 입력받고 T만큼 반복하면서 체스판 한 변의 길이(I), 나이트의 현재 위치와 이동하려는 칸의 위치를 입력받는다.

board에는 체스판의 크기 I*I 만큼 0을 저장해둔다. 그리고 BFS를 수행한다.

```python
T = int(input())
for _ in range(T):
    # 체스판 한 변의 길이
    I = int(input())
    board = [[0] * I for _ in range(I)]
    # pprint(board)
    # 나이트가 현재 있는 칸
    X1, Y1 = map(int, input().split())
    # 나이트가 이동하려는 칸
    X2, Y2 = map(int, input().split())
    BFS(X1, Y1, X2, Y2)
```

<br>

deque를 생성하고 나이트의 현재 위치 좌표를 담아둔다.

현재 위치를 이미 방문했으므로 해당 좌표의 값은 1로 처리한다.

현재 위치를 꺼내 a, b에 저장해둔다. a, b가 이동하려는 칸에 도달했다면, 이동하려는 칸의 값 -1 을 출력하고 리턴한다.

a, b에 나이트가 이동할 수 있는 좌표 8방위를 순차적으로 더해 탐색한다.

범위 내에 나이트의 좌표가 있다면 Q에 좌표값을 저장하고 board의 해당 좌표에 1을 누적한다.

``` python
def BFS(x1, y1, x2, y2):
    Q = deque()
    Q.append([x1, y1])
    # 방문처리
    board[x1][y1] = 1
    
    while Q:
        a, b = Q.popleft()
        if a == x2 and b == y2:
            print(board[x2][y2] -1)
            return
        for i in range(8):
            x = a + dx[i]
            y = b + dy[i]
            # 범위 내의 위치에서 이동횟수 기록
            if 0 <= x < I and 0 <= y < I and board[x][y] == 0:
                Q.append([x, y])
                board[x][y] = board[a][b]+1
```

<br>

#### 전체코드

``` python
import sys
from collections import deque
input = sys.stdin.readline

# 나이트의 이동 경로 8가지
dx = [-1, 1, 2, 2, 1, -1, -2, -2]
dy = [2, 2, 1, -1, -2, -2, -1, 1]

def BFS(x1, y1, x2, y2):
    Q = deque()
    Q.append([x1, y1])
    # 방문처리
    board[x1][y1] = 1
    
    while Q:
        a, b = Q.popleft()
        if a == x2 and b == y2:
            print(board[x2][y2] -1)
            return
        for i in range(8):
            x = a + dx[i]
            y = b + dy[i]
            # 범위 내의 위치에서 이동횟수 기록
            if 0 <= x < I and 0 <= y < I and board[x][y] == 0:
                Q.append([x, y])
                board[x][y] = board[a][b]+1
            
T = int(input())
for _ in range(T):
    # 체스판 한 변의 길이
    I = int(input())
    board = [[0] * I for _ in range(I)]
    # pprint(board)
    # 나이트가 현재 있는 칸
    X1, Y1 = map(int, input().split())
    # 나이트가 이동하려는 칸
    X2, Y2 = map(int, input().split())
    BFS(X1, Y1, X2, Y2)
```

<br>



