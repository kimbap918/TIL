A = list(input())
B = list(input().split())

for i in range(len(A)) :
    for j in range(len(B)) :
        if A[i] == B[j] :
            A[i] = A[i].lower()
            continue

print(''.join(A))
