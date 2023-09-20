# 이항 계수(Binomial Coefficient)
# 조합론에서 등장하는 개념으로 주어진 크기 집합에서 원하는 개수만큼 순서 없이 뽑는 조합의 가짓수

# 1. N * ... * 1을 총 K번 진행
# 2. K! 계산
# 3. 1번의 결과를 2번의 결과로 나눔

# Factorial 계산하는 함수
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

print((num1 // num2)%10007)