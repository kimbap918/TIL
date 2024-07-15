n = int(input())
result = []
for i in range(1, n + 1):
    for j in range(i, n // i + 1):
        if (n / i / j).is_integer():
            result.append([i, j, n // i // j])
result = sorted(result, key=lambda x:sum(x))
print(*result[0])