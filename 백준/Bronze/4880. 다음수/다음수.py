while 1:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    if b-a == c-b:
        print(f"AP {c + c-b}")
    else:
        print(f"GP {c * (c//b)}")