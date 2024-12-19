n = int(input())
for i in range(65):
    k = 2 ** i - 1
    for j in range(i+1, 65):
        k *= 2
    if k == n:
        print(i)