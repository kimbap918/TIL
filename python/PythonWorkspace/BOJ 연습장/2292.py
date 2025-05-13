N = int(input())

if N == 1:
    print(1)
else:
    L = 1

    while 1 + 3 * L * (L-1) < N:
        L += 1


print(L)



