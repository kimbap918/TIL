while True:
    N = int(input())
    ans = 0
    if N == 0:
        break
    for i in range(1, N+1):
        ans += i

    print(ans)