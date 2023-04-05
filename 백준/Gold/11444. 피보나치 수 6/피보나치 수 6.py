import sys
input = sys.stdin.readline

N = int(input())
matrix = [[1, 1], [1, 0]]

# 행렬 곱셈
def multiple_matrix(matrix_A, matrix_B):
    res = [[0]*2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                res[i][j] += matrix_A[i][k] * matrix_B[k][j] % 1000000007
    return res

# 분할 정복
def divide_matrix(A, B):
    # B의 값이 1이 될때까지 재귀
    if B == 1:
        return A
    else:
        # a^(B//2)
        temp = divide_matrix(A, B//2)
        if B % 2 == 0:
            return multiple_matrix(temp, temp)
        else:
            return multiple_matrix(multiple_matrix(temp, temp), A)

res = divide_matrix(matrix, N)

print(res[0][1] % 1000000007)