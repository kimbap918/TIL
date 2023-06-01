import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [-1] * (N+1)
t = [0] * (N+1)
cnt = 1
ans = 0

def DFS(r, depth):
    global cnt
    t[r] = cnt
    visited[r] = depth

    for i in graph[r]:
        if visited[i] == -1:
            cnt += 1
            DFS(i, depth+1)

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for num in graph:
    num.sort(reverse=True)

DFS(R, 0)

for i in range(1, N+1):
    ans += visited[i] * t[i]

# print(ans)
# print(graph)
# print(visited)
# print(t)