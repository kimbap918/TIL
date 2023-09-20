import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
queue = deque()
for i in range(N):
    command = list(map(str, input().split()))
    word = command[0]
    if word == "push":
        queue.append(int(command[1]))
    if word == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    if word == "size":
        print(len(queue))
    if word == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    if word == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    if word == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])


    
            
