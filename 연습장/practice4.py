# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
graph = list([0] * N for _ in range(N))
length = len(graph)
cnt = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
# (1, 1) -> (1, 2) (2, 1)
# (4, 4) -> (4, 3) (3, 3)
# (3, 3) -> ()
for i in range(K):
    x, y = map(int, input().split())
    x, y = x-1, y-1
    graph[x][y] += 1
    cnt += 1
    for j in range(4):
        nx = x + dx[j]
        ny = y + dy[j]
        if nx < 0 or nx >= length or ny < 0 or ny >= length:
            continue
        if graph[nx][ny] == 0:
            graph[nx][ny] = 1
            cnt += 1
        else:
            graph[nx][ny] += 1
            cnt += 1
print(cnt)
