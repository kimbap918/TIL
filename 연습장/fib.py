# 일반적인 피보나치 수 (피보나치 수 5 boj 10870)
# def fib(N):
#     res = 0 
#     if N < 2:
#         return N
#     else:
#         res = fib(N-1) + fib(N-2)
#         return res

# 2747 피보나치 수 
# memo = [0 for _ in range(45+1)]
# memo[1] = 1

# def fib(N):    
#     if N <= 1:
#         return N
#     elif memo[N] != 0:
#         return memo[N]
#     else:
#         memo[N] = fib(N-1) + fib(N-2)
#         return memo[N] 


# 2748 피보나치 수 2
# def fib(N):
#     memo = [0, 1]
#     if N < 2:
#         return N
#     else:
#         for i in range(2, N+1):
#             memo.append(memo[i-1] + memo[i-2])
#         return memo[N]

# 2749 피보나치 수 3 피사노 주기(Pisano Period)
# 피보나치 수를 K로 나눈 나머지는 항상 주기를 갖게된다는 원리
# mod = 1000000
# p = mod//10*15
# memo = [0, 1]
# def fib(N):
#     if N < 2:
#         return N
#     else:
#         for i in range(2, p):
#             memo.append(memo[i-1] + memo[i-2])
#             memo[i] %= mod
#         return memo[N]
# N = int(input())
# print(fib(N%p))

# 피보나치 수 6(행렬 곱셈, 분할 정복 이용)
# import sys
# input = sys.stdin.readline

# N = int(input())
# matrix = [[1, 1], [1, 0]]

# # 행렬 곱셈
# def multiple_matrix(matrix_A, matrix_B):
#     res = [[0]*2 for _ in range(2)]
#     for i in range(2):
#         for j in range(2):
#             for k in range(2):
#                 res[i][j] += matrix_A[i][k] * matrix_B[k][j] % 1000000007
#     return res

# # 분할 정복
# def divide_matrix(A, B):
#     # B의 값이 1이 될때까지 재귀
#     if B == 1:
#         return A
#     else:
#         # a^(B//2)
#         temp = divide_matrix(A, B//2)
#         if B % 2 == 0:
#             return multiple_matrix(temp, temp)
#         else:
#             return multiple_matrix(multiple_matrix(temp, temp), A)

# res = divide_matrix(matrix, N)

# print(res[0][1] % 1000000007)