from collections import deque
import sys
from copy import deepcopy
input = sys.stdin.readline

def BFS():
    global ans
    Q = deque()
    # 깊은 복사
    tmp = deepcopy(graph)
    for i in range(N):
        for j in range(M):
            if tmp[i][j] == 2:
                Q.append([i, j])


    while Q:
        x, y = Q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                Q.append([nx, ny])
    cnt = 0
    for i in range(N):
        cnt += tmp[i].count(0)
    ans = max(ans, cnt)

def makeWall(cnt):
    # 기둥 3개가 전부 설치되면 BFS실행
    if cnt == 3:
        BFS()
        return
    
    for i in range(N):
        for j in range(M):
            # 기둥이 없는 곳에 기둥을 세운다.
            if graph[i][j] == 0:
                graph[i][j] = 1
                makeWall(cnt+1)
                # 원래대로 되돌림(백트래킹)
                graph[i][j] = 0

    

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
ans = 0

makeWall(0)
print(ans)
