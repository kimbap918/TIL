from collections import deque

N = int(input())
P = list(map(int, input().split())) + [0]

if N < 3:
    print(0)
else:
    dp = deque()
    dp.append(P[0])
    dp.append(P[1])
    dp.append(P[2])

    for i in range(3, N+1):
        dp.append(min(dp[0], dp[1], dp[2]) + P[i])
        # print(dp)
        dp.popleft()

    print(dp[-1])