

## 파이썬 세 번 이내에 사과를 먹자(BOJ 26169)

<br>

## 문제

5 x 5 크기의 보드가 주어진다. 보드는 1 x 1 크기의 정사각형 격자로 이루어져 있다. 보드의 격자는 사과가 1개 있는 격자, 장애물이 있는 격자, 빈칸으로 되어 있는 격자로 구분된다. 격자의 위치는 (*r*, *c*)로 표시한다. *r*은 행 번호, *c*는 열 번호를 나타낸다. 행 번호는 맨 위 위치가 0이고 아래 방향으로 1씩 증가한다. 열 번호는 맨 왼쪽 위치가 0이고 오른쪽으로 1씩 증가한다. 즉, 맨 왼쪽 위 위치가 (0, 0), 맨 아래 오른쪽 위치가 (4, 4)이다.

현재 한 명의 학생이 (*r*, *c*) 위치에 있고 한 번의 이동으로 상, 하, 좌, 우 방향 중에서 한가지 방향으로 한 칸 이동할 수 있다. 학생이 사과가 있는 칸으로 이동하면 해당 칸에 있는 사과를 1개 먹는다. 장애물이 있는 칸으로는 이동할 수 없다. 학생이 지나간 칸은 학생이 해당 칸을 떠나는 즉시 장애물이 있는 칸으로 변경된다. 즉, 학생이 해당 칸에서 상, 하, 좌, 우 방향으로 한 칸 이동하는 즉시 해당 칸은 장애물이 있는 칸으로 변경된다.

학생이 현재 위치 (*r*, *c*)에서 **세 번 이하의 이동**으로 사과를 2개 이상 먹을 수 있으면 1을 출력하고, 그렇지 않으면 0을 출력하자.

<br>

## 입력

첫 번째 줄부터 다섯 개의 줄에 걸쳐 보드의 정보가 주어진다. *i*번째 줄의 *j*번째 수는 보드의 (*i* - 1)번째 행, (*j* - 1)번째 열의 정보를 나타낸다. 보드의 정보가 1이면 해당 칸은 사과가 1개 있는 격자임을 나타내고, 0이면 빈칸이 있는 격자를 나타내고, -1이면 장애물이 있는 격자임을 나타낸다.

다음 줄에 학생의 현재 위치 *r*, *c*가 빈칸을 사이에 두고 순서대로 주어진다.

<br>

## 출력

첫 번째 줄에 학생이 현재 위치 (*r*, *c*)에서 세 번 이하의 이동으로 사과를 2개 이상 먹을 수 있으면 1을 출력하고, 먹을 수 없으면 0을 출력한다.

<br>

## 제한

- 0 ≤ *r*, *c* ≤ 4
- 현재 위치 (*r*, *c*)는 빈칸이다.

<br>

## 예제 입력 1 

```
0 0 1 0 0
0 0 -1 0 0
0 0 1 0 0
1 1 -1 1 0
0 0 0 -1 0
4 1
```

## 예제 출력 1 

```
1
```

(4, 1) -> (3, 1) -> (3, 0)으로 이동하면 사과를 2개 먹을 수 있다.

## 예제 입력 2 

```
0 0 1 0 0
0 0 -1 0 0
0 0 1 0 0
1 0 -1 1 0
0 0 0 -1 0
2 3
```

## 예제 출력 2 

```
0
```

(2, 3) -> (2, 2) -> (2, 3) -> (3, 3) 이동에서 두 번째 (2, 3)에는 장애물이 있으므로 이동할 수 없다.

<br>

## 📝 풀어보기 

백트래킹에 미숙해서 상당히 애를 먹었던 문제다.

<br>

보드가 5x5로 이뤄져있기 때문에 board_size를 5로 지정해뒀다.

board_size만큼 보드의 상태를 입력받아 저장한다. r, c는 학생의 처음 좌표다.

move는 학생의 이동횟수, apple은 학생이 먹은 사과의 수를 기록한다. 

dx, dy는 학생을 기준으로 상하좌우를 탐색한다.

DFS를 실행시켜 얻은 값을 res에 저장하고, res의 값에 따라서 조건을 충족할 수 있으면 1을 출력, 아니면 0을 출력한다.

``` python
board_size = 5
board = [list(map(int, input().split())) for _ in range(board_size)]
r, c = map(int, input().split())
move, apple = 0, 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

res = DFS(board, r, c, apple, move)

if res:
    print(1)
else:
    print(0)
```

<br>

학생의 좌표 row, col를 x, y에 저장한다.

사과를 2회 이상 먹으면 성공한것이기 때문에 True를 반환하고, 3회 이상 이동하면 실패한것이기 때문에 False를 반환하도록 한다.

상하좌우 4방향을 탐색한다. 보드의 범위 내, 그리고 탐색 위치가 -1이 아닌곳에 사과가 있는 경우(1) eaten에 1을 저장해서 사과를 먹었음을 표시한다. 그리고 사과를 먹었으므로 탐색 위치의 값을 0으로 변경해서 빈 공간으로 표시한다.

그리고 현재 위치를 장애물(-1)로 변경을 하고 DFS를 재귀호출한다. 이 때에 apple과 move 변수를 업데이트해 준다.

재귀 호출이 끝난 후에 원래 상태로 복구하기 위해 현재 위치를 0으로 변경하고, 사과를 먹은 경우에 사과를 원래대호 복구한다.

모든 이동방향에 대해 성공경로를 찾으면 True를 반환하고, 실패한 경우 False를 반환한다.

```python
def DFS(arr, row, col, apple, move):
    x, y = row, col
    
    if apple >= 2:
        return True

    if move == 3:
        return False

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < board_size and 0 <= ny < board_size and arr[nx][ny] != -1:
            eaten = 0

            # 사과가 있는 경우
            if arr[nx][ny] == 1:
                eaten = 1
                # 사과를 먹었으므로 빈 칸으로 변경
                arr[nx][ny] = 0

            arr[x][y] = -1 # 현재 위치를 장애물로 변경
            if DFS(arr, nx, ny, apple+eaten, move+1):
                return True    
            arr[x][y] = 0 # 백트래킹 : 원래대로 복구

            if arr[nx][ny] == 1: 
                arr[nx][ny] = 1

    return False
```

<br>

#### 전체코드

```python
import sys
input = sys.stdin.readline

def DFS(arr, row, col, apple, move):
    x, y = row, col
    # 이동이 3회 이하면서 사과를 2개이상 먹었을 경우
    if apple >= 2:
        return True

    if move == 3:
        return False

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < board_size and 0 <= ny < board_size and arr[nx][ny] != -1:
            eaten = 0

            # 사과가 있는 경우
            if arr[nx][ny] == 1:
                eaten = 1
                # 사과를 먹었으므로 빈 칸으로 변경
                arr[nx][ny] = 0

            arr[x][y] = -1 # 현재 위치를 장애물로 변경
            if DFS(arr, nx, ny, apple+eaten, move+1):
                return True    
            arr[x][y] = 0 # 백트래킹 : 원래대로 복구

            # 백트래킹 : 원래대로 복구
            if arr[nx][ny] == 1: 
                arr[nx][ny] = 1

    return False


board_size = 5
board = [list(map(int, input().split())) for _ in range(board_size)]
r, c = map(int, input().split())
move, apple = 0, 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

res = DFS(board, r, c, apple, move)

if res:
    print(1)
else:
    print(0)
```

