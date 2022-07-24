N = int(input())

def factorial(N):
    if N == 1 or N == 0: # N이 1일때
        return 1 # 1을 반환하고 끝낸다
    return N * factorial(N-1) # N * N-1

print(factorial(N))
