import sys
input = sys.stdin.readline
K, N = map(int, input().split())
LAN = [int(input()) for i in range(K)]
# 가장 짧은 길이, 가장 긴 길이
start, end = 1, max(LAN)

while start <= end:
    mid = (start + end)//2
    line = 0
    for i in LAN:
        line += i // mid
    if line >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)