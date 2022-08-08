a = []

for _ in range(9):
    dwarf = int(input())
    a.append(dwarf)
    total = sum(a)

    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if 100 == total - (a[i] + a[j]):
                no_dwarf1, no_dwarf2 = a[i], a[j] # 25, 15


a.remove(no_dwarf1)
a.remove(no_dwarf2)
a.sort()
for k in range(len(a)):
    print(a[k])

