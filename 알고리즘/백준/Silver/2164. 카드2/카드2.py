from collections import deque
import sys

queue = deque()
N = int(input())

for i in range(1, N+1):
    queue.append(i)

while len(queue) > 1:
    queue.popleft()
    # print(queue)
    queue.rotate(-1)
    # print(queue)
print(queue[0])