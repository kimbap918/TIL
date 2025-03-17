N, M = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (N+1) for _ in range(N+1)]

# min(dist[a][b], dist[a][k] + dist[k][b])


for a in range(1, N+1):
    for b in range(1, N+1):
        if a == b:
            graph[a][b] = 0


for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

dist = graph[1][k] + graph[k][x] # 시작 지점에서 k번 들러서 x에 도달하는 최소시간

if dist >= INF:
    print(-1)
else:
    print(dist)

