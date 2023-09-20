N = int(input())
a = []
for i in range(N):
    num = int(input())
    a.append(num)
b = sorted(a)

for i in b:
    print(i)