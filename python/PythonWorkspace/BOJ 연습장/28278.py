import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    order = input()
    command = order[0]
    if command == "1":
        stack.append(int(order[2:]))
    elif command == "2":
        if len(stack) > 0:
            print(stack.pop())            
        else:
            print(-1)
    elif command == "3":
        print(len(stack))
    elif command == "4":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command == "5":
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)
