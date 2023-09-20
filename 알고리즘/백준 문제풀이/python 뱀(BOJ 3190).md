

## 파이썬 뱀(BOJ 3190)

<br>

## 문제

'Dummy' 라는 도스게임이 있다. 이 게임에는 뱀이 나와서 기어다니는데, 사과를 먹으면 뱀 길이가 늘어난다. 뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.

게임은 NxN 정사각 보드위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있다. 보드의 상하좌우 끝에 벽이 있다. 게임이 시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다. 뱀은 처음에 오른쪽을 향한다.

뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.

- 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
- 만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
- 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
- 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.

사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.

<br>

## 입력

첫째 줄에 보드의 크기 N이 주어진다. (2 ≤ N ≤ 100) 다음 줄에 사과의 개수 K가 주어진다. (0 ≤ K ≤ 100)

다음 K개의 줄에는 사과의 위치가 주어지는데, 첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미한다. 사과의 위치는 모두 다르며, 맨 위 맨 좌측 (1행 1열) 에는 사과가 없다.

다음 줄에는 뱀의 방향 변환 횟수 L 이 주어진다. (1 ≤ L ≤ 100)

다음 L개의 줄에는 뱀의 방향 변환 정보가 주어지는데, 정수 X와 문자 C로 이루어져 있으며. 게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다. X는 10,000 이하의 양의 정수이며, 방향 전환 정보는 X가 증가하는 순으로 주어진다.

<br>

## 출력

첫째 줄에 게임이 몇 초에 끝나는지 출력한다.

<br>

## 예제 입력 1 

```
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D
```

## 예제 출력 1 

```
9
```

## 예제 입력 2 

```
10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L
```

## 예제 출력 2 

```
21
```

## 예제 입력 3 

```
10
5
1 5
1 3
1 2
1 6
1 7
4
8 D
10 D
11 D
13 L
```

## 예제 출력 3 

```
13
```

<br>

## 📝 풀어보기

보드의 크기 N, 사과의 개수 K를 입력받는다.

보드는 N x N으로 이뤄져있는데, 보드를 전부 0으로 초기화 시켜준다. 여기서 뱀이 있는 위치는 1로, 사과의 위치는 2로 지정을 해줄것이다.

이번에도 방위를 탐지하고 뱀을 명령에 따라 회전시키기 위해 dx, dy에 좌표를 저장해둔다. 이번 문제는 좌표값의 저장 순서가 중요하다.

다음 K개의 줄에 걸쳐서 사과의 위치정보를 입력받는다. board의 인덱스는 0부터 시작하기 때문에, 입력받은 a, b에서 -1한 좌표에 사과를 표시한다.

``` python
from collections import deque
N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(K):
    a, b = map(int, input().split())
    board[a-1][b-1] = 2
```

<br>

L개의 줄에는 뱀의 방향 정보가 주어진다. 

뱀의 방향 정보를 담기 위해 transfer 딕셔너리를 만들어둔다.

L만큼 반복하면서 X초와 C의 각도정보를 저장한다. X는 int로 변환 후 transfer에 담아준다.

``` python
L = int(input())
transfer = dict()

for _ in range(L):
    X, C = map(str, input().split())
    X = int(X)
    transfer[X] = C
```

<br>

뱀의 초기 위치를 설정해준다.

뱀은 시작할 때 가장 왼쪽 가장 위에 위치하므로 0, 0의 좌표에서 시작하며, 오른쪽 방향을 보고 이동한다.

뱀이 있는곳을 보드에서 구분하기 위해 1로 표시한다.

게임이 몇 초만에 끝나는지 확인하기 위해 cnt를 만들고, 뱀이 바라보는 각도를 0으로 저장해둔다.

명령어에 따른 뱀의 각도 변경을 하는 함수 turn을 정의한다.

명령어가 L(왼쪽) 이면 초기에 설정된 0에서  - 1을 하므로  = -1,  여기에 4로 나눈 나머지는 3이다. 즉, dx, dy의 3번 인덱스로, 왼쪽을 이동하게 된다.

명령어가 D(오른쪽) 이면 초기에 설정된 0에서 +1을 하므로 = 1, 여기에 4로 나눈 나머지는 1이다. 즉, dx, dy의 1번 인덱스로, 오른쪽을 이동하게 된다. 

이와 같은 방법으로 진행에 따라 뱀이 바라보는 각도 degree가 바껴도 바라보고 있는 방향에서 왼쪽, 오른쪽을 변경한다. 

``` python
# 뱀의 초기 위치
x, y = 0, 0
# 뱀이 있는곳을 1로 표시
board[x][y] = 1
# 경과시간
cnt = 0
# 뱀이 바라보는 각도
degree = 0

def turn(command):
    global degree

    if command == "L":
        degree = (degree - 1) % 4
    elif command == "D":
        degree = (degree + 1) % 4
```

<br>

뱀의 진행을 확인하고, 게임이 끝나기까지 몇 초가 진행되었는지를 파악할 함수 solve를 정의한다.

뱀의 초기 위치 0, 0를 Q에 삽입한다.

BFS와 유사한 방법으로, while문 안에서 원래 좌표 x, y에서 상하좌우를 탐색하고, 보드 범위 내에서 사과를 발견한 경우라면 해당 보드를 1로 변경시키고 해당 좌표를 Q에 삽입한다.

transfer에는 몇 초 후에 뱀이 진행방향을 변경할지에 대한 정보가 들어있으므로, cnt가 transfer에 들어있는 시간과 맞아떨어진다면 뱀이 방향을 바꿔야한다. 그렇기 때문에 cnt가 transfer에 있으면 turn함수를 실행시킨다.

사과도 뱀도 없는 일반적인 보드의 경우에는 뱀이 해당자리를 지나가기 때문에 해당 보드를 1로 바꿔주고 Q에 해당 좌표를 삽입해준다.

하지만 뱀의 몸이 늘어난것은 아니고 다시 줄어들어야 하기 때문에 tx, ty에 Q에서 좌표값을 꺼내 저장하고, 해당 tx, ty의 좌표는 0으로 변경해준다. 

마찬가지로 cnt값이 transfer안에 있다면 turn함수를 실행시켜준다.

``` python
def solve():
    global cnt, x, y
    Q = deque([[0, 0]])
    
    while True:
        cnt += 1
        x += dx[degree]
        y += dy[degree]

        # 범위 내를 탐지
        if x < 0 or x >= N or y < 0 or y >= N:
            break

        # 사과를 발견한 경우
        if board[x][y] == 2:
            board[x][y] = 1
            Q.append([x, y])
            if cnt in transfer:
                turn(transfer[cnt])

        # 사과도 뱀도 없는 일반적인 보드인 경우
        elif board[x][y] == 0:
            board[x][y] = 1
            Q.append([x, y])
            tx, ty = Q.popleft()
            board[tx][ty] = 0
            if cnt in transfer:
                turn(transfer[cnt])
        
        else:
            break
solve()
```

<br>

#### 전체코드

``` python
from collections import deque
N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(K):
    a, b = map(int, input().split())
    board[a-1][b-1] = 2

L = int(input())
transfer = dict()

for _ in range(L):
    X, C = map(str, input().split())
    X = int(X)
    transfer[X] = C

# 뱀의 초기 위치
x, y = 0, 0
# 뱀이 있는곳을 1로 표시
board[x][y] = 1
# 경과시간
cnt = 0
# 뱀이 바라보는 각도
degree = 0

def turn(command):
    global degree

    if command == "L":
        degree = (degree - 1) % 4
    elif command == "D":
        degree = (degree + 1) % 4


def solve():
    global cnt, x, y
    Q = deque([[0, 0]])
    
    while True:
        cnt += 1
        x += dx[degree]
        y += dy[degree]

        # 범위 내를 탐지
        if x < 0 or x >= N or y < 0 or y >= N:
            break

        # 사과를 발견한 경우
        if board[x][y] == 2:
            board[x][y] = 1
            Q.append([x, y])
            if cnt in transfer:
                turn(transfer[cnt])

        # 사과도 뱀도 없는 일반적인 보드인 경우
        elif board[x][y] == 0:
            board[x][y] = 1
            Q.append([x, y])
            tx, ty = Q.popleft()
            board[tx][ty] = 0
            if cnt in transfer:
                turn(transfer[cnt])
        
        else:
            break
solve()

print(cnt)
```

