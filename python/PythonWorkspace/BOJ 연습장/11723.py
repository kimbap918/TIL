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


    
    
# import sys
# input = sys.stdin.readline

# M = int(input())
# S = 0  # 공집합

# for _ in range(M):
#     cmd = input().strip().split()

#     if cmd[0] == "add":
#         S |= (1 << int(cmd[1]) - 1)
#     elif cmd[0] == "remove":
#         S &= ~(1 << int(cmd[1]) - 1)
#     elif cmd[0] == "check":
#         print(1 if S & (1 << int(cmd[1]) - 1) else 0)
#     elif cmd[0] == "toggle":
#         S ^= (1 << int(cmd[1]) - 1)
#     elif cmd[0] == "all":
#         S = (1 << 20) - 1  # 모든 비트 1 (1~20)
#     elif cmd[0] == "empty":
#         S = 0
