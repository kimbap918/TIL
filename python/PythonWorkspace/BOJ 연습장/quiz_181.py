n = int(input()) # 6
a = list(map(int, input().split())) # 10 20 10 30 20 50
dp = [0 for _ in range(n)] # [0, 0, 0, 0, 0, 0]
for i in range(n): # 6
    for j in range(i):
        print(i)
        # i = 122333444455555
        # j = 001012012301234
        # 비교하는 a[i] 값이 순회하는 이전값들 보다 크고, 
        # 저장한 길이값이 비교값보다 작을 경우 
        if a[i] > a[j] and dp[i] < dp[j]: 
            dp[i] = dp[j] # 최댓값 저장
    dp[i] += 1 # 1씩 누적
print(max(dp))