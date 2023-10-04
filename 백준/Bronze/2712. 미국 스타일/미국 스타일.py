for _ in range(int(input())):
    n, s = input().split()
    if s == "kg":
        print("%.4f %s" % (float(n)*2.2046, "lb"))
    elif s == "lb":
        print("%.4f %s" % (float(n)*0.4536, "kg"))
    elif s == "l":
        print("%.4f %s" % (float(n)*0.2642, "g"))
    elif s == "g":
        print("%.4f %s" % (float(n)*3.7854, "l"))