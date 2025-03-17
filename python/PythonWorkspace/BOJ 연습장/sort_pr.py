N = int(input())
arr = []

for i in range(N):
    m = int(input())
    arr.append(m)

arr = sorted(arr, reverse=True)

for i in arr:
    print(i, end=' ')
