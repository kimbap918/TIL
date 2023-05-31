# from collections import deque
# import sys
# input = sys.stdin.readline

# T = int(input())
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]

# def BFS(h, w):
#     global cnt
#     Q = deque([[h, w]])

#     while Q:
#         y, x = Q.popleft()
#         for i in range(4):
#             ny = y + dy[i]
#             nx = x + dx[i]
#             if 0 <= nx < W and 0 <= ny < H and graph[ny][nx] == '#' and not visited[ny][nx]:
#                 visited[ny][nx] = True
#                 Q.append([ny, nx])


# for _ in range(T):
#     cnt = 0
#     H, W = map(int, input().split())
#     visited = [[False] * W for _ in range(H)]
#     graph = [list(input().rstrip()) for _ in range(H)]

#     for i in range(H):
#         for j in range(W):
#             if graph[i][j] == '#' and not visited[i][j]:
#                 visited[i][j] = True
#                 BFS(i, j)
#                 cnt += 1
#     print(cnt)



import sys
input = sys.stdin.readline

T = int(input())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def DFS(h, w):
    visited[h][w] = True

    for i in range(4):
        ny = h + dy[i]
        nx = w + dx[i]
        if 0 <= nx < W and 0 <= ny < H and graph[ny][nx] == '#' and not visited[ny][nx]:
            DFS(ny, nx)

for _ in range(T):
    cnt = 0
    H, W = map(int, input().split())
    visited = [[False] * W for _ in range(H)]
    graph = [list(input().rstrip()) for _ in range(H)]

    for i in range(H):
        for j in range(W):
            if graph[i][j] == '#' and not visited[i][j]:
                DFS(i, j)
                cnt += 1
    print(cnt)
