N = int(input())

def fib(N):
    if N == 0:
        return 0
    if N == 1 or N == 2: # N이 0 or 1일때
        return 1 # 1을 반환하고 끝낸다
    return fib(N-1) + fib(N-2)

print(fib(N))