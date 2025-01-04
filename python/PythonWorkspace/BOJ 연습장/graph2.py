from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]
# print(board)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if board[nx][ny] == 0:
                continue
            if board[nx][ny] == 1:
                board[nx][ny] = board[x][y]+1
                queue.append((nx, ny))

    return board[N-1][M-1]


print(bfs(0,0))