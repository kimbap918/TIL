import sys
input = sys.stdin.readline

# 입력
N = int(input())
lst = list(map(int, input().split()))

res = 0
max_res = 0
for i in lst:
    if i == 0:
        res = 0
        continue
    res += 1
    max_res = max(res, max_res)
print(max_res)