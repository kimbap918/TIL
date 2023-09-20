import sys
input = sys.stdin.readline

N = int(input())
T, P = [0 for _ in range(N)], [0 for _ in range(N)]
for i in range(N):
    a, b = map(int, input().split())
    T[i], P[i] = a, b

dp = [0 for _ in range(N+1)]
# # 역순으로 진행
# for i in range(len(T)-1, -1, -1):
#     # i일에 상담을 하는것이 퇴사일을 넘기면 상담을 하지 않음
#     if i + T[i] > N:
#         dp[i] = dp[i+1]
#     else:
#         # i일에 상담을 하는 것과 하지 않는것 중 큰것을 선택
#         dp[i] = max(dp[i+1], P[i] + dp[i + T[i]])


# print(dp[0])

for i in range(N):
    # 오늘일자 + 상담소요시간, N+1까지
    for j in range(i + T[i], N+1):
        # dp[j]보다 dp[i] + 이익이 큰 경우 dp[j]에 저장
        if dp[j] < dp[i] + P[i]:
            dp[j] = dp[i] + P[i]

print(dp[-1])