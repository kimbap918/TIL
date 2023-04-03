import sys

input = sys.stdin.readline
N, M = map(int, input().split())
matrix_A = [list(map(int, input().split())) for i in range(N)]
M, K = map(int, input().split())
matrix_B = [list(map(int, input().split())) for i in range(M)]


for n in range(N):
    ans = []
    for k in range(K):
        a = 0
        for m in range(M):
            a += matrix_A[n][m] * matrix_B[m][k]
        ans.append(a)

    print(*ans)