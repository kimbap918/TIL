def binary_search(arr, tar, start, end):
    while start <= end:
        ttl = 0
        mid = (start+end) // 2

        for x in arr:
            if x > mid:
                ttl += x - mid

        if ttl < tar:
            end = mid - 1
        else:
            res = mid
            start = mid + 1

    return res


N, M = map(int, 5,input().split())
arr = map(int, input().split())
max_dduk = max(arr)
res = 0

print(binary_search(arr, M, 0, max_dduk))