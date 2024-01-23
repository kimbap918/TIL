a1, h1 = map(int, input().split())
a2, h2 = map(int, input().split())
a, b = h1//a2 + (1 if h1%a2 else 0), h2//a1 + (1 if h2%a1 else 0)
if a == b:
    print("DRAW")
elif a > b:
    print("PLAYER A")
else:
    print("PLAYER B")