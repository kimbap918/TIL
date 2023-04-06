def fib(N):
    memo = []
    memo.append(0)
    memo.append(1)
    for i in range(2, 45+1):
        memo.append(memo[i-1] + memo[i-2])
    return memo[N]

N = int(input())
print(fib(N))