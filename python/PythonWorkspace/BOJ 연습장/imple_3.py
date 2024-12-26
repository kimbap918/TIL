N, M = map(int, input().split())
x, y, direction = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
d = [[0] * M for _ in range(N)]
d[x][y] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


cnt = 1
turn = 0

while True:
    left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and board[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        cnt += 1
        turn = 0
        continue

    else:
        turn += 1

    if turn == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if board[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn = 0

print(cnt)