import sys
input = sys.stdin.readline
N, M = map(int, input().split()) # 4 3
# N+1 크기로 2차원 리스트 생성
dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
nums_table = []

for _ in range(N):
    nums = list(map(int, input().split()))
    nums_table.append(nums)

for i in range(N): # 0 1 2 3 4 행
    for j in range(N): # 0 1 2 3 4 열
        # dp의 1번째 1번요소부터 저장, (dp[0][1] + dp[1][0] - dp[0][0]) + nums_table[0][0](1)
        # dp[2][1] = dp[1][1](1) + dp[2][0](0) - dp[1][0](0) + nums_table[1][0](2)
        # 구하는 dp의 이전행 dp + 다음행 이전열 dp - 이전행 이전열 dp + 숫자가 저장된 테이블위치의 값 
        # dp의 각 행별 마지막 요소는 해당 구간까지의 합임. 10, 24, 42, 64
        dp[i+1][j+1] = (dp[i][j+1] + dp[i+1][j] - dp[i][j]) + nums_table[i][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    # dp[3][4](42) - (dp[1][4](10) + dp[3][1](6) - dp[1][1](1))
    print(dp[x2][y2] - (dp[x1-1][y2] + dp[x2][y1-1] - dp[x1-1][y1-1]))