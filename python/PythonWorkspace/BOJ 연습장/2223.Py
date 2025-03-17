t, x, m = map(int, input().split())
# t 단위의 시간동안
# x 개의 금화를 줍는다.

min_ = 1e9

for i in range(m):
    d, s = map(int, input().split())
    min_ = min(min_, (d-1)//s)

    # 몬스터는 d만큼 떨어져있으며
    # s만큼 가까워진다

if min_ == 0:
    print(min_*x)
elif t > min_:
    print((min_+(t-min_)//2)*x)
else:
    print(t*x)