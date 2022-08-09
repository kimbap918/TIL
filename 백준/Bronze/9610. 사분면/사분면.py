T = int(input())
cnt1, cnt2, cnt3, cnt4, axis = 0, 0, 0, 0, 0
for _ in range(T):
    x, y = map(int, input().split())
    if x > 0 and y > 0:
        cnt1 += 1
    elif x < 0 and y > 0:
        cnt2 += 1
    elif x < 0 and y < 0:
        cnt3 += 1
    elif x > 0 and y < 0:
        cnt4 += 1
    else:
        axis += 1
print("Q1: {}".format(cnt1))
print("Q2: {}".format(cnt2))
print("Q3: {}".format(cnt3))
print("Q4: {}".format(cnt4))
print("AXIS: {}".format(axis))