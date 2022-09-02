import math
T = int(input())
# 출발점과 도착점이 주어지는 원 안에 속하는지 속하지 않는지 확인한다.
# 둘 다 속하거나, 둘 다 속하지 않으면 진입이나 이탈을 할 필요가 없다.
# 하나는 속하고, 하나는 속하지 않을때 cnt를 1 증가시켜 준다.
for _ in range(T):
    cnt = 0
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    for _ in range(n):
        x, y, r = map(int, input().split())
        d1 = math.sqrt(((x1 - x) ** 2) + ((y1 - y) ** 2))
        d2 = math.sqrt(((x2 - x) ** 2) + ((y2 - y) ** 2))
        if (d1 < r and d2 > r) or (d1 > r and d2 < r):
            cnt += 1
    print(cnt)