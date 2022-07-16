# 1 = 시작점
# 2~7(6), 8~19(12), 20~37(18), 38~61(24)

# 등차수열 
# N번째 항의 값 = 시작숫자 + (시작숫자-1) * 공차
start = 1 # 시작지점(시작숫자)
res = 0 # 도착까지 횟수 
goal = int(input()) # N번째 항의 값, 목표지점

for i in range(0, goal): 
    start += res * 6
    if start < goal:
        res += 1
    else:
        res += 1
        break
print(res)

# while True:
#     if goal >= (start + (n-1) * 6):
#         n += 1
#     if goal <= (start + (n-1) * 6):
#         print(n)
#         break
#     if start >= goal: break

# N=int(input())
# res=0
# fin=1
# while True:
#     fin+=6*res
#     res+=1
#     if fin>=N: break
# print(res)
 

# 등차수열의 공식 
# an = a1 + (n-1) * d
# N번째 항의 값 = 시작숫자 + (시작숫자-1) * 공차
# valueN = inputA1 + (inputN-1) * inputD
# inputA1 = int(input('a1 입력:'))
# inputD = int(input('공차 입력:'))
# inputN = int(input('n 입력:'))

# valueN = 0
# n = 1

# while n <= inputN:
#     if n == 1:
#         valueN = inputA1
#         print(valueN)
#         n += 1
#         continue

#     valueN += inputD
#     print(valueN)
#     n += 1
# print('{}번째 항의 값: {}'.format(inputN, valueN))