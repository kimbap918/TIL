import sys

input = sys.stdin.readline
A, B, C = map(int, input().split())

# for i in range(B):
#     temp = A
#     A *= temp
#     print(A)

# print(A%C)


def fpow(A, B):
    # 제곱 하는 횟수가 1이면
    if B == 1:
        # 그냥 반환한다
        return A % C
    # 제곱 하는 횟수가 1 이상일 때
    else:
        # A와 B를 반으로 나눈 몪을 함수 호출
        x = fpow(A, B//2) # ex) 10 11 12 경우 10 100 10000
        if B % 2 == 0:
            return (x * x) % C # 100
        else:
            return (x * x * A) % C # 100000, 100000000000
print(fpow(A, B))

# def fpow2(A, B):
#     res = 1
#     while B:
#         # 차수가 짝수일때
#         if B % 2 == 0:
#             # A를 res에 곱누적
#             res *= A
#         # A에 A를 곱누적    
#         A *= A
#         # B를 2로 나눈 몫을 누적
#         B //= 2
#     return res%C

# print(fpow2(A, B))


# 예를들어 거듭제곱되는 수치가 짝수일 때와 홀수일 때를 예로들면 다음과 같다.

# A^4 = (A^2)^2 (짝수일때)
# A^5 = A * A^4 = A * (A^2)^2 (홀수일때)

# 만약 A^8이 있다면 원래는 A*A*A*A*A*A*A*A 으로 곱셈 연산을 7번 해야 하지만, 
# A^8을 ((A^2)^2)^2 으로 변경하면 A*A=A', A'^2=A'' 이라 할 시 
# 최종적으로 A'을 구하는데에 A*A로 곱셉 한번, A''=A'*A'을 구하는데도 마찬가지로 곱셈 한번, 
# 최종적으로 A''*A''을 구하는데 곱셈 한 번이 들어간다. 즉 7번의 연산이 3번의 연산으로 줄어든다!