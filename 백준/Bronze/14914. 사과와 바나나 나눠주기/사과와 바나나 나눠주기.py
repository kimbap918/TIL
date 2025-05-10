from math import gcd

n, m = map(int, input().split())
for i in range(1, gcd(n, m) + 1):
    if n % i == 0 and m % i == 0:
        print(f"{i} {n // i} {m // i}")