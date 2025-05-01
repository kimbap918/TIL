N = int(input())
arr = list(map(int, input().split()))
M = int(input())

def check(arr):
    start, end = 0, max(arr)

    while start <= end:
        mid = (start+end) // 2
        total = sum(min(mid, x) for x in arr)

        if total > M:
            end = mid - 1
        else:
            start = mid + 1

    return end

if sum(arr) <= M:
    print(max(arr))
else:
    print(check(arr))
