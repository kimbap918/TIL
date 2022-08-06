N, M = map(int, input().split())

for i in range(N):
    f_bread = input()

    for j in range(len(f_bread)-1, -1, -1):
        print(f_bread[j], end='')
    print()