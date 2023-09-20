import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# A = list(map(int, input().split()) for i in range(N))
# B = list(map(int, input().split()) for i in range(N))

A = []
B = []
for row in range(N):
    row = list(map(int, input().split()))
    A.append(row)

for row in range(N):
    row = list(map(int, input().split()))
    B.append(row)

print(A)

# for i in range(N):
#     for j in range(M):
#         print(A[i][j] + B[i][j], end=' ')
#     print()