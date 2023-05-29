import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
cnt = [0 for _ in range(N+1)]
cycle = []

for i in range(N):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    cnt[u] += 1
    cnt[v] += 1

print(graph)
print(cnt)