from collections import deque
import sys
input = sys.stdin.readline

def BFS(arr, start):
    visited.add(start)
    Q = deque([start])  

    while Q:
        c = Q.popleft() 
        for i in arr[c]:
            if i not in visited:
                visited.add(i)  
                Q.append(i)  

N, M = map(int, input().split())
cows = [[] for _ in range(N+1)]
visited = set()

for _ in range(M):
    c1, c2 = map(int, input().split())
    cows[c1].append(c2)
    cows[c2].append(c1)

BFS(cows, 1)

cow_list = []
for i in range(2, N+1):
    if i not in visited:
        cow_list.append(i)

if cow_list:
    print(*cow_list, sep='\n')
else:
    print(0)
