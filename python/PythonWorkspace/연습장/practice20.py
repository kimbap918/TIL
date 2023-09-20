import sys
from pprint import pprint
from collections import deque
input = sys.stdin.readline

N = int(input())
x, y = map(int, input().split())
x, y= x-1, y-1
M = [list(map(int, input().split())) for _ in range(N)]
visited = [list(0 for _ in range(N)) for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
K = M[x][y]
ans = 0

def BFS(i, j):
    global ans
    Q = deque([[i, j]])
    visited[i][j] = 1
    cnt = 0
    while Q:
        a, b = Q.popleft()
        cnt += 1
        for k in range(4):
            nx = a + dx[k]
            ny = b + dy[k]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if visited[nx][ny] or M[nx][ny] != M[a][b]:
                continue
            visited[nx][ny] = 1
            Q.append([nx, ny])
    # ans = max(cnt, ans)


for i in range(N):
    for j in range(N):
        if visited[i][j] or M[i][j] != K:
            continue
        BFS(i, j)
        ans += 1

print(ans)

