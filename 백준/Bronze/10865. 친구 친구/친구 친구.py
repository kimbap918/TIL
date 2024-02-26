import sys
input = sys.stdin.readline

# 입력
n, m = map(int, input().split())

cnt = [0] * (n+1)
for i in range(m):
    a, b = map(int, input().split())
    cnt[a] += 1
    cnt[b] += 1
for i in range(1, n+1):
    print(cnt[i])