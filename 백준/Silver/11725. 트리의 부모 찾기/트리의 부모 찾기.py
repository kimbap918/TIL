import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

def DFS(r):
    for i in graph[r]:
        if visited[i] == 0:
            visited[i] = r
            DFS(i)

for i in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


DFS(1)

for i in visited[2:]:
    print(i)
