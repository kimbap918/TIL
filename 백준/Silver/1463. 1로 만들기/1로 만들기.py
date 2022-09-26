n = int(input()) # 10
dp = [0] * (n+1) # [0] * 11

for i in range(2, n+1): # 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
    dp[i] = dp[i-1]+1 # dp[2] = dp[1] 0+1 = 1, dp[3] = dp[2] 0+1 = 1...

    if i % 2 == 0: # 2
        dp[i] = min(dp[i], dp[i//2]+1) # dp[2] = dp[2](1), dp[1](0)+1=(1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)

print(dp[n])