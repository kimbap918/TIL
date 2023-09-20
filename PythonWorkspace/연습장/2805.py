import sys
input = sys.stdin.readline

N, M = map(int, input().split())
logs = list(map(int, input().split()))
start, end = 1, max(logs)

while start <= end:
    mid = (start+end) // 2
    res = 0

    for i in logs:
        if i >= mid:
            res += (i - mid)

    if res >= M:
        # 19 = 20 - 1
        start = mid + 1
    else:
        end = mid - 1

print(end)

