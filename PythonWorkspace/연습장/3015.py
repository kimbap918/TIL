import sys
input = sys.stdin.readline

stack = []
ans = 0

# N명이 한 줄로 서있다.
for _ in range(int(input())):
    hight = int(input())

    # 스택이 비어있고, 끝자리가 높이보다 작으면 좋료
    while stack and stack[-1][0] < hight:
        # print(stack)
        # 카운트값을 꺼내 ans에 누적한다
        ans += stack.pop()[-1]
        # print(stack)

    # 스택의 끝자리가 높이와 같을때
    if stack and stack[-1][0] == hight:
        # 카운트를 누적한다.
        cnt = stack.pop()[1]
        ans += cnt

        # 스택의 길이가 0이 아니라면? 스택에 수가 들어왔을때 
        if len(stack) != 0:
            ans += 1
        # 스택의 끝자리와 높이가 같으면 (높이, 카운트+1) 값을 추가
        stack.append((hight, cnt+1))
        # print(stack)
    # 스택이 비어있는 경우
    else:
        if len(stack) != 0:
            ans += 1
        stack.append((hight, 1))   

print(ans)