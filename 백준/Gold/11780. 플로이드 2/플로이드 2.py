N = int(input())
M = int(input())
INF = int(1e9)
graph = [[INF] * (N+1) for _ in range(N+1)]
path = [[0] * (N+1) for _ in range(N+1)]

for a in range(1, N+1):
    for b in range(1, N+1):
        if a == b:
            graph[a][b] = 0
        else: # 직접 연결된 경우 목적지를 경로로 저장
            path[a][b] = b

for _ in range(M):
    a, b, c = map(int, input().split())
    if c < graph[a][b]: # 더 짧은 경로를 발견한 경우에만 업데이트
        graph[a][b] = c
        path[a][b] = b # 목적지를 경로로 저장

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            if graph[a][k] + graph[k][b] < graph[a][b]:
                graph[a][b] = graph[a][k] + graph[k][b]
                path[a][b] = path[a][k]


for a in range(1, N+1):
    for b in range(1, N+1):
        if graph[a][b] == INF:
            print(0, end=" ")
        else:
            print(graph[a][b], end=" ")
    print()

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j or graph[i][j] == INF:
            print(0)
            continue
        route = [i]
        current = i
        while current != j:
            current = path[current][j]
            route.append(current)

        
        print(len(route), end=" ")
        print(*route)


# 먼저, N개의 줄을 출력해야 한다. 
# i번째 줄에 출력하는 j번째 숫자는 도시 i에서 j로 가는데 필요한 최소 비용이다. 
# 만약, i에서 j로 갈 수 없는 경우에는 그 자리에 0을 출력한다.
# 그 다음에는 N×N개의 줄을 출력해야 한다. 
# i×n+j번째 줄에는 도시 i에서 도시 j로 가는 최소 비용에 포함되어 있는
# 도시의 개수 k를 출력한다. 
# 그 다음, 도시 i에서 도시 j로 가는 경로를 공백으로 구분해 출력한다. 
# 이때, 도시 i와 도시 j도 출력해야 한다. 
# 만약, i에서 j로 갈 수 없는 경우에는 0을 출력한다.

