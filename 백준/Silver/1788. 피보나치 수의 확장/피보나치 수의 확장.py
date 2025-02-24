import sys


def fib(N):
    mod = 1000000000
    if N == 0:
        return (0, 0)

    if N < 0:
        N = abs(N)
        if N % 2 == 0:
            sign = -1
        else:
            sign = 1
    else:
        sign = 1

    if N == 1:
        return (sign, 1)
    
    a, b = 0, 1
    for i in range(2, N+1):
        a, b = b, (a+b) % mod

    return (sign, b)


N = int(input())
sign, value = fib(N)

print(sign)
print(value)