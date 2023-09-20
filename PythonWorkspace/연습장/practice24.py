from collections import deque
import sys
from pprint import pprint
input = sys.stdin.readline

N, M = map(int, input().split())
picture = [list(map(str, input().rstrip())) for _ in range(M)]
visited = [list(False for _ in range(N)) for _ in range(M)]
ans = []
shape = 0
cnt = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def BFS(i, j):
    global shape
    global cnt
    Q = deque([[i, j]])
    shape += 1
    while Q:
        y, x = Q.popleft()
        for k in range(4):
            x = x + dx[k]
            y = y + dy[k]
            if 0 <= x < N and 0 <= y < M and picture[y][x] == "#" and not visited[y][x]:
                visited[y][x] = True
                cnt += 1
                ans.append(cnt)



for i in range(M):
    for j in range(N):
        if picture[i][j] == "#" and not visited[i][j]:
            visited[i][j] = True
            BFS(i, j)
            
print(sum(ans))
print(shape)


