import sys

input = sys.stdin.readline
N, M = map(int, input().split())
matrix_A = [list(map(int, input().split())) for i in range(N)]
M, K = map(int, input().split())
matrix_B = [list(map(int, input().split())) for i in range(M)]

# NxN, NxK 행렬을 곱하면 NxK행렬이 된다.
# 행렬 A
# 1 2
# 3 4
# 5 6

# 행렬 B
# -1 -2 0
# 0 0 3

# 행렬 AxB
# -1 -2 6
# -3 -6 12
# -5 -10 18

# AxB의 2행 2열 -6을 구하려면
# 행렬 A의 2행 3,4
# 행렬 B의 2열 -2, 0
# (3*-2) + (4*0) = -6

# AxB의 3행 2열 -10을 구하려면?
# 행렬 A의 3행 5, 6
# 행렬 B의 2열 -2, 0
# (5*-2) + (6*0) = -10 
for n in range(N):
    ans = []
    for k in range(K):
        a = 0
        for m in range(M):
            a += matrix_A[n][m] * matrix_B[m][k]
        ans.append(a)
    print(*ans)
