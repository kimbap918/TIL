N = int(input())
M = int(input())
INF = int(1e9)
graph = [[INF] * (N+1) for _ in range(N+1)]


# graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, N+1):
    for b in range(1, N+1):
        if a == b:
            graph[a][b] = 0


for _ in range(M):
    # 시작도시, 도착도시, 비용
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c) # 시작도시와 도착도시를 연결하는 노선이 하나가 아닐수있음


for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])


for a in range(1, N+1):
    for b in range(1, N+1):
        if graph[a][b] == INF:
            print(0, end=" ")
        else:
            print(graph[a][b], end=" ")
    print()
        
