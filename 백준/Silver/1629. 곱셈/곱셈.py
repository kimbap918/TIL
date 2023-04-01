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