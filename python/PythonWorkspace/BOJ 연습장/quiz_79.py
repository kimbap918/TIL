# 자리에 들어가는 5개의 숫자를 각각 
# 제곱한 수의 합을 10으로 나눈 나머지이다.

N = list(map(int, input().split()))
a = 0
for i in range(len(N)):
    a += (N[i] * N[i])
print(a%10)