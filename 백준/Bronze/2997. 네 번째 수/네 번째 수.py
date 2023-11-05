import sys
input = sys.stdin.readline

a = list(map(int, input().split()))
a.sort()
if a[1] - a[0] == a[2] - a[1]:
    print(a[2] * 2 - a[1])
elif a[1] - a[0] > a[2] - a[1]:
    print(a[1] * 2 - a[2])
else:
    print(a[1] * 2 - a[0])