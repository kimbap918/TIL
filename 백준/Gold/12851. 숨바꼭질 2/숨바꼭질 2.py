import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
MAX = 100001
arr = [0] * MAX
cnt_ans = 0
cnt_way = 0

def BFS(v):
    global cnt_ans
    global cnt_way

    Q = deque([v])

    while Q:
        x = Q.popleft()
        count = arr[x]

        if x == K:
            cnt_way += 1
            cnt_ans = count 
            continue

        # X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
        # 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.
        # 기존 위치에서 이동하는 위치는 3가지
        for nx in (x-1, x+1, x*2):
            # x-1, x+1 x*2이 범위를 벗어나면 안된다.
            if 0 <= nx < MAX:
                if arr[nx] == 0 or arr[nx] == arr[x]+1:
                    arr[nx] = count + 1
                    Q.append(nx)

BFS(N)
print(cnt_ans)
print(cnt_way)