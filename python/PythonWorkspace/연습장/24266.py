# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n
#         for j <- 1 to n
#             for k <- 1 to n
#                 sum <- sum + A[i] × A[j] × A[k]; # 코드1
#     return sum;
# }


def MenOfPassion(A, n):
    sum = 0
    for i in range(1, n+1):
        A.append(1)
        for j in range(1, n+1):
            A.append(1)
            for k in range(1, n+1):
                A.append(1)
                sum += A[i] * A[j] * A[k] 
    return sum


A = []
n = int(input())
print(MenOfPassion(A, n))

print(n**3)
print(3)


