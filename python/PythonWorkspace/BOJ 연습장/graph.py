N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]

def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    if board[x][y] == 0:
        board[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

res = 0

for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            res += 1            
print(res)
