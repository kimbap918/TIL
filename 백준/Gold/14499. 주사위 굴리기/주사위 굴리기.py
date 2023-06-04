
# 세로, 가로, 주사위의 좌표, 명령의 개수
N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
command = list(map(int, input().split()))

# 위, 아래, 우, 좌
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dice = [0, 0, 0, 0, 0, 0]

def turn(direction):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    # 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
    if direction == 1: # 동쪽인 경우 주사위가 오른쪽으로 회전
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
    elif direction == 2: # 서쪽인 경우 주사위가 왼쪽으로 회전
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
    elif direction == 3: # 남쪽인 경우 주사위가 아래로 회전
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b
    else:
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
