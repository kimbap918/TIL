from collections import deque
from pprint import pprint
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = [list(map(int, input().split())) for _ in range(N)]
visited = [list(False for _ in range(M)) for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def BFS(i, j):
    Q = deque([[i, j]])
    while Q:
        x, y = Q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if S[nx][ny] == 1 and not visited[nx][ny]:
                Q.append([nx, ny])
                visited[nx][ny] = True
                S[nx][ny] = 0


for i in range(N):
    for j in range(M):
        if S[i][j] == 0 and not visited[i][j]:
            visited[i][j] = True
            BFS(i, j)

# if 0 not in visited:
#     print(-1)
# else:
#     print(ans-1)


