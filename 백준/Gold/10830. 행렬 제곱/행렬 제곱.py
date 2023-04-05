import sys
input = sys.stdin.readline

# 행렬 곱셈 
def multiple_matrix(N, matrix_A, matrix_B):
    res = [list(0 for _ in range(N)) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                # 행렬곱셈
                # matrix[i][j] = matrix_A[i][k] * matrix_B[k][j]
                res[i][j] += matrix_A[i][k] * matrix_B[k][j]
            # 1000으로 나눈 나머지 저장
            res[i][j] %= 1000

    return res

# 2분할 후 분할정복
def divide_matrix(N, B, matrix):
    # 차수가 1일때
    if B == 1:
        # 그대로 이므로 반환
        return matrix
    # 차수가 2이상
    else:
        # B를 2분할
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

