for _ in range(int(input())):
    a, b, c, d, e = map(int, input().split())
    res = a*350.34 + b*230.9 + c*190.55 + d*125.3 + e*180.9
    print("$%.2f" % (res))