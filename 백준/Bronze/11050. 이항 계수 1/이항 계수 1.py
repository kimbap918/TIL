def factorial(K):
    if K < 2:
        return 1
    else:
        return K * factorial(K-1)
    
# 입력
N, K = map(int, input().split())

# N * N-1 * ...
num1 = 1
for i in range(K):
    num1 *= N-i

# K!
num2 = factorial(K)

# N * N-1 * ... // K!
print(num1 // num2)