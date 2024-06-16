R, B = map(int, input().split())
LpW = (R + 4) // 2
LW = R + B

for i in range(1, LpW):
    if (LpW - i) * i == LW:
        print(max(i, LpW-i), min(i, LpW-i))
        break