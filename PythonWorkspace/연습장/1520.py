import sys
input = sys.stdin.readline

def dfs(x, y):
    # 목적지 도착시 1을 추가하여 이동경로에 모두 추가
    if x == M-1 and y == N-1:
        return 1
    
    # 방문하지 않은 곳을 방문처리
    if dp[x][y] == -1:
        dp[x][y] = 0
        
        # 4방위 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 탐색 범위가 보드를 초과하지 않고
            if 0 <= nx < M and 0 <= ny < N:
                # 현재 위치가 탐색위치보다 높은곳에 있다면(내리막길)
                if board[x][y] > board[nx][ny]:
                    # dp[x][y]에 탐색위치의 dfs를 추가
                    dp[x][y] += dfs(nx, ny)
    
    return dp[x][y]

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
dp = [[-1 for _ in range(N)] for _ in range(M)]

print(dfs(0, 0))
