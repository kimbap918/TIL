import sys

def f(n):
    return n*f(n-1) if n > 0 else 1

while 1:
    n = sys.stdin.readline().rstrip()
    if n == '0':
        break
    res = 0
    for i in range(1, len(n)+1):
        res += int(n[len(n)-i])*f(i)
    print(res)