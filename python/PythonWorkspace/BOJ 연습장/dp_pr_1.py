N = int(input())
K = list(map(int, input().split()))

dp = [0] * 100
dp[0] = K[0]
dp[1] = max(K[0], K[1])

for i in range(2, N):
    dp[i] = max(dp[i-1], dp[i-2]+K[i])

print(dp[N-1])