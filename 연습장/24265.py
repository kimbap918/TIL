# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n - 1
#         for j <- i + 1 to n
#             sum <- sum + A[i] × A[j]; # 코드1
#     return sum;
# }


def MenOfPassion(A, n):
    sum = 0
    for i in range(1, n): # 1, 2, 3, 4, 5
        A.append(1)
        for j in range(i+1, n+1):
            A.append(1)

    for i in range(1, n): # 1, 2, 3, 4, 5
        for j in range(i+1, n+1):
            sum += A[i] * A[j]
            
    return sum

A = []
n = int(input())
print(MenOfPassion(A, n))
# i는 [1, n-1], j는 [i+1, n] 이다. 
# i가 n-1번 도는 동안 j는 순서대로 n-1, n-2, n-3, ... , 1번 돌게 된다. 
# 따라서 n-1 + n-2 + ... + 1 이 답이 된다. 
# 등차가 1인 등차수열의 합을 구하면 되므로 첫째 줄에는 n*(n-1)/2 를 출력해주면 된다.
print(int(n*(n-1)/2))
print(2)

