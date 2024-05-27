# 1부터 n까지의 합을 만드는 함수(재귀조건)
N = int(input())

def recursive_plus(N):
    if N == 1:
        return 1 
    else:
        return N + recursive_plus(N-1)



print(recursive_plus(N))


# X를 n번 곱하는 함수(재귀조건)

def recursive_mul(x, N):
    if N == 0:
        return 1 
    else:
        return x * recursive_mul(x, N-1)

print(recursive_mul(2, 10))