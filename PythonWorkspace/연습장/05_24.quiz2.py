# 2차원 배열에서 조건에 따른 #의 영역 탐색하기
# 분산된 #의 영역 개수 찾기
# #의 영역 중 가장 크기가 클때 크기 찾기
# component(연결요소) 찾기

# DFS와 BFS로 풀 수 있는 문제가 있다면, BFS로 문제를 풀것
# 파이썬은 재귀에 취약하다.

# 시작지점이 여러개 -> visited를 사용해 방문 확인

# DX/DY기법
# [0, 0, 1, -1]
# [1, -1, 0, 0]

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(str, input().rstrip())) for _ in range(M)]
visited = [[False for _ in range(N)] for _ in range(M)]
each = 0
ans = 0

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def BFS(i, j):
    global cnt
    global ans
    Q = deque()
    Q.append([i, j])

    while Q:
        y, x = Q.popleft()
        cnt += 1
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if ny < 0 or nx < 0 or ny >= M or nx >= N or visited[ny][nx] or matrix[ny][nx] == '.':
                continue    
            visited[ny][nx] = True
            Q.append([ny, nx])
    ans = max(ans, cnt)


for i in range(M):
    for j in range(N):
        if matrix[i][j] == '#' and not visited[i][j]:
            visited[i][j] = True
            each += 1
            cnt = 0
            BFS(i, j)


print(each)
print(ans)
