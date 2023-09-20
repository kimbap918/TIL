N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
max_val = max(map(max, board))
ans = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def DFS(y, x, depth, s):
    global ans
    # 남은 블럭이 모두 최댓값이라 해도 현재의 최대를 넘길수 없을때 조기종료 해버림
    if s + max_val * (4-depth) <= ans:
        return
    if depth >= 4:
        if ans < s:
            ans = s
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                # dfs수행중에 2까지일때 시작점을 자기자신으로 하는 dfs를 호출함
                # ㅗ 모양은 DFS처리 중에 깊이가 2일때 다시 자기자신을 시작점으로 dfs를 호출해야한다.
                if depth == 2:
                    visited[ny][nx] = True
                    DFS(y, x, depth+1, s+board[ny][nx])
                    visited[ny][nx] = False
                
                visited[ny][nx] = True
                DFS(ny, nx, depth+1, s+board[ny][nx])
                visited[ny][nx] = False

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        DFS(i, j, 1, board[i][j])
        visited[i][j] = False

print(ans)