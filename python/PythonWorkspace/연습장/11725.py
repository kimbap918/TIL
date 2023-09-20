import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
graph = [[] for _ in range(N+1)]
visited_1 = [0] * (N+1)
visited_2 = [0] * (N+1)


def DFS(r):
    for i in graph[r]:
        if visited_1[i] == 0:
            visited_1[i] = r
            DFS(i)

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


DFS(1)
BFS(1)

for i in visited_1[2:]:
    print(i)

for i in visited_2[2:]:
    print(i)