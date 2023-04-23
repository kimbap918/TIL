import sys
input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()
stack = []
length = len(str2)

for i in range(len(str1)):
    stack.append(str1[i])
    # print(stack)
    # str2의 길이만큼 
    if ''.join(stack[-length:]) == str2:
        # print(stack[-2:])
        for _ in range(length):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print("FRULA")
