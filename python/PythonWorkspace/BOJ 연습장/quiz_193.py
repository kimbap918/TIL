import sys
input = sys.stdin.readline
N = int(input())
stack = []
oper = []
cnt = 1
temp = True

for _ in range(N):
    command = int(input())
    if cnt <= command: # cnt 보다 명령어가 크면 추가
        for i in range(cnt, command+1): # 중복숫자는 안나오므로 cnt이후의 수
            stack.append(cnt)
            oper.append('+')
            # print("cnt:"+str(cnt))
            # print("stack:"+str(stack))
            cnt += 1 # cnt 증가

    if stack[-1] == command: # stack의 끝이 입력숫자와 같으면
        stack.pop() # 빼준다
        oper.append('-') # - 추가
        # print("stack:"+str(stack))
    else: # 그외(연산불가)
        temp = False 

if temp == False:
    print('NO')
else:
    for i in oper:
        print(i)
