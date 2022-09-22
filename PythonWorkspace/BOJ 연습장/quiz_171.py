dp = [0 for i in range(101)] # 1 <= N <= 100
dp[1] = 1 # 1번째부터 3번째 변의 길이는 무조건 1
dp[2] = 1
dp[3] = 1

for i in range(0, 98):
    dp[i+3] = dp[i] + dp[i+1] # 3번째 이후의 수는 dp[i]와 dp[i+1]의 합이 나열됨

T = int(input())
for i in range(T):
    n = int(input())
    print(dp[n])    