n, x, k = map(int, input().split())
arr = []
for i in range(0, n):
    arr.append(i + 1)
change = [list(map(int, input().split())) for _ in range(k)]

for i in range(k):
    arr[change[i][0] - 1], arr[change[i][1] - 1] = arr[change[i][1] - 1], arr[change[i][0] - 1]

print(arr.index(x) + 1)