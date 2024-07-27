a, b, c, n = list(map(int, input().split()))
dp = [0] * (300+1)
dp[a] = dp[b] = dp[c] = 1

for i in range(a, n+1):
   for j in [a, b, c]:
      if i >= j  and dp[i - j]:
         dp[i] = 1 

print(dp[n])