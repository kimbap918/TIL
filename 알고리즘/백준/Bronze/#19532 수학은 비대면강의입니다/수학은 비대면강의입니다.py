# 1*x + 3*y = -1
# 4*x + 1*y = 7   
# -999 부터 1000까지 x, y룰 전부 탐색
a, b, c, d, e, f = map(int, input().split())

for x in range(-999, 1000):
    for y in range(-999, 1000):
        if ((a*x) + (b*y) == c) and ((d*x) + (e*y) == f):
            print(x, y)


