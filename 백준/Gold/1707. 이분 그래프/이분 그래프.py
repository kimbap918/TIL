import sys
from collections import deque
input = sys.stdin.readline

def BFS(start, num):
    Q = deque([start])
    visited[start] = num
    
    while Q:
        x = Q.popleft()

        for i in graph[x]:
            if not visited[i]:
                Q.append(i)
                visited[i] = -1 * visited[x]
            elif visited[i] == visited[x]:
                return False
    return True

for K in range(int(input())):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [False] * (V+1)

    # E줄에 걸쳐 정점의 개수, 간선의 개수를 입력받음
    for i in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    # 각 정점에는 1부터 V까지 차례로 번호가 붙어있다.
    for j in range(1, V+1):
        if not visited[j]:
            ans = BFS(j, 1)
            if not ans:
                break

    if ans:
        print("YES")
    else:
        print("NO")