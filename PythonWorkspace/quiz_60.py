import math

T = int(input())
A = list(map(int, input().split()))
B = []
max = 0
cnt = 0

for i in range(len(A)): # 가장 큰 수 구하기
    if max < A[i]:
        max = A[i]

# 소수 구하기/에라토스테네스의 체
for n in range(2, max+1): # 2부터 max+1까지 
    check = True          
    for i in range(2, int(n**0.5)+1): # 2부터 n의 제곱근까지만 검사
        if n%i == 0:                  # n%i가 소수가 아닌 경우 
            check = False
    if check: # 소수인경우 
        B.append(n)

for k in B: # 리스트 B와 A 비교
    for h in range(len(A)):
        if A[h] == k: # k의 값(소수)이 리스트 A에 있는 값과 같다면
            cnt += 1 # 카운트 증가
print(cnt)

# import sys
# n = int(sys.stdin.readline())
# ar = list(map(int,sys.stdin.readline().split()))
# c= 0
# for i in ar:
#     b = 0
#     if i ==1: b=1
#     for j in range(2,i):
#         if i%j == 0: b =1
#     if b == 0: c+=1
# print(c)