for _ in range(int(input())):
    C = G = 0
    for i in range(int(input())):
        c, g = map(float, input().split())
        C += c
        G += c*g
    print("%d %.1f" %(C, G/C))