import sys
input = sys.stdin.readline

def BFS(x,y):           
    queue = [(x,y)]
    matrix[x][y] = 0 

    while queue:
        x,y = queue.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            
            if matrix[nx][ny] == 1 :
                queue.append((nx,ny))
                matrix[nx][ny] = 0

# 테스트 케이스 수
T = int(input()) 

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(T):
    # 배추밭의 가로, 세로, 배추가 심어진 위치의 개수
    M, N, K = map(int, input().split())
    matrix = [[0]*(N) for _ in range(M)]
    cnt = 0

    for j in range(K):
        x,y = map(int, input().split())
        matrix[x][y] = 1

    for a in range(M):
        for b in range(N):
            if matrix[a][b] == 1:
                BFS(a,b)
                cnt += 1

    print(cnt)