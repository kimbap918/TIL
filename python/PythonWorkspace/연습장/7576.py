from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
Q = deque()
cnt = 0

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            Q.append([i, j])

def BFS():
    while Q:
        a, b = Q.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < N and 0 <= y < M and board[x][y] == 0:
                board[x][y] = board[a][b] + 1
                Q.append([x, y])

BFS()
for i in board:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    cnt = max(cnt, max(i))

print(cnt-1)

