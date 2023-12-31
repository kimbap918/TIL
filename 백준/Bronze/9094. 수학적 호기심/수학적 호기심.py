from sys import stdin

for _ in range(int(stdin.readline())):
    n, m = map(int, stdin.readline().split())
    cnt = 0
    for a in range(1, n-1):
        for b in range(a+1, n):
            if (a**2 + b**2 +m)%(a*b) == 0:
                cnt += 1
    print(cnt)