
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [-1] * (N+1)

def DFS(r):
    for i in graph[r]:
        if visited[i] == -1:
            visited[i] = visited[r]+1
            DFS(i)

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for num in graph:
    num.sort(reverse=True)

visited[R] = 0
DFS(R)

for i in visited[1:]:
    print(i)