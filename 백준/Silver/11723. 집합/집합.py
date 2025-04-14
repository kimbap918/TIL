import sys
from collections import deque
input = sys.stdin.readline


M = int(input())
S = deque()

for i in range(M):
    commands = input().rstrip().split()
    command = commands[0]

    if len(commands) == 2:
        num = int(commands[1])

    if command == "add":
        if num in S:
            continue
        else: 
            S.append(num)
    elif command == "remove":
        if num in S:
            S.remove(num)
        else:
            continue
    elif command == "check":
        if num in S:
            print(1)
        else:
            print(0)
    elif command == "toggle":
        if num in S:
            S.remove(num)
        else:
            S.append(num)
    elif command == "all":
        S = [i for i in range(1, 21)]
    elif command == "empty":
        S = []


    
 