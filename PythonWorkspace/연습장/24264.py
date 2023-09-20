# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n
#         for j <- 1 to n
#             sum <- sum + A[i] × A[j]; # 코드1
#     return sum;
# }

A = []
def MenOfPassion(A, n):
    sum = 0
    for i in range(0, n):
        for j in range(0, n):
            A.append(1)
            sum += A[i] * A[j]
    return sum

n = int(input())
print(MenOfPassion(A, n))

print(n*n)
print(2)