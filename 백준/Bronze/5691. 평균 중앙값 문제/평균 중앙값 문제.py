import sys

input = sys.stdin.readline
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    else:
        print(2 * a - b)