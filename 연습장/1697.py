import sys
from collections import deque
input = sys.stdin.readline

def BFS(v):
    Q = deque([v])
    while Q:
        x = Q.popleft()
        if x == K:
            return arr[x]
        # X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
        # 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.
        # 기존 위치에서 이동하는 위치는 3가지
        for nx in (x-1, x+1, x*2):
            # 
            if 0 <= nx <= MAX and not arr[nx]:
                arr[nx] = arr[x]+1
                Q.append(nx)

MAX = 10001
arr = [0] * MAX
N, K = map(int, input().split())
print(BFS(N))