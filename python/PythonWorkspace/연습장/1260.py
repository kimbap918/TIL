import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for i in range(N+1)]
visited_dfs = [0] * (N+1)
visited_bfs = [0] * (N+1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for num in graph:
    num.sort()

def dfs(visited, graph, V):
    visited[V] = 1
    print(V, end=" ")
    for i in graph[V]:
        if visited[i] == 0:
            dfs(visited, graph, i)

def bfs(visited, graph, V):
    visited[V] = 1
    Q = deque([V])
    while Q:
        V = Q.popleft()
        print(V, end=" ")
        for i in graph[V]:
            if visited[i] == 0:
                visited[i] = 1
                Q.append(i)
        


dfs(visited_dfs, graph, V)
print()
bfs(visited_bfs, graph, V)
