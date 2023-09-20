T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    cnt = 0
    a = []
    for i in range(N, M+1):
        zero = str(i)
        cnt += zero.count('0')
    print(cnt)