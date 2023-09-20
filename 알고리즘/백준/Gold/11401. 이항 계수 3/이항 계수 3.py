

# nCk = N!/(N-K)!K! 이다.
# 나머지 연산(모듈러)의 분배법칙
# (A + B) % p = ((A % p) + (B % p)) % p
# (A x B) % p = ((A % p) x (B % p)) % p
# (A - B) % p = ((A % p) - (B % p) + p) % p
# 나눗셈에 대해서는 분배법칙이 성립하지 않는다.
# 이를 위해 곱셈에 대한 분배법칙을 활용하기 위해 페르마의 소정리를 이용한다.

# p가 소수, a가 정수일 때
# a^p ≡ a(mod p)
# 세줄 등호는 합동을 의미(p로 나눈 나머지가 서로 같다)
# 이 식의 양 변을 a^2로 나눠주면
# a^p−2 ≡ 1/a(mod p)(a는 0이 아님) 를 이용한다.
# nCk % p = N!/(N-K)!K!%p = N!((N-K)!K!)^-1%p = N!((N-K)!K!)^p-2%p

import sys
input = sys.stdin.readline
N, K = map(int, input().split())
mod = 1000000007

# 팩토리얼
def factorial(N):
    n = 1
    # 나머지 연산을 적용한 팩토리얼 값 계산
    for i in range(2, N+1):
        n = (n * i) % mod
    return n

# 거듭제곱
def square(N, K):
    if K == 0:
        return 1
    elif K == 1:
        return N
    
    temp = square(N, K//2)
    if K % 2:
        return temp * temp * N % mod
    else:
        return temp * temp % mod

numerator = factorial(N)
denominator = factorial(N-K) * factorial(K) % mod
# N!((N-K)!K!)^p-2%p
print(numerator * square(denominator, mod-2) % mod)
