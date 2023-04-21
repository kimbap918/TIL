import sys
input = sys.stdin.readline

stack = []
ans = 0

for _ in range(int(input())):
    hight = int(input())
    # 스택의 끝자리보다 큰 수가 들어왔을 시 
    while stack and stack[-1][0] < hight:
        ans += stack.pop()[-1]

    if stack and stack[-1][0] == hight:
        cnt = stack.pop()[1]
        ans += cnt

        # 스택의 길이가 0이 아니라면? 스택에 수가 들어왔을때 
        if len(stack) != 0:
            ans += 1
        stack.append((hight, cnt+1))
    else:
        if len(stack) != 0:
            ans += 1
        stack.append((hight, 1))   

print(ans)