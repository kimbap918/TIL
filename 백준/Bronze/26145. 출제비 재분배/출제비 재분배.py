n, m = map(int, input().split())
pay = list(map(int, input().split()))
result = pay + [0] * m
for i in range(n):
    tmp_ls = list(map(int, input().split()))
    for j in range(n + m):
        result[i] -= tmp_ls[j]
        result[j] += tmp_ls[j]
print(*result)