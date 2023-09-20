import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = [int(input()) for i in range(n)]
dp = [0 for i in range(k+1)]
# dp[0]동전 하나를 사용하는 경우
# 즉 n이 1인 경우, 만약 n, k = 1, 2 라면 dp[2-2] = 1
dp[0] = 1

# dp[i] = i원을 만들 때 가능한 경우의 수
for i in coin:
    for j in range(i, k+1):
        if j-i >= 0:
            dp[j] += dp[j-i]
print(dp[k])
