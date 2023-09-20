import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
photo = [list(input().rstrip()) for _ in range(M)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    cnt = 1
    queue = deque([(x, y)])
    photo[x][y] = '.'

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N and photo[nx][ny] == '#':
                cnt += 1
                photo[nx][ny] = '.'
                queue.append((nx, ny))

    return cnt



object_count = 0
max_size = 0

for i in range(M):
    for j in range(N):
        if photo[i][j] == '#':
            size = bfs(i, j)
            object_count += 1
            max_size = max(max_size, size)

print(object_count)
print(max_size)
