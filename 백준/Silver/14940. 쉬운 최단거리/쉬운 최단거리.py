from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
res = [[-1] * M for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def BFS(y, x):
    q = deque()
    q.append((y, x))
    res[y][x] = 0  # 시작점 거리 0

    while q:
        cy, cx = q.popleft()

        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]

            if 0 <= ny < N and 0 <= nx < M:
                if board[ny][nx] == 1 and res[ny][nx] == -1:
                    res[ny][nx] = res[cy][cx] + 1
                    q.append((ny, nx))

# 시작 좌표 찾기
for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            start_y, start_x = i, j

BFS(start_y, start_x)

# 최종 출력: 벽은 0으로, 나머지는 res 값 사용
for i in range(N):
    row = []
    for j in range(M):
        if board[i][j] == 0:
            row.append(0)
        else:
            row.append(res[i][j])
    print(' '.join(map(str, row)))
