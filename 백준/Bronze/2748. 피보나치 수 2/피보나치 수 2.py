def fib(N):
    memo = [0, 1]
    if N < 2:
        return N
    else:
        for i in range(2, N+1):
            memo.append(memo[i-1] + memo[i-2])
        return memo[N]

N = int(input())
print(fib(N))