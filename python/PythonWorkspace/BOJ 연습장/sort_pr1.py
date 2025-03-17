N = int(input())
arr = []

for i in range(N):
    n, m = map(str, input().split())
    m = int(m)

    arr.append([n, m])

arr = sorted(arr)


for i in arr:
    print(i[0], end=' ')

