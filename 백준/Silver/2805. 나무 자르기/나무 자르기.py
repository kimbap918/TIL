import sys
input = sys.stdin.readline
N, M = map(int, input().split())
logs = list(map(int, input().split()))
start, end = 1, max(logs)

def binary_search(start, end):
    while start <= end:
        mid = (start+end) // 2
        log = 0
        for i in logs:
            if i >= mid:
                log += (i - mid)
        if log >= M:
            start = mid + 1
        else:
            end = mid - 1
    return end

print(binary_search(start, end))