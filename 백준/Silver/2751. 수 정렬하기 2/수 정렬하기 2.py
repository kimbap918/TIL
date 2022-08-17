import sys
input = sys.stdin.readline
N = int(input())
a = []
for _ in range(N):
    num = int(input())
    a.append(num)
    
for i in sorted(a):
    print(i)
