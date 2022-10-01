n = int(input())
a = []
b = []
dp = [0 for i in range(n)]
for i in range(n):
    a.append(list(map(int, input().split())))
a.sort(key = lambda x:x[0])
# [[1, 8], [2, 2], [3, 9], [4, 1], [6, 4], [7, 6], [9, 7], [10, 10]]
for i in range(n):
    b.append(a[i][1])
    # 8, 2, 9, 1, 4, 6, 7, 10
for i in range(n): # 8
    for j in range(i): 
        if b[i] > b[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(n - max(dp))