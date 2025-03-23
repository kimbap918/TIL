# L인 문자열이 현재 편집기에 입력되어 있으면, 커서가 위치할 수 있는 곳은 L+1가지 경우

# L	커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
# D	커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
# B	커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
# 삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 
# 실제로 커서의 오른쪽에 있던 문자는 그대로임

# P $	$라는 문자를 커서 왼쪽에 추가함
from collections import deque
import sys
input = sys.stdin.readline

strings = input().rstrip()
cursor = len(strings)  # 커서는 문자열 끝에 위치
M = int(input())

left_stack = deque(strings)
right_stack = deque()

for _ in range(M):
    commands = input().split()
    cmd = commands[0]

    if cmd == "L":  # 커서를 왼쪽으로 이동
        if left_stack:
            right_stack.appendleft(left_stack.pop())
    elif cmd == "D":  # 커서를 오른쪽으로 이동
        if right_stack:
            left_stack.append(right_stack.popleft())
    elif cmd == "B":  # 커서 왼쪽 문자 삭제
        if left_stack:
            left_stack.pop()
    elif cmd == "P":  # 커서 왼쪽에 문자 추가
        word = commands[1]
        left_stack.append(word)


print(''.join(left_stack)+''.join(right_stack))