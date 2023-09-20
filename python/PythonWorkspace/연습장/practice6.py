import sys
from pprint import pprint
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0, -2, 2, 0, 0]
dy = [0, 0, -1, 1, 0, 0, -2, 2]

def BFS(i, j):
    global cnt
    Q = deque()
    Q.append([i, j])
    arr[i][j] = 0
    while Q:
        a, b = Q.popleft()
        for i in range(8):
            x = a + dx[i]
            y = b + dy[i]
            if x < 0 or x >= length or y < 0 or y >= length:
                continue
            if arr[x][y] == 1:
                arr[x][y] = 0
                cnt += 1

N, M = map(int, input().split())
cnt = 0
arr = []
# 0 = 비어있는 위치
# 1 = 개미가 있는 위치
# 2 = 진딧물이 있는 위치
for i in range(N):
    position = list(map(int, input().split()))
    arr.append(position)
length = len(arr)

for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            BFS(i, j)

print(cnt)
