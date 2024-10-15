import sys
input = sys.stdin.readline

m = int(input())
ans = 0
rot = 0

for i in range(m):
    a, b, r = map(int,input().split())
    if(i == 0): ans = a * b
    else: ans = int(ans / a * b)
    if(r == 1): rot = 1 - rot
    
print(rot,ans)