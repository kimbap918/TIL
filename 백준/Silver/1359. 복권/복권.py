import math

N, M, K = map(int, input().split())

# 1부터 N까지 수 중
# 서로 다른 M 개의 수를 골라
# K개의 수가 같다면 당첨

# 3
# 1
# 1

# 1 2 3 N
# 1, 2, 3 M
# K



case = math.comb(N, M) # M개를 고르는 방법의 수
cnt = 0

# i개가 일치하는 경우
for i in range(K, M+1):
    # 고른 M개 중 i개가 일치하고, 나머지 (M-i)개는 일치하지 않는 경우
    cnt += math.comb(M, i) * math.comb(N-M, M-i)

res = cnt / case


print(res)

