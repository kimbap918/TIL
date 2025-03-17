import sys
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
start = int(input())

graph = [[] for i in range(N+1)]
visited = [False] * (N+1)
dist = [INF] * (N+1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))


def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, N+1):
        if dist[i] < min_value and not visited[i]:
            min_value = dist[i]
            index = i
    return index

def dijkstra(start):
    dist[start] = 0
    visited[start] = True
    for j in graph[start]:
        dist[j[0]] = j[1]

    for i in range(N-1):
        now = get_smallest_node()
        visited[now] = True
        
        for j in graph[now]:
            cost = dist[now] + j[1]
            if cost < dist[j[0]]:
                dist[j[0]] = cost

dijkstra(start)

for i in range(1, N+1):
    if dist[i] == INF:
        print("INFINITY")
    else:
        print(dist[i])


