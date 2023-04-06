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
mod = 1000000
p = mod//10*15
memo = [0, 1]
def fib(N):
    if N < 2:
        return N
    else:
        for i in range(2, p):
            memo.append(memo[i-1] + memo[i-2])
            memo[i] %= mod
        return memo[N]
N = int(input())
print(fib(N%p))