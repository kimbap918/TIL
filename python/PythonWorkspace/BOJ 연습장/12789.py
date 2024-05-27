# from collections import deque

# N = int(input())
# arr = deque(map(int, input().split()))
# stack = []
# check = 0

# while True:
#     if len(arr) == 0 and len(stack) == 0:
#         print("Nice")
#         break

#     if len(arr) != 0: # 데크가 비어있지 않을때
#         if arr[0] == min(arr): # 맨 첫번째 사람이 제일 우선순번인 경우
#             check = arr.popleft() # 빠져나감
#             print(arr)
#             print(stack) 
#         elif arr[0] != min(arr): # 데크의 첫번째가 우선순위가 아닌 경우
#             if len(stack) != 0 and check+1 == stack[-1]:
#                 check = stack.pop()
#                 print(check)
            
#             stack.append(arr.popleft())
#             print(stack)
#             #     print(stack)
#     # {10, 9, 8, 7, 6}
#     # [5, 4, 3, 2]
#     else: # 데크가 비어있을때
#         if min(stack) == stack[-1]:
#             check = stack.pop()
#             print(stack)
#         else:
#             print("Sad")
#             break


# 5 4 3 2 1 10 9 8 7 6
# [5, 4, 3, 2]
# [10, 9, 8, 7]



        # if len(arr) != 0:
        #     if arr[0] < stack[-1]:
        #         arr.popleft()
        #         # print(arr) # 1 3 2
        #     elif arr[0] > stack[-1]:
        #         stack.pop()
        #         # print(stack)
        # else:
        #     if min(stack) == stack[-1]:
        #         stack.pop()
        #         print(stack)
        #     else:
        #         flag = -1


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
