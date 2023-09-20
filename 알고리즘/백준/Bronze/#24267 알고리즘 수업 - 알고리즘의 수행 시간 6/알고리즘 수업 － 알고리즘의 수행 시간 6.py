# 작동 확인
# def MenOfPassion(A, n):
#     sum = 0
#     for i in range(1, n-1):
#         A.append(1)
#         for j in range(i+1, n):
#             A.append(1)
#             for k in range(j+1, n+1):
#                 A.append(1)

#     for i in range(1, n-1):
#         # print("i : "+str(i))
#         for j in range(i+1, n):
#             # print("j : "+str(j))
#             for k in range(j+1, n+1):
#                 print("k : "+str(k))

#                 sum += A[i] * A[j] * A[k]
#     return sum

# A = []
n = int(input())
# print(MenOfPassion(A, n))

# 수식 구현
print(int((n-2)*(n-1)*n/6))
print(3)