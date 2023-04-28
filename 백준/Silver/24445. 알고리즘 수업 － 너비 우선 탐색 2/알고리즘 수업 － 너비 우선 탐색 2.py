import sys
from collections import deque
input = sys.stdin.readline

N, M, R = map(int, input().split())
E = [[] for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 1

for _ in range(M):
    u, v = map(int, input().split())
    E[u].append(v)
    E[v].append(u)

def bfs(E, R, visited):
    global cnt
    Q = deque([R])
    visited[R] = 1
    while Q:
        u = Q.popleft()
        E[u].sort(reverse=True)
        for i in E[u]:
            if visited[i] == 0:
                cnt += 1
                visited[i] = cnt
                Q.append(i)


bfs(E, R, visited)

for i in visited[1:]:
    print(i)