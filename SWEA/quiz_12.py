T = input().upper()
A = list(T)
for i in range(len(A)):
    A[i] = ord(A[i])-64
    print(A[i], end = ' ')
