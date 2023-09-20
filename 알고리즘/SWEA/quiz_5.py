T = int(input())

for test_case in range(1, T + 1):
    a = map(int, input().split())
    b = list(a)
    c = 0
    for i in range(len(b)):
        if b[i] % 2 == 0:
            continue
        else:
            c += b[i]
    print("#{0} {1}".format(test_case, c))
