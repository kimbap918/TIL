# 1. 첫 번째 원소를 뽑아낸다. 이 연산을 수행하면, 원래 큐의 원소가 a1, ..., ak이었던 것이 a2, ..., ak와 같이 된다.
# 2. 왼쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 a2, ..., ak, a1이 된다.
# 3. 오른쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 ak, a1, ..., ak-1이 된다.
from collections import deque
import sys
input = sys.stdin.readline
# queue의 크기 N, 뽑아내려고 하는 수의 개수 M
N, M = map(int, input().split())
pos = list(map(int, input().split()))
queue = deque([i for i in range(1, N+1)])

cnt = 0
for i in pos: # 위치 하나씩마다 반복하기
    while True: # 뽑을때까지 반복하기
        if queue[0] == i: # 큐의 첫 인덱스가 뽑아내려는 숫자와 같다면
            queue.popleft()
            break
        else:
            if queue.index(i) < len(queue) / 2: # 인덱스 값이 큐를 반으로 나눈것보다 작으면?
                while queue[0] != i: # 2번 실행
                    queue.append(queue.popleft())
                    cnt += 1
            else: # 큐를 반으로 나눈 값 보다 크면 
                while queue[0] != i: # 3번 실행
                    queue.appendleft(queue.pop())
                    cnt += 1
print(cnt)
                


