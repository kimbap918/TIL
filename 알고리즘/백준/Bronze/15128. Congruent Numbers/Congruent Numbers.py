p1, q1, p2, q2 = map(int, input().split())
res = p1/q1 * p2/q2 / 2
if int(res) == res:
    print(1)
else:
    print(0)