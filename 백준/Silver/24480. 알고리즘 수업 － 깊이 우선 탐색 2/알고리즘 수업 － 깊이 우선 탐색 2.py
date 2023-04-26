import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
N, M, R = map(int, input().split())
E = [[] for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 1

for _ in range(M):
    u, v = map(int, input().split())
    E[v].append(u)
    E[u].append(v)

for num in E:
    num.sort(reverse=True)

def dfs(E, R, visited):
    global cnt
    visited[R] = cnt
    for i in E[R]:
        if visited[i] == False:
            cnt += 1
            dfs(E, i, visited)
    return visited

dfs(E, R, visited)
for i in visited[1:]:
    print(i)