

## 파이썬 구슬 탈출3(BOJ 15644)

<br>

## 문제

스타트링크에서 판매하는 어린이용 장난감 중에서 가장 인기가 많은 제품은 구슬 탈출이다. 구슬 탈출은 직사각형 보드에 빨간 구슬과 파란 구슬을 하나씩 넣은 다음, 빨간 구슬을 구멍을 통해 빼내는 게임이다.

보드의 세로 크기는 N, 가로 크기는 M이고, 편의상 1×1크기의 칸으로 나누어져 있다. 가장 바깥 행과 열은 모두 막혀져 있고, 보드에는 구멍이 하나 있다. 빨간 구슬과 파란 구슬의 크기는 보드에서 1×1크기의 칸을 가득 채우는 사이즈이고, 각각 하나씩 들어가 있다. 게임의 목표는 빨간 구슬을 구멍을 통해서 빼내는 것이다. 이때, 파란 구슬이 구멍에 들어가면 안 된다.

이때, 구슬을 손으로 건드릴 수는 없고, 중력을 이용해서 이리 저리 굴려야 한다. 왼쪽으로 기울이기, 오른쪽으로 기울이기, 위쪽으로 기울이기, 아래쪽으로 기울이기와 같은 네 가지 동작이 가능하다.

각각의 동작에서 공은 동시에 움직인다. 빨간 구슬이 구멍에 빠지면 성공이지만, 파란 구슬이 구멍에 빠지면 실패이다. 빨간 구슬과 파란 구슬이 동시에 구멍에 빠져도 실패이다. 빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없다. 또, 빨간 구슬과 파란 구슬의 크기는 한 칸을 모두 차지한다. 기울이는 동작을 그만하는 것은 더 이상 구슬이 움직이지 않을 때 까지이다.

보드의 상태가 주어졌을 때, 최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지, 또 어떻게 기울여야 하는지 구하는 프로그램을 작성하시오.

## 입력

첫 번째 줄에는 보드의 세로, 가로 크기를 의미하는 두 정수 N, M (3 ≤ N, M ≤ 10)이 주어진다. 다음 N개의 줄에 보드의 모양을 나타내는 길이 M의 문자열이 주어진다. 이 문자열은 '`.`', '`#`', '`O`', '`R`', '`B`' 로 이루어져 있다. '`.`'은 빈 칸을 의미하고, '`#`'은 공이 이동할 수 없는 장애물 또는 벽을 의미하며, '`O`'는 구멍의 위치를 의미한다. '`R`'은 빨간 구슬의 위치, '`B`'는 파란 구슬의 위치이다.

입력되는 모든 보드의 가장자리에는 모두 '`#`'이 있다. 구멍의 개수는 한 개 이며, 빨간 구슬과 파란 구슬은 항상 1개가 주어진다.

<br>

## 출력

첫째 줄에 최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지, 둘째 줄에 어떻게 기울여야 하는지 순서대로 출력한다. 왼쪽으로 기울이기는 'L', 오른쪽으로 기울이기는 'R', 위로 기울이기는 'U', 아래로 기울이기는 'D'로 출력하며, 공백없이 한 줄에 모두 출력한다. 가능한 방법이 여러 가지면, 아무거나 출력한다.

만약, 10번 이하로 움직여서 빨간 구슬을 구멍을 통해 빼낼 수 없으면 -1을 출력한다.

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
R
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
LDRDL
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
LDRDL
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
#.#....#.#
#.#.#.#..#
#...#.O#.#
##########
```

## 예제 출력 4 

```
-1
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
R
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
DRURDLD
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

이 문제는 구슬 탈출4와 매우 유사하다. 하지만 구슬 탈출2의 조건과 더불어 이동에 사용된 명령어를 출력해야하는 조건이 있다.

<br>

보드의 세로 가로 N, M을 입력받는다.

board의 상태를 입력받아 저장한다.  '`.`'은 빈 칸을 의미하고, '`#`'은 공이 이동할 수 없는 장애물 또는 벽을 의미하며, '`O`'는 구멍의 위치를 의미한다. '`R`'은 빨간 구슬의 위치, '`B`'는 파란 구슬의 위치이다.

visited에는 빨간 구슬과 파란 구슬의 board방문여부를 저장한다.  

path에는 빨간 구슬과 파란 구슬의 이동경로를 저장한다. path의 값을 꺼내어 command의 인덱스에 대응하는 명령어를 ans에 저장해 출력할 예정이다.

``` python
# '.', '#', 'O', 'R', 'B' 
# . : 빈칸, # : 벽, O : 구멍, R : 빨간공, B : 파란공
import sys
from collections import deque
from pprint import pprint
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
path = [[[[[0, 0, 0, 0, 0] for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
command = ['U', 'R', 'D', 'L']
ans = list()
```

<br>

함수 BFS에서 board의 파란 구슬이 구멍에 빠지지 않고, 빨간 구슬이 구멍에 빠지는 경우에 ans에 command[i] 값을 삽입한다.

rmx, rmy, bmx, bmy 에 각각 rx,  ry, bx, by를 저장하고 rmx가 True인 동안 rmx, rmy, bmx, bmy, k에 `path[rmx][rmy][bmx][bmy]`의 값을 저장하고 `command[k]`의 값을 ans에 삽입한다.

반복이 종료된 후 ans의 맨 끝의 값을 빼내고, 리스트를 역순으로 회전시킨다.

그리고 cnt와 공백을 뺀 ans의 값을 출력해준다.

63번째 줄의 `if not visited[rnx][rny][bnx][bny]:` 빨간 구슬과 파란 구슬이 방문하지 않은 경우에 path의 해당 좌표에도 rx, ry, bx, by, i값을 저장해준다.

``` python

def BFS(x1, y1, x2, y2):
    Q = deque([[x1, y1, x2, y2, 1]])

    while Q:
        rx, ry, bx, by, cnt = Q.popleft()
        visited[rx][ry][bx][by] = True

        if cnt > 10:
            print(-1)
            exit(0)

        for i in range(4):
            rnx, rny, rcnt = move(rx, ry, i)
            bnx, bny, bcnt = move(bx, by, i)

            if board[bnx][bny] != "O":
                if board[rnx][rny] == "O":
                    ans.append(command[i])
                    rmx, rmy, bmx, bmy = rx, ry, bx, by
                    while rmx:
                        rmx, rmy, bmx, bmy, k = path[rmx][rmy][bmx][bmy]
                        ans.append(command[k])
                    ans.pop()
                    ans.reverse()
                    print(cnt)
                    print(''.join(ans))
                    exit(0)

                if rnx == bnx and rny == bny:
                    if rcnt > bcnt:
                        rnx -= dx[i]
                        rny -= dy[i]
                    else:
                        bnx -= dx[i]
                        bny -= dy[i]

                if not visited[rnx][rny][bnx][bny]:
                    visited[rnx][rny][bnx][bny] = True
                    Q.append([rnx, rny, bnx, bny, cnt+1])
                    path[rnx][rny][bnx][bny] = (rx, ry, bx, by, i)


    print(-1)
    return
```



#### 전체코드

``` python
# '.', '#', 'O', 'R', 'B' 
# . : 빈칸, # : 벽, O : 구멍, R : 빨간공, B : 파란공
import sys
from collections import deque
from pprint import pprint
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
path = [[[[[0, 0, 0, 0, 0] for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
command = ['U', 'R', 'D', 'L']
ans = list()

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

        if cnt > 10:
            print(-1)
            exit(0)

        for i in range(4):
            rnx, rny, rcnt = move(rx, ry, i)
            bnx, bny, bcnt = move(bx, by, i)

            if board[bnx][bny] != "O":
                if board[rnx][rny] == "O":
                    ans.append(command[i])
                    rmx, rmy, bmx, bmy = rx, ry, bx, by
                    while rmx:
                        rmx, rmy, bmx, bmy, k = path[rmx][rmy][bmx][bmy]
                        ans.append(command[k])
                    print(ans)
                    ans.pop()
                    ans.reverse()
                    print(cnt)
                    print(''.join(ans))
                    exit(0)

                if rnx == bnx and rny == bny:
                    if rcnt > bcnt:
                        rnx -= dx[i]
                        rny -= dy[i]
                    else:
                        bnx -= dx[i]
                        bny -= dy[i]

                if not visited[rnx][rny][bnx][bny]:
                    visited[rnx][rny][bnx][bny] = True
                    Q.append([rnx, rny, bnx, bny, cnt+1])
                    path[rnx][rny][bnx][bny] = (rx, ry, bx, by, i)


    print(-1)
    return


rx, ry, bx, by = 0, 0, 0, 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            rx, ry = i, j
        if board[i][j] == 'B':
            bx, by = i, j

BFS(rx, ry, bx, by)

```

