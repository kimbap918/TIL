from collections import deque
from pprint import pprint
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())
board = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[0] * M for _ in range(N)] for _ in range(H)]
dx = [1, -1, 0, 0, 0, 0] 
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
# pprint(board)
Q = deque()

def BFS():
    while Q:
        a, b, c = Q.popleft()

        for i in range(6):
            h = a + dz[i]
            n = b + dy[i]
            m = c + dx[i]
            
            if h < 0 or h >= H or n < 0 or n >= N or m < 0 or m >= M:
                continue

            if board[h][n][m] == 0 and visited[h][n][m] == 0:
                Q.append([h, n, m])
                board[h][n][m] = board[a][b][c]+1
                visited[h][n][m] = 1

for k in range(H):
    for i in range(N):
        for j in range(M):  
            if board[k][i][j] == 1 and visited[k][i][j] == 0:
                visited[k][i][j] = 1
                Q.append([k, i, j])

BFS()                
cnt = 0

for i in board:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        cnt = max(cnt, max(j))

print(cnt-1)


