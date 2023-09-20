N, M = map(int, input().split())
arr = [0 for i in range(N+1)]

for _ in range(M):
    i, j, k = map(int, input().split())
    for n in range(i, j+1):
        arr[n] = k

for i in range(1, N+1):
    print(arr[i], end=' ')