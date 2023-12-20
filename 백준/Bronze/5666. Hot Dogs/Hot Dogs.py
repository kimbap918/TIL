while 1:
    try:
        H, P = map(int, input().split())
        print("%.2f" % (H/P))
    except EOFError:
        break