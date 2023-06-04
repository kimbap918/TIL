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

