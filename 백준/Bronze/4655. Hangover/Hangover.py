while 1:
    n = float(input())
    if n == 0:
        break
    i = 2
    t = 0
    while t < n:
        t += 1/i
        i += 1
    print(f"{i-2} card(s)")