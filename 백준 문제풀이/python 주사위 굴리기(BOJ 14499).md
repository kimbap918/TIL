

## 파이썬 주사위 굴리기(BOJ 14499)

<br>

## 문제

크기가 N×M인 지도가 존재한다. 지도의 오른쪽은 동쪽, 위쪽은 북쪽이다. 이 지도의 위에 주사위가 하나 놓여져 있으며, 주사위의 전개도는 아래와 같다. 지도의 좌표는 (r, c)로 나타내며, r는 북쪽으로부터 떨어진 칸의 개수, c는 서쪽으로부터 떨어진 칸의 개수이다. 

```
  2
4 1 3
  5
  6
```

주사위는 지도 위에 윗 면이 1이고, 동쪽을 바라보는 방향이 3인 상태로 놓여져 있으며, 놓여져 있는 곳의 좌표는 (x, y) 이다. 가장 처음에 주사위에는 모든 면에 0이 적혀져 있다.

지도의 각 칸에는 정수가 하나씩 쓰여져 있다. 주사위를 굴렸을 때, 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다. 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.

주사위를 놓은 곳의 좌표와 이동시키는 명령이 주어졌을 때, 주사위가 이동했을 때 마다 상단에 쓰여 있는 값을 구하는 프로그램을 작성하시오.

주사위는 지도의 바깥으로 이동시킬 수 없다. 만약 바깥으로 이동시키려고 하는 경우에는 해당 명령을 무시해야 하며, 출력도 하면 안 된다.

<br>

## 입력

첫째 줄에 지도의 세로 크기 N, 가로 크기 M (1 ≤ N, M ≤ 20), 주사위를 놓은 곳의 좌표 x, y(0 ≤ x ≤ N-1, 0 ≤ y ≤ M-1), 그리고 명령의 개수 K (1 ≤ K ≤ 1,000)가 주어진다.

둘째 줄부터 N개의 줄에 지도에 쓰여 있는 수가 북쪽부터 남쪽으로, 각 줄은 서쪽부터 동쪽 순서대로 주어진다. 주사위를 놓은 칸에 쓰여 있는 수는 항상 0이다. 지도의 각 칸에 쓰여 있는 수는 10 미만의 자연수 또는 0이다.

마지막 줄에는 이동하는 명령이 순서대로 주어진다. 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4로 주어진다.

<br>

## 출력

이동할 때마다 주사위의 윗 면에 쓰여 있는 수를 출력한다. 만약 바깥으로 이동시키려고 하는 경우에는 해당 명령을 무시해야 하며, 출력도 하면 안 된다.

<br>

## 예제 입력 1 

```
4 2 0 0 8
0 2
3 4
5 6
7 8
4 4 4 1 3 3 3 2
```

## 예제 출력 1 

```
0
0
3
0
0
8
6
3
```

## 예제 입력 2 

```
3 3 1 1 9
1 2 3
4 0 5
6 7 8
1 3 2 2 4 4 1 1 3
```

## 예제 출력 2 

```
0
0
0
3
0
1
0
6
0
```

## 예제 입력 3 

```
2 2 0 0 16
0 2
3 4
4 4 4 4 1 1 1 1 3 3 3 3 2 2 2 2
```

## 예제 출력 3 

```
0
0
0
0
```

## 예제 입력 4 

```
3 3 0 0 16
0 1 2
3 4 5
6 7 8
4 4 1 1 3 3 2 2 4 4 1 1 3 3 2 2
```

## 예제 출력 4 

```
0
0
0
6
0
8
0
2
0
8
0
2
0
8
0
2
```

<br>

## 📝 풀어보기

지도의 세로 N, 가로 M, 주사위의 좌표 x, y 명령의 개수 K를 입력 받는다. 주의해야할 점은 여기서 x는 세로, y는 가로다.

지도의 정보를 입력받아 board에 저장한다.

command에는 K개만큼의 명령어를 입력받아 저장해둔다.

주사위는 처음에 모든 면에 0이 적혀있으므로 0을 6개 저장해둔다.

위, 아래, 좌, 우를 탐색하기 위해 dx, dy에 좌표를 저장해둔다.

``` python
# 세로, 가로, 주사위의 좌표(세로 = x, 가로 = y), 명령의 개수
N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
command = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0]

# 동, 서, 북, 남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
```

<br>

주사위의 회전을 계산하는 turn함수를 정의한다.

```
  2
4 1 3
  5
  6
```

문제에 제시된 대로 명령어는 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4로 되어있다.

해당 명령어에 따라서 위의 주사위 전개도가 움직이는 방향을 저장한다.

``` python
def turn(direction):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    # 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
    if direction == 1: # 동쪽인 경우 주사위가 오른쪽으로 회전
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
    elif direction == 2: # 서쪽인 경우 주사위가 왼쪽으로 회전
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
    elif direction == 3: # 북쪽인 경우 주사위가 위로 회전
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b
    else: # 남쪽인 경우 주사위가 아래로 회전
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e
```

<br>

주사위의 윗면에 쓰인 수를 출력할 solve함수를 정의한다.

입력된 명령어를 순회하며 nx, ny에 해당 명령어의 좌표값을 더해준다.

더해진 좌표가 지도의 범위를 벗어나면 더했던 좌표를 원래대로 되돌리고 건너뛴다.

그외엔 turn함수를 사용해서 명령어에 따른 주사위의 움직임을 저장하고, `board[nx][ny]`가 0이라면, 보드의 값을 dice의 마지막 인덱스 값으로 업데이트한다.

그외엔 다이스의 마지막 값을 `board[nx][ny]`로 업데이트 한다. 그리고 해당 보드는 0으로 바꿔준다.

그리고 dice의 0번째 인덱스 값을 하나씩 출력한다.

```python
nx, ny = x, y
def solve():
    global nx, ny
    for i in command:
        nx += dx[i-1]
        ny += dy[i-1]
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            nx -= dx[i-1]
            ny -= dy[i-1]
            continue
        turn(i)
        if board[nx][ny] == 0:
            board[nx][ny] = dice[-1]
        else:
            dice[-1] = board[nx][ny]
            board[nx][ny] = 0
        print(dice[0])
solve()
```



#### 전체코드

``` python

# 세로, 가로, 주사위의 좌표(세로 = x, 가로 = y), 명령의 개수
N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
command = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0]

# 동, 서, 북, 남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def turn(direction):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    # 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
    if direction == 1: # 동쪽인 경우 주사위가 오른쪽으로 회전
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
    elif direction == 2: # 서쪽인 경우 주사위가 왼쪽으로 회전
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
    elif direction == 3: # 북쪽인 경우 주사위가 위로 회전
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b
    else: # 남쪽인 경우 주사위가 아래로 회전
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e

nx, ny = x, y
def solve():
    global nx, ny
    for i in command:
        nx += dx[i-1]
        ny += dy[i-1]
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            nx -= dx[i-1]
            ny -= dy[i-1]
            continue
        turn(i)
        if board[nx][ny] == 0:
            board[nx][ny] = dice[-1]
        else:
            dice[-1] = board[nx][ny]
            board[nx][ny] = 0
        print(dice[0])
solve()
```

