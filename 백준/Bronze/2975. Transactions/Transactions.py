while 1:
    a, op, b = input().split()
    if a == b == '0':
        break
    s = int(a)-int(b) if op == 'W' else int(a)+int(b)
    print("Not allowed" if s < -200 else s)