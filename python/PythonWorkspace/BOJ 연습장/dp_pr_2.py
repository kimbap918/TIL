N = int(input())

dp = [0] * 1001
dp[0] = 1
dp[1] = 3

for i in range(3, N+1):
    dp[i] = (dp[i-1] + dp[i-2] * 2) % 796796


print(dp[N])