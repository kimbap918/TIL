A = []
cnt = 0

for i in range(10):
    N = int(input())
    A.append(N%42)

A = len(set(A))
print(A)