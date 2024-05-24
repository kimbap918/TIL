
from collections import deque

N = int(input())
arr = deque(map(int, input().split()))
stack = []
expected = 1

while arr or stack:
    if arr and arr[0] == expected:
        arr.popleft()
        expected += 1
    elif stack and stack[-1] == expected:
        stack.pop()
        expected += 1
    elif arr:
        stack.append(arr.popleft())
    else:
        print("Sad")
        break
else:
    print("Nice")
