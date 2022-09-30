n = int(input())
a = list(map(int, input().split()))
dpA = [0 for i in range(n)]
dpB = [0 for i in range(n)]
dpC = [0 for i in range(n)]
for i in range(n):
    for j in range(i):
        if a[i] > a[j] and dpA[i] < dpA[j]:
            dpA[i] = dpA[j]
    dpA[i] += 1
for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if a[i] > a[j] and dpB[i] < dpB[j]:
            dpB[i] = dpB[j]
    dpB[i] += 1
for i in range(n):
    dpC[i] = dpA[i] + dpB[i] - 1
print(max(dpC))