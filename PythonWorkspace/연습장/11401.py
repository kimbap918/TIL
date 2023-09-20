# # 이항 계수(Binomial Coefficient)
# # 조합론에서 등장하는 개념으로 주어진 크기 집합에서 원하는 개수만큼 순서 없이 뽑는 조합의 가짓수
# # nCk = n! / (k! * (n-k)!)

# import sys
# sys.setrecursionlimit(10**9)

# mod = 1000000007
# input = sys.stdin.readline
# N, K = map(int, input().split())

# # 부분문제의 중복이라는 현상을 설명하기 위해 비슷한 예제인 피보나치 수열에 대한 반복구현의 실행흐름을 가져왔다.
# # , 원 문제를 풀기 위한 부분문제가 너무 중복되어서 쓸데없는 시간을 잡아먹고 있는 것이다. 
# # 저런 식으로 만약 100번째 피보나치 수를 구하자고 하면 컴퓨터가 멈추고 만다.
# # res = factorial(N) // (factorial(K) * factorial(N - K))
# def bin(N, K):
#     # 이항계수를 담을 캐시를 생성한다.
#     cache = [[0 for j in range(K+1)] for i in range(N+1)]

#     def calc(N, K):
#         if cache[N][K] > 0:
#             return cache[N][K]

#         if K == 0 or N == K:
#             return 1
#         else:
#             res = calc(N-1, K-1) + calc(N-1, K)
#             cache[N][K] = res 
#         return res 

#     return calc(N, K) % mod

# print(bin(N, K))


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

# # 팩토리얼과 역원을 미리 계산하여 저장합니다.
# fact = [1, 1]
# for i in range(2, 4000001):
#     fact.append((fact[-1] * i) % MOD)

# inv = [0, 1]
# for i in range(2, 4000001):
#     inv.append((inv[MOD % i] * (MOD - int(MOD / i))) % MOD)

# for i in range(2, 4000001):
#     inv[i] = (inv[i] * inv[i - 1]) % MOD

# # 분할정복과 모듈러 연산을 이용하여 이항계수를 계산합니다.
# def binomial_coefficient(n, k):
#     return (fact[n] * inv[k] * inv[n - k]) % MOD

# n, k = map(int, input().split())
# print(binomial_coefficient(n, k))