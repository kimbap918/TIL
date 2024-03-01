for i in range(int(input())):
    leg, ch = map(int, input().split())
    cc = 2*ch - leg
    print(cc, ch-cc)