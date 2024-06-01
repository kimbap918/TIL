import sys
input = sys.stdin.readline

res = 0
N = int(input())
for i in range(N):
    num = int(input())
    res += num-1
    
print(res+1)
    