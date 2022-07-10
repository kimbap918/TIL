A = []
B = 0
max = 0

for i in range(1, 10):
    N = int(input())
    A.append(N)

for j in range(i):
    if max < A[j]:
        max = A[j]
        B = j+1
print(max)
print(B)
