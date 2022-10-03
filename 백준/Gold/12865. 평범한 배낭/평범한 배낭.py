N, K = map(int, input().split())

WV = [[0,0]]
dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(N):
    WV.append(list(map(int, input().split())))

for i in range(1, N+1):
    for j in range(1, K+1):
        w = WV[i][0] # 무게는 WV의 0번째 요소
        v = WV[i][1] # 가치는 WV의 1번째 요소

        if j < w: # 가방의 허용 용량이 무게보다 작다면
            dp[i][j] = dp[i-1][j] # 물건을 넣지 않는다
        else: # 가방의 허용 용량이 무게보다 크다면
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v) # 이전 베낭을 그대로 가져가거나, 
                                                        # 현재 넣을 물건 무게만큼 빼고, 현재 물건을 넣거나

print(dp[N][K])