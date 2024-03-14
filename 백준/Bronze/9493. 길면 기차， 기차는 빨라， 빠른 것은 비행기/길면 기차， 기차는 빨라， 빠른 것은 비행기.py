while 1:    
    M, A, B = map(int, input().split())
    if M == A == B == 0:
        break
    t = round((M/A - M/B)*3600)
    h = t//3600
    m = (t%3600) // 60
    s = t%60
    print("%d:%02d:%02d" % (h, m, s))