N, M = map(int, input().split())
arr = [i for i in range(N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    val = []
    for k in range(i, j+1):
        val.append(arr[k])

    val = val[::-1]
    num = 0
    for k in range(i, j+1):
        arr[k] = val[num]
        num += 1

for k in range(1, N+1):
    print(arr[k], end=' ')


# 1 2 3 4 5
# 2 1 3 4 5
# 2 1 4 3 5
# 3 4 1 2 5

