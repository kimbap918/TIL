row = []
for i in range(0, 46):
    for j in range(i):
        row.append(i)
A, B = map(int, input().split())
print(sum(row[A-1:B]))