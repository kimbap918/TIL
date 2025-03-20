N = int(input()) # 보드의 크기
K = int(input()) # 사과의 개수
dx = [0, 1, 0, -1] # 동, 남, 서 북
dy = [1, 0, -1, 0]
board = list([0] * (N+1) for _ in range(N+1))
directions = []

for _ in range(K):
    row, col = map(int, input().split())
    board[row][col] = 1
    # 3 4
    # 2 5
    # 5 3

L = int(input()) # 방향 변환 횟수
for _ in range(L):
    X, C = input().split() # X초가 끝난 뒤에 L(완쪽) D(오른쪽)으로 90도 회전
    directions.append((int(X), C))

def turn(dir, C):
    # L이 왼쪽, 
    # 동(0, 1) -> 북(-1, 0), 남(1, 0) -> 동(0, 1)
    # 서(0, -1) -> 남(1, 0), 북(-1, 0) -> 서(0, -1)
    if C == "L": 
        dir = (dir - 1) % 4
    else:
        dir = (dir + 1) % 4
    return dir

def simulate():
    x, y = 1, 1
    board[x][y] = 2 # 뱀의 위치
    direction = 0
    time = 0
    index = 0

    q = [(x, y)]
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 1 <= nx and nx <= N and 1 <= ny and ny <= N and board[nx][ny] != 2:
            if board[nx][ny] == 0:
                board[nx][ny] = 2
                q.append((nx,ny))
                px, py = q.pop(0)
                board[px][py] = 0

            if board[nx][ny] == 1:
                board[nx][ny] = 2
                q.append((nx,ny))
        else:
            time += 1
            break

        x, y = nx, ny
        time += 1
        if index < L and time == directions[index][0]:
            direction = turn(direction, directions[index][1])
            index += 1
    return time

print(simulate())

