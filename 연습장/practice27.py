# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from collections import deque
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
island = [[] for _ in range(N+1)]
distance = [1e9 for _ in range(N+1)]
distance[K] = 0
ans = 9**9

def BFS():
    global ans
    Q = deque()
    Q.append(K)
    
    while Q:
        cur = Q.popleft()
        for i in island[cur]:
            if i == K:
                ans = min(ans, distance[cur]+1)
            if distance[i] <= distance[cur]+1:
                continue
            distance[i] = distance[cur]+1
            Q.append(i)

for _ in range(M):
    a, b = map(int, input().split())
    island[a].append(b)
    
BFS()

if ans == 9**9:
    print(-1)
else:
    print(ans)
