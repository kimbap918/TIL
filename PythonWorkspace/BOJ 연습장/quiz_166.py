import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
ans = 0
arr.sort()

for i in range(N):
    for j in range(i+1):
        ans += arr[j]
print(ans)