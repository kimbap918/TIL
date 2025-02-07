import sys

input = sys.stdin.readline
n,m=sorted(map(int,input().split()))
if m==0:
    print("Impossible")
else:
    if n==m:
        print(int((n*2)**0.5))
    else:
        print(int((n*2+1)**0.5))