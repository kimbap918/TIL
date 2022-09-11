# 첫째 줄에 n(5 ≤ n ≤ 40)이 주어진다.
def fib(n):
    # n이 1이나 2일때는 1을 리턴하고 아니면 fib(n - 1) + fib(n - 2)를 호출한다.
    # 자기 자신을 호출할때만 카운트를 올려줌
    global cnt1
    cnt1 += 1
    if n == 1 or n == 2:
        cnt1 -= 1
        return 1  # 코드1
    else:
        return fib(n - 1) + fib(n - 2)

def fibonacci(n):
    # 미리 계산했다가 필요할때 불러서 쓰기(동적 계획법)
    global cnt2
    f[1], f[2] = 1, 1 # 피보나치수에서 맨 처음과 두번째는 항상 1, 1
    for i in range(3, n+1): # 세번째부터 n까지 피보나치 수를 계산
        cnt2 += 1 # 이때부터 카운트
        f[i] = f[i-1]+f[i-2]
    return f[n]

cnt1, cnt2 = 0, 0
f = [0 for _ in range(41)]
n = int(input())
fib(n)
fibonacci(n)
print(cnt1+1, cnt2)