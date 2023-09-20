# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
stack = deque()
for i in range(N):
    command = input().rstrip()

    if "push" in command:
        command, value = map(str, command.split())
        value = int(value)
        stack.append(value)
        if len(stack) > K:
            print("Overflow")
            
    elif command == "pop":
        if len(stack) <= 0:
            print("Underflow")
        else:
            print(stack.pop())
