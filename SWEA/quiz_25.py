T = int(input())

for i in range(1, T+1):
    a, b, c, d = map(int, input().split())
    e = a+c
    f = b+d
    if f > 60:
        f -= 60
        e += 1
    if e > 12:
        e -= 12

    print("#{0} {1} {2}".format(i, e, f))