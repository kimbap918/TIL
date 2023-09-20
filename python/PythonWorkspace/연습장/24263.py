# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n
#         sum <- sum + A[i]; # 코드1
#     return sum;
# }
A = []
def MenOfPassion(A, n):
    answer = 0
    for i in range(n):
        A.append(1)
        answer += A[i]
    return answer;

# 주어진 함수의 for문이 항상 n에 비례하므로,
# 수행 횟수는 n, 수행 시간은 항상 1이 된다.

n = int(input())
print(MenOfPassion(A, n))

# answer
print(input())
print(1)