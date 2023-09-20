import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
v = int(input())
cnt = 0

for i in arr:
    if i == v:
        cnt += 1
print(cnt)