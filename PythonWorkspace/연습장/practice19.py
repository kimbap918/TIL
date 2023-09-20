import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
island = [[] for _ in range(N+1)]
distance = [1e9 for _ in range(N+1)]

for i in range(M):
    u, v = map(int, input().split())
    island[u].append(v)
    island[v].append(u)

def BFS():
    distance[1] = 0
    Q = deque([1])
    
    while Q:
        a = Q.popleft()
        for i in island[a]:
            if distance[i] <= distance[a]+1:
                continue
            distance[i] = distance[a]+1
            Q.append(i)

BFS()
if distance[N] <= K:
    print("YES")
else:
    print("NO")
