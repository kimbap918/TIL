import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
S = [input().rstrip() for _ in range(M)]
V = [[0 for _ in range(N)] for _ in range(M)]
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

component, ans = 0, 0
for i in range(M):
    for j in range(N):
        if V[i][j] or S[i][j] == '.':
            continue
        cnt = 0
        component += 1
        V[i][j] = 1
        Q = deque()
        Q.append((i, j))
        while Q:
            y, x = Q.popleft()
            cnt += 1
            for k in range(4):
                ny, nx = y + dy[k], x + dx[k]
                if ny < 0 or nx < 0 or ny >= M or nx >= N or V[ny][nx] or S[ny][nx] == '.':
                    continue
                V[ny][nx] = 1
                Q.append((ny, nx))
        ans = max(ans, cnt)

print(component, ans, sep='\n')