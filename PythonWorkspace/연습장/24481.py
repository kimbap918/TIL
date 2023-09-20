import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [-1] * (N+1) # 미방문 노드를 -1로 초기화

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
for num in graph:
    num.sort()

def DFS(r):
    for i in graph[r]:
        if visited[i] == -1:
            # 노드를 방문하면서 깊이를 저장
            visited[i] = visited[r]+1
            DFS(i)

visited[R] = 0
DFS(R)

# print(visited)
for i in visited[1:]:
    print(i)

# print(graph)
# print(visited)