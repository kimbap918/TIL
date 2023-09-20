a = []
for _ in range(5):
    N = int(input())
    a.append(N)

a.sort()
print(int(sum(a)/5))
print(a[2])
