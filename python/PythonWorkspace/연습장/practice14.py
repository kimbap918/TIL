# import sys
# input = sys.stdin.readline

# # 주기의 길이를 p라고 하면, N번째 피보나치 수를 M으로 나눈 나머지는 N%P번째 피보나치 수를 M으로 나눈 나머지와 같다.
# K = int(input())
# p = 100_000
# memo = [0, 1]

# def fib(n):
#     if n < 2:
#         return n
#     else:
#         for i in range(2, p+1):
#             memo.append(memo[i-1] + memo[i-2])
#             memo[i] %= 1_000_000_007
#         return memo[n]

# print(fib((K)))

import sys
input = sys.stdin.readline

K = int(input())
matrix = [[1, 1], [1, 0]]
mod = 1_000_000_007

def multiple_matrix(mat_A, mat_B):
    res = [[0]*2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                res[i][j] += mat_A[i][k] * mat_B[k][j] % mod
    return res

def nth(A, B):
    if B == 1:
        return A
    else:
        temp = nth(A, B//2)
        if B % 2 == 0:
            return multiple_matrix(temp, temp)
        else:
            return multiple_matrix(multiple_matrix(temp, temp), A)

res = nth(matrix, K)

print(res[0][1] % mod)

# 2748 피보나치 수 2
# N = int(input())
# mod = 1_000_000_007

# def fib(N):
#     memo = [0, 1]
#     if N < 2:
#         return N
#     else:
#         for i in range(2, N+1):
#             memo.append(memo[i-1] + memo[i-2])
#         return memo[N]

# print(fib(N)%mod)