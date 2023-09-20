import sys
input = sys.stdin.readline

while True:
    n = float(input())
    if n == 0: break
    print('%.2f' %(1+n+n**2+n**3+n**4))