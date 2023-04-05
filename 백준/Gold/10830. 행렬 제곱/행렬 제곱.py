import sys
input = sys.stdin.readline

def multiple_matrix(N, matrix_A, matrix_B):
    res = [list(0 for _ in range(N)) for _ in range(N)]
    # 행렬 곱셈for i in range(N):
    for i in range(N):
        for j in range(N):
            for k in range(N):
                res[i][j] += matrix_A[i][k] * matrix_B[k][j]
            res[i][j] %= 1000
    return res

def divide_matrix(N, B, matrix):
    if B == 1:
        return matrix
    else:
        temp = divide_matrix(N, B//2, matrix)
        
        if B%2 == 0:
            return multiple_matrix(N, temp, temp)
        else:
            return multiple_matrix(N, multiple_matrix(N, temp, temp), matrix)
        
N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
res = divide_matrix(N, B, A)

for i in res:
    for j in i:
        print(j%1000, end=' ')
    print('')    