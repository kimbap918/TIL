N = int(input())
A = input()
B = []
c = 0

for i in range(N):
    B.append(A[i])
    c += int(B[i])
print(c)