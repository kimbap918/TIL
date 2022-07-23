N = 10000
array1 = []
array2 = []
[array1.append(i) for i in range(N+1) if True]
array1[0], array1[1] = False, False

for i in range(2, int(N**0.5)+1):
    if array1[i]:
        j = 2
        while i*j <= N:
            array1[i*j] = False
            j += 1
[array2.append(i) for i in range(len(array1)) if array1[i] != False]

T = int(input())
for i in range(T):
    n = int(input())
    half = n // 2
    for j in range(half, 1, -1):
        if (n - j in array2) and (j in array2):
            print(j, n-j)
            break