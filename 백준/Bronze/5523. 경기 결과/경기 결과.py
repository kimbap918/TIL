from sys import stdin

a = b = 0
for _ in range(int(stdin.readline())):
    A, B = map(int, stdin.readline().split())
    if A > B:
        a += 1
    elif A < B:
        b += 1
print(a, b)