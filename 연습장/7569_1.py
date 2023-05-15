from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())
board = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[list(False for _ in range(M)) for _ in range(N)] for _ in range(H)]
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
Q = deque()

# (높이, 세로, 가로)
def BFS():
    while Q:
        a, b, c = Q.popleft()
        for l in range(6):
            z = a + dz[l] # 높이
            y = b + dy[l] # 세로
            x = c + dx[l] # 가로

            # 탐색 범위를 넘어서면 건너뛴다.
            if 0 > x or x >= M or 0 > y or y >= N or 0 > z or z >= H:
                continue
            if board[z][y][x] == 0 and visited[z][y][x] == False:
                visited[z][y][x] = True
                board[z][y][x] = board[a][b][c] + 1
                Q.append([z, y, x])

# N = 가로칸(x축)
# M = 세로칸(y축)
# H = 높이(z축)
for i in range(H): # 높이
    for j in range(N): # 세로
        for k in range(M): # 가로
            if board[i][j][k] == 1 and visited[i][j][k] == False:
                visited[i][j][k] = True
                Q.append([i, j, k])


BFS() # (높이, 세로, 가로)
cnt = 0
for i in board:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        cnt = max(cnt, max(j))

print(cnt-1)