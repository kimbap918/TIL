while 1:
    n = int(input())
    if n == -1:
        break
    cp = res = 0
    for _ in range(n):
        s, t = map(int, input().split())
        res += s*(t-cp)
        cp = t
    print(f"{res} miles")