a, b, c = map(int, input().split())
d = [a, b, c]
for i in range(len(d)):
    if d[i] % 2 == 0:
        print("even")
    elif d[i] % 2 == 1:
        print("odd")

