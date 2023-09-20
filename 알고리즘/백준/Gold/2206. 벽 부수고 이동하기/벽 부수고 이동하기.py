import sys
from collections import deque
from pprint import pprint
input = sys.stdin.readline


N, M = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 시작지점의 좌표 x, y, cnt
def BFS(x, y, cnt):
    Q = deque([[0, 0, 1]])
    visited[x][y][cnt] = 1
    while Q:
        x, y, cnt = Q.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y][cnt]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            # 벽을 부수지 않고 이동하기
            if graph[nx][ny] == 0 and visited[nx][ny][cnt] == 0:
                Q.append([nx, ny, cnt])
                visited[nx][ny][cnt] = visited[x][y][cnt] + 1
            # 벽을 부순다
            if graph[nx][ny] == 1 and cnt == 1:
                Q.append([nx, ny, cnt-1])
                visited[nx][ny][cnt-1] = visited[x][y][cnt] + 1
    return -1

# 시작지점 x,y좌표와 남은 카운트 1
print(BFS(0, 0, 1))
