import sys
from pprint import pprint
input = sys.stdin.readline

N, M, K = map(int, input().split()) # 열, 행, 크기
maps = [list(input().rstrip()) for _ in range(N)] # 보드의 각 행의 상태
SUM = [[0] * (M+1) for _ in range(N+1)]

# pprint(maps)
# pprint(SUM)

for c in range(1, M+1): # 행 탐색
    for r in range(1, N+1): # 열 탐색
        if (r + c) % 2 == 0: # 행+열이 짝수면, 체스판이 B여야한다
            if maps[r-1][c-1] == 'B': # 해당 체스판의 값이 B면
                SUM[r][c] = SUM[r-1][c] + SUM[r][c-1] - SUM[r-1][c-1]
            else: # 해당 체스판 값이 W면
                SUM[r][c] = SUM[r-1][c] + SUM[r][c-1] - SUM[r-1][c-1] + 1

        else: # 행+열이 홀수면, 체스판이 W여야한다 
            if maps[r-1][c-1] == 'W': # 해당 체스판 값이 W면
                SUM[r][c] = SUM[r-1][c] + SUM[r][c-1] - SUM[r-1][c-1] 
            else: # 해당 체스판 값이 B면
                SUM[r][c] = SUM[r-1][c] + SUM[r][c-1] - SUM[r-1][c-1] + 1
max_ = -float('inf')
min_ = float('inf')
for c in range(K, M+1): # K부터 행 탐색
    for r in range(K, N+1): # K부터 열 탐색
        max_ = max(SUM[r][c] - SUM[r-K][c] - SUM[r][c-K] + SUM[r-K][c-K], max_)
        min_ = min(SUM[r][c] - SUM[r-K][c] - SUM[r][c-K] + SUM[r-K][c-K], min_)

print(min(min_, max_, K*K - min_, K*K - max_))

