c = s = 100
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a > b:
        s -= a
    elif a < b:
        c -= b
print(c)
print(s)