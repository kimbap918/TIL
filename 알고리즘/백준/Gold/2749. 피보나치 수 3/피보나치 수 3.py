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