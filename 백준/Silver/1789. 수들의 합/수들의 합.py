# 200
# 19
# 서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?


S = int(input())
res = 0
N = 0

while res <= S:
    N += 1
    res += N

print(N-1)

