import sys
input = sys.stdin.readline

N, C = map(int, input().split())
X = list(int(input()) for i in range(N))
start, end = 1, max(X)
X.sort()


def binary_search(arr, start, end):
    res = 0
    while start <= end:
        mid = (start+end) // 2
        current = arr[0]
        cnt = 1
        for i in range(1, len(arr)):
            if arr[i] >= current + mid:
                cnt += 1
                current = arr[i]
        if cnt >= C:
            start = mid + 1
            res = mid
        else:
            end = mid - 1
    return res

print(binary_search(X, start, end))
