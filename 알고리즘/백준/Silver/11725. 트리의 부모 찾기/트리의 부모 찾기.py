import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
visited_2 = [0] * (N+1)

def BFS(r):
    Q = deque([r])

    while Q:
        cur = Q.popleft()
        for i in graph[cur]:
            if visited_2[i] == 0:
                visited_2[i] = cur
                Q.append(i)


for i in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


BFS(1)

for i in visited_2[2:]:
    print(i)