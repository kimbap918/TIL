import sys
input = sys.stdin.readline

N, M, K = map(int, input().split()) # 행, 열, 크기
maps = [list(input().rstrip()) for _ in range(N)]
SUM = [[0] * (M+1) for _ in range(N+1)]

for r in range(1, N+1): # 열
    for c in range(1, M+1): # 행
        if (r + c) % 2 == 0:
            if maps[r-1][c-1] == 'B': # 검정이면
                SUM[r][c] = SUM[r-1][c] + SUM[r][c-1] - SUM[r-1][c-1]
            else:
                SUM[r][c] = SUM[r-1][c] + SUM[r][c-1] - SUM[r-1][c-1] + 1
        else:
            if maps[r-1][c-1] == 'W': # 흰색이면
                SUM[r][c] = SUM[r-1][c] + SUM[r][c-1] - SUM[r-1][c-1]
            else:
                SUM[r][c] = SUM[r-1][c] + SUM[r][c-1] - SUM[r-1][c-1] + 1

max_ = -float('inf')
min_ = float('inf')
for r in range(K, N+1):
    for c in range(K, M+1):
        max_ = max(SUM[r][c] - SUM[r-K][c] - SUM[r][c-K] + SUM[r-K][c-K], max_)
        min_ = min(SUM[r][c] - SUM[r-K][c] - SUM[r][c-K] + SUM[r-K][c-K], min_)

print(min(min_, max_, K*K - min_, K*K - max_))

