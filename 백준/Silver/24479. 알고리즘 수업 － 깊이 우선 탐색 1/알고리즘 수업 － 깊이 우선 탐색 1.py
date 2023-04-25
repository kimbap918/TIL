import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

# 5 5 1
N, M, R = map(int, input().split())
# 간선 정보가 담긴 리스트
E = [[] for _ in range(N+1)]
# 방문 기록
visited = [0] * (N+1)
cnt = 1

for _ in range(M):
    u, v = map(int, input().split())
    E[u].append(v)
    E[v].append(u)    

for num in E:
    num.sort()

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