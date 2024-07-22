import sys
from collections import deque
n = int(input())

dequeue = deque()
for i in range(n):
    num = list(map(int, sys.stdin.readline().strip().split()))
    l = len(dequeue)
    if num[0] == 1:
        dequeue.appendleft(num[1])
    elif num[0] == 2:
        dequeue.append(num[1])
    elif num[0] == 3:
        print(dequeue.popleft() if l else -1)
    elif num[0] == 4:
        print(dequeue.pop() if l else -1)
    elif num[0] == 5:
        print(len(dequeue))
    elif num[0] == 6:
        print(0 if l else 1)
    elif num[0] == 7:
        print(dequeue[0] if l else -1)
    elif num[0] == 8:
        print(dequeue[-1] if l else -1)