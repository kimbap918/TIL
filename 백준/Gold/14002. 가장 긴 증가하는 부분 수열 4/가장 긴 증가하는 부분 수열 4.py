import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [0 for i in range(N+1)]

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j]+1)

ans1 = max(dp)
res = []
for i in range(N-1, -1, -1):
    if dp[i] == ans1:
        res.append(A[i])
        ans1 -= 1
res.reverse()
print(len(res))
for i in res:
    print(i, end=' ')

