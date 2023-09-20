# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# N, M = map(int, input().split())
# campus = [list(input().rstrip()) for _ in range(N)]
# visited = [[False] * M for _ in range(N)]
# dx = [0, 0, 1, -1]
# dy = [-1, 1, 0, 0]
# cnt = 0

# def DFS(i, j):
#     global cnt
    
#     for k in range(4):
#         nx = j + dx[k]
#         ny = i + dy[k]

#         if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx]:
#             if campus[ny][nx] == "X":
#                 continue
#             if campus[ny][nx] == "P":
#                 cnt += 1
#             visited[ny][nx] = True
#             DFS(ny, nx)

# for i in range(N):
#     for j in range(M):
#         if campus[i][j] == "I" and not visited[i][j]:
#             visited[i][j] = True
#             DFS(i, j)

# if cnt:
#     print(cnt)
# else:
#     print("TT")

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
campus = [list(input().rstrip()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
cnt = 0

def BFS(i, j):
    global cnt
    Q = deque([[i, j]])

    while Q:
        y, x = Q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx]:
                if campus[ny][nx] == "X":
                    continue
                if campus[ny][nx] == "P":
                    cnt += 1
                visited[ny][nx] = True
                Q.append([ny, nx])

for i in range(N):
    for j in range(M):
        if campus[i][j] == "I" and not visited[i][j]:
            visited[i][j] = True
            BFS(i, j)

if cnt:
    print(cnt)
else:
    print("TT")