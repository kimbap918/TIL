from collections import deque
from pprint import pprint
import sys
input = sys.stdin.readline

# 탐색 좌표
# 위, 아래, 우, 좌
# (0, 1), (0, -1), (1, 0), (-1, 0)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(graph, a, b):
    length = len(graph)
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= length or ny < 0 or ny >= length:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count


N = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
# pprint(graph)

cnt = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            cnt.append(bfs(graph, i, j))

# 오름차순 정렬
cnt.sort()
# 총 단지 수 출력
print(len(cnt))
# 단지 내 집 수 출력
for i in range(len(cnt)):
    print(cnt[i])