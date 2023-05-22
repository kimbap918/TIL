import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
S = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
update = [[0 for _ in range(M)] for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def DFS(i, j):
    y, x = i, j
    for k in range(4):
        ny, nx = y + dy[k], x + dx[k]
        if ny < 0 or nx < 0 or ny >= N or nx >= M:
            continue
        if visited[ny][nx] or not S[ny][nx]:
            continue
        visited[ny][nx] = 1
        DFS(ny, nx)

day = 0
while 1:
    island = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] or not S[i][j]:
                continue
            visited[i][j] = 1
            island += 1
            DFS(i, j)
    
    if island > 1:
        print(day)
        exit(0)
        
    if island == 0:
        print(-1)
        exit(0)
        
    for i in range(N):
        for j in range(M):
            for k in range(4):
                ny, nx = i + dy[k], j + dx[k]
                if ny < 0 or nx < 0 or ny >= N or nx >= M:
                    continue
                if not S[ny][nx]:
                    update[i][j] = 1
                    
    for i in range(N):
        for j in range(M):
            if update[i][j]:
                S[i][j] = 0
    
    for i in range(N):
        for j in range(M):
            update[i][j] = visited[i][j] = 0
    day += 1