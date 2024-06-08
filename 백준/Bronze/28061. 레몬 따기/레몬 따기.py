import sys
input = sys.stdin.readline

# 입력
N = int(input())
x = list(map(int, input().split()))

# xi - (N-ai) 가 최대인 걸 고른다
res = 0
for i, lemon in enumerate(x, 1):
    tmp = lemon - (N+1-i)
    res = max(res, tmp)
print(res)