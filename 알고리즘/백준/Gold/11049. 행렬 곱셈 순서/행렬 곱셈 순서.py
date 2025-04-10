import sys
input = sys.stdin.readline
# 4
# 5 3
# 3 2
# 2 6
# 6 3
N = int(input())
S = [list(map(int, input().split())) for i in range(N)]
# dp[i][j] -> i부터 j까지 최솟값
# (a) + (b, c, d) + 비용
# (a, b) + (c, d) + 비용
# (a, b, c) + (d) + 비용 이 중 최소값이 된다.
dp = [[0] * N for i in range(N)]
for i in range(1, N):
    for j in range(N - i):
        x = j + i
        dp[j][x] = 2 ** 32

        for k in range(j, x):
            # n = 4일때
            # dp[0][1] -> dp[1][2] -> dp[2][3] -> dp[0][2] -> dp[1][3] -> dp[0][3]
            dp[j][x] = min(dp[j][x], dp[j][k] + dp[k + 1][x] + S[j][0] * S[k][1] * S[x][1])

print(dp[0][N - 1])