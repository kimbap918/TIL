# import sys
# input = sys.stdin.readline

# def Sieve(N):
#     is_prime = [1 for _ in range(N + 1)]
#     prime = []
#     for i in range(2, N + 1):
#         if not is_prime[i]:
#             continue
#         prime.append(i)
#         for j in range(2 * i, N + 1, i):
#             is_prime[j] = 0
#     print(prime)
#     return prime

# N = int(input())
# A = [0] + list(map(int, input().split()))
# ans = 0

# # 7
# primes = Sieve(N)
# for prime in primes:
#     ans += A[prime]
        
# print(ans)
# UTF-8 encoding when using korean
import sys
import math
input = sys.stdin.readline
	
def is_prime(x):
	if x < 2:
		return False
	for i in range(2, int(math.sqrt(x))+1):
		if x % i == 0:
			return False
	return True

N = int(input())
A = [0] + list(map(int, input().split()))
ans = 0
for num in range(1, N+1):
	if is_prime(num):
		ans += A[num]

print(ans)