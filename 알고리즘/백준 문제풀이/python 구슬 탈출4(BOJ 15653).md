

## 파이썬 구슬 탈출4(BOJ 15653)

<br>

## 문제

스타트링크에서 판매하는 어린이용 장난감 중에서 가장 인기가 많은 제품은 구슬 탈출이다. 구슬 탈출은 직사각형 보드에 빨간 구슬과 파란 구슬을 하나씩 넣은 다음, 빨간 구슬을 구멍을 통해 빼내는 게임이다.

보드의 세로 크기는 N, 가로 크기는 M이고, 편의상 1×1크기의 칸으로 나누어져 있다. 가장 바깥 행과 열은 모두 막혀져 있고, 보드에는 구멍이 하나 있다. 빨간 구슬과 파란 구슬의 크기는 보드에서 1×1크기의 칸을 가득 채우는 사이즈이고, 각각 하나씩 들어가 있다. 게임의 목표는 빨간 구슬을 구멍을 통해서 빼내는 것이다. 이때, 파란 구슬이 구멍에 들어가면 안 된다.

이때, 구슬을 손으로 건드릴 수는 없고, 중력을 이용해서 이리 저리 굴려야 한다. 왼쪽으로 기울이기, 오른쪽으로 기울이기, 위쪽으로 기울이기, 아래쪽으로 기울이기와 같은 네 가지 동작이 가능하다.

각각의 동작에서 공은 동시에 움직인다. 빨간 구슬이 구멍에 빠지면 성공이지만, 파란 구슬이 구멍에 빠지면 실패이다. 빨간 구슬과 파란 구슬이 동시에 구멍에 빠져도 실패이다. 빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없다. 또, 빨간 구슬과 파란 구슬의 크기는 한 칸을 모두 차지한다. 기울이는 동작을 그만하는 것은 더 이상 구슬이 움직이지 않을 때 까지이다.

보드의 상태가 주어졌을 때, 최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 구하는 프로그램을 작성하시오.

<br>

## 입력

첫 번째 줄에는 보드의 세로, 가로 크기를 의미하는 두 정수 N, M (3 ≤ N, M ≤ 10)이 주어진다. 다음 N개의 줄에 보드의 모양을 나타내는 길이 M의 문자열이 주어진다. 이 문자열은 '`.`', '`#`', '`O`', '`R`', '`B`' 로 이루어져 있다. '`.`'은 빈 칸을 의미하고, '`#`'은 공이 이동할 수 없는 장애물 또는 벽을 의미하며, '`O`'는 구멍의 위치를 의미한다. '`R`'은 빨간 구슬의 위치, '`B`'는 파란 구슬의 위치이다.

입력되는 모든 보드의 가장자리에는 모두 '`#`'이 있다. 구멍의 개수는 한 개 이며, 빨간 구슬과 파란 구슬은 항상 1개가 주어진다.

<br>

## 출력

최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 출력한다. 만약, 어떻게 움직여도 빨간 구슬을 구멍을 통해 빼낼 수 없으면 -1을 출력한다.

<br>

## 예제 입력 1 

```
5 5
#####
#..B#
#.#.#
#RO.#
#####
```

## 예제 출력 1 

```
1
```

## 예제 입력 2 

```
7 7
#######
#...RB#
#.#####
#.....#
#####.#
#O....#
#######
```

## 예제 출력 2 

```
5
```

## 예제 입력 3 

```
7 7
#######
#..R#B#
#.#####
#.....#
#####.#
#O....#
#######
```

## 예제 출력 3 

```
5
```

## 예제 입력 4 

```
10 10
##########
#R#...##B#
#...#.##.#
#####.##.#
#......#.#
#.######.#
#.#...##.#
#.#.#.#..#
#...#.O#.#
##########
```

## 예제 출력 4 

```
12
```

## 예제 입력 5 

```
3 7
#######
#R.O.B#
#######
```

## 예제 출력 5 

```
1
```

## 예제 입력 6 

```
10 10
##########
#R#...##B#
#...#.##.#
#####.##.#
#......#.#
#.######.#
#.#....#.#
#.#.##...#
#O..#....#
##########
```

## 예제 출력 6 

```
7
```

## 예제 입력 7 

```
3 10
##########
#.O....RB#
##########
```

## 예제 출력 7 

```
-1
```

<br>

## 📝 풀어보기

이 문제는 구슬 탈출 ~ 구슬탈출 4까지 있다. 전부 풀어본 결과 구슬탈출 4를 풀면 나머지 문제는 조금씩 문제를 활용해서 풀면 된다.

<br>

보드의 세로 N, 가로 M을 입력받는다.

N줄에 걸쳐서 보드의 정보를 입력받는다. 보드 내의 문자열은 ".", "#", "O", "R", "B"로 이뤄져있고 각각 빈칸, 벽, 구멍, 빨간구슬, 파란구슬을 의미한다.

visited는 빨간구슬과 파란구슬의 해당 위치 방문 여부를 확인하기 위해 `[[False] * M for _ in range(N)]]`을 M 만큼 반복하고, 다시 그것을 N만큼 반복한 값을 저장한다.

dx, dy에는 상하좌우 탐색을 위해 좌표를 저장해둔다. 

``` python
import sys
from collections import deque
from pprint import pprint
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
```

<br>

보드의 세로와 가로 N M만큼 반복하며 탐색하는 보드의 요소가 빨간구슬(R)이면 rx, ry에 위치값을, 파란구슬(B)이면  bx, by에 위치값을 저장하고 BFS를 수행한다.

``` python
for i in range(N):
    for j in range(M):
        if board[i][j] == "R":
            rx, ry = i, j
        if board[i][j] == "B":
            bx, by = i, j

BFS(rx, ry, bx, by)
```

<br>

BFS를 정의 하기 전 move함수를 정의한다. 인자는 좌표 값 x, y 그리고 방향 dir이다.

cnt를 0으로 초기화하고, 반복 종료조건을 board의 상하좌우 탐색값이 #이고, `board[x][y]`가 구멍일때로 한다.

반복하는동안 x, y에 탐색하는 좌표값을 더하고 카운트를 1 증가시킨후 반환한다.

``` python
def move(x, y, dir):
    cnt = 0

    while board[x + dx[dir]][y + dy[dir]] != "#" and board[x][y] != "O":
        x += dx[dir]
        y += dy[dir]
        cnt += 1

    return x, y, cnt
```

<br>

BFS를 정의한다.

deque에 인자로 들어간 좌표 값들과 시작 카운트 1을 저장한다.

Q에 값이 있는동안 반복하며 rx, ry, bx, by, cnt에 Q에 삽입된 값을 꺼내어 저장한다. visited의 꺼낸 빨간 구슬과 파란 구슬의 좌표는 방문처리한다.

상하좌우를 반복하며 빨간 구슬의 좌표와 카운트, 파란 구슬의 좌표와 카운트에 move함수를 실행한다. 실행된 함수는 각각의 좌표들에 dx, dy의 상하좌우 값을 더하고, 카운트를 더해 반환할것이다.

여기서, `board[bnx]][bny]`가 구멍이 아니고, `board[rnx][rny]`가 구멍이라면 빨간 구슬만 구멍에 들어간 것이므로 움직인 카운트를 출력하고 프로그램을 종료한다.

<br>

이 문제의 탐색하는 과정에서 중요한건, 구슬들이 탐색을 하는 과정에서 **좌표가 겹칠수도 있다는 점**이다. 실제로 구슬은 같은 좌표상에서 겹쳐있을 수는 없다. 그렇기 때문에 bnx와 rnx, bny와 rny과 같다면 둘의 움직인 카운트 값을 확인해서 rcnt가 더 크다면 rnx, rny에 움직인 좌표값을 빼주어 구슬을 정렬하고, bcnt가 크다면 bnx, bny에 움직인 좌표값을 빼주어 정렬해야한다.

<br>

빨간 구슬과 파란 구슬 모두 방문하지 않은 좌표가 있다면 방문처리를 하고 해당 좌표값과 cnt+1값을 Q에 넣는다.

Q가 전부 비어도 문제가 해결되지 않는다면 -1을 출력하고 반환한다.

``` python
def BFS(x1, y1, x2, y2):
    Q = deque([[x1, y1, x2, y2, 1]])

    while Q:
        rx, ry, bx, by, cnt = Q.popleft()
        visited[rx][ry][bx][by] = True
        
        for i in range(4):
            rnx, rny, rcnt = move(rx, ry, i)
            bnx, bny, bcnt = move(bx, by, i)

            if board[bnx][bny] != "O":
                if board[rnx][rny] == "O":
                    print(cnt)
                    exit(0)
            
                if bnx == rnx and bny == rny:
                    if rcnt > bcnt:
                        rnx -= dx[i]
                        rny -= dy[i]
                    else:
                        bnx -= dx[i]
                        bny -= dy[i]

                if not visited[rnx][rny][bnx][bny]:
                    visited[rnx][rny][bnx][bny] = True
                    Q.append([rnx, rny, bnx, bny, cnt+1])
    print(-1)
    return
```

<br>

#### 전체코드

``` python
import sys
from collections import deque
from pprint import pprint
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def move(x, y, dir):
    cnt = 0

    while board[x + dx[dir]][y + dy[dir]] != "#" and board[x][y] != "O":
        x += dx[dir]
        y += dy[dir]
        cnt += 1

    return x, y, cnt


def BFS(x1, y1, x2, y2):
    Q = deque([[x1, y1, x2, y2, 1]])

    while Q:
        rx, ry, bx, by, cnt = Q.popleft()
        visited[rx][ry][bx][by] = True
        
        for i in range(4):
            rnx, rny, rcnt = move(rx, ry, i)
            bnx, bny, bcnt = move(bx, by, i)

            if board[bnx][bny] != "O":
                if board[rnx][rny] == "O":
                    print(cnt)
                    exit(0)
            
                if bnx == rnx and bny == rny:
                    if rcnt > bcnt:
                        rnx -= dx[i]
                        rny -= dy[i]
                    else:
                        bnx -= dx[i]
                        bny -= dy[i]

                if not visited[rnx][rny][bnx][bny]:
                    visited[rnx][rny][bnx][bny] = True
                    Q.append([rnx, rny, bnx, bny, cnt+1])
    print(-1)
    return

for i in range(N):
    for j in range(M):
        if board[i][j] == "R":
            rx, ry = i, j
        if board[i][j] == "B":
            bx, by = i, j

BFS(rx, ry, bx, by)
```

