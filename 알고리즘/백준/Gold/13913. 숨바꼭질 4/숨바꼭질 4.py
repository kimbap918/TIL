import sys
from collections import deque
input = sys.stdin.readline

MAX = 100001
N, K = map(int, input().split())
visited = [0] * MAX
move = [0] * MAX
ans = []

def path(x):
    temp = x
    for _ in range(visited[x]+1):
        ans.append(temp)
        temp = move[temp]


def BFS(v):
    Q = deque([v])
    while Q:
        x = Q.popleft()
        if x == K:
            path(x)
            return visited[x]
        for nx in (x+1, x-1, x*2):
            if 0 <= nx < MAX and not visited[nx]:
                Q.append(nx)
                visited[nx] = visited[x]+1
                move[nx] = x

print(BFS(N))
print(*ans[::-1])