import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
event = [list(map(int, input().split())) for _ in range(M)]
visited = [list(False for _ in range(len(event[0]))) for _ in range(M)]
arr = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def BFS(j, i):
    Q = deque([[j, i]])

    while Q:
        y, x = Q.popleft()
        for k in range(4):
            y = y + dy[i]
            x = x + dx[i]
            if 0 <= x < len(event[0]) and 0 <= y < M and event[y][x] == num:
                visited[y][x] = True
                Q.append([y, x])
                arr.append(event[y][x])
                print(arr)


for i in range(len(event[0])):
    for j in range(M):
        if event[j][i] and not visited[j][i]:
            visited[j][i] = True
            num = event[j][i]
            BFS(j, i)

print(visited)