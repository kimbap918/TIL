alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for _ in range(int(input())) :
    n, l = input().split()
    idx = alpha.index(l)
    for i in range(1, int(n) + 1) :
        print(alpha[idx] * i)
        idx += 1
        if idx == 26 : idx = 0
    print()