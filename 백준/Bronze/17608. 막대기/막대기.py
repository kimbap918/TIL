import sys

input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
    stack.append(int(input()))

last = stack[-1]
count = 1

for i in reversed(range(N)):
    if stack[i] > last:
        count += 1
        last = stack[i]

print(count)
