def dfs(depth, idx):
    global min_diff
    if depth == n//2:
        team1, team2 = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    team1 += graph[i][j]
                elif not visited[i] and not visited[j]:
                    team2 += graph[i][j]
        min_diff = min(min_diff, abs(team1-team2))
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i+1)
            visited[i] = False


n = int(input())

visited = [0 for _ in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]
min_diff = int(1e9)

dfs(0, 0)
print(min_diff)