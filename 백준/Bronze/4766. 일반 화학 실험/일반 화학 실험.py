t1 = float(input())
while 1:
    t2 = float(input())
    if t2 == 999:
        break
    print("%.2f" % (t2-t1))
    t1 = t2