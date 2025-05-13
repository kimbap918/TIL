N, M = map(int, input().split())
arr = [] # 2, 3

for i in range(N):
    arr.append(int(input()))


dp = [10001] * (M+1)
dp[0] = 0

for i in range(N): # 2, 15
    # i = 0, 1
    for j in range(arr[i], M+1): # 2, 3 / 15
        if dp[j-arr[i]] != 10001:
            dp[j] = min(dp[j], dp[j-arr[i]+1])


if dp[M] == 100001:
    print(-1)
else:
    print(dp[M])