import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
cnt = 0
stack = []

for h in arr:
    # 10 3 8 4 12 2
    while stack and stack[-1] <= h: # 스택의 마지막이 높이보다 작거나 같을때까지

        stack.pop()
    cnt += len(stack)
    stack.append(h)

print(cnt)



# cnt = 0
# index = 0
# for i in arr:
#     if index == len(arr):
#         break
#     idx = index+1
#     while True:
#         if i < arr[idx]:
#             break
#         else:
#             cnt += 1
#             idx += 1
#     index += 1

# print(cnt)