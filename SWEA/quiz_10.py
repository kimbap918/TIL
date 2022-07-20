T = int(input())
A = []

for i in range(1, T+1):
    if T % i == 0:
        A.append(i)
for i in range(len(A)):
    print(A[i], end=' ')