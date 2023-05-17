# N = int(input())
# dp = [[0 for _ in range(5)] for _ in range(N + 1)]
# dp[0][0] = 1
# MOD = 100000007
    
# for i in range(1, N + 1):
#     dp[i][0] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3] + dp[i - 1][4]) % MOD
#     dp[i][1] = (dp[i - 1][0] + dp[i - 1][2] + dp[i - 1][3]) % MOD
#     dp[i][2] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][3] + dp[i - 1][4]) % MOD
#     dp[i][3] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % MOD
#     dp[i][4] = (dp[i - 1][0] + dp[i - 1][2]) % MOD

# print(sum(dp[N]) % MOD)

N = int(input())
dp = [[0] * 5 for _ in range(N+1)]
dp[0][0] = 1  # 초기값 설정
mod = 100_000_007

for i in range(1, N+1):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2] + dp[i-1][3] + dp[i-1][4]) % mod
    dp[i][1] = (dp[i-1][0] + dp[i-1][2] + dp[i-1][3]) % mod
    dp[i][2] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][3] + dp[i-1][4]) % mod
    dp[i][3] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % mod
    dp[i][4] = (dp[i-1][0] + dp[i-1][2]) % mod
print(sum(dp[N]) % mod)
