for _ in range(int(input())):
    d, n, s, p = map(int, input().split())
    if d + p*n == n*s:
        print("does not matter")
    elif d + p*n > n*s:
        print("do not parallelize")
    else:
        print("parallelize")