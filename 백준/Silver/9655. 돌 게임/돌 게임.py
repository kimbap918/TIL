N = int(input())
dp = [False] * (N+4)

dp[1] = True # SK
dp[2] = False # CY
dp[3] = True

for i in range(4, N+1):
    if not dp[i-1] or not dp[i-3]:
        dp[i] = True
    else:
        dp[i] = False

print("SK" if dp[N] else "CY")