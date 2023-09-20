import sys
input = sys.stdin.readline

K = int(input())
range_fib = 10_000
p = range_fib//10*15 # 150_000
memo = [0, 1]

def fib(n):
    if n < 2:
        return n
    else:
        for i in range(2, p):
            memo.append(memo[i-1] + memo[i-2])
            # memo[i] %= 1_000_000_007
        return memo[n]

print(fib((K)))