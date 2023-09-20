N, M = map(int, input().split())
arr = [i for i in range(N+1)]

for _ in range(M):
    temp = 0
    i, j = map(int, input().split())
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

for k in range(1, N+1):
    print(arr[k], end=' ')
