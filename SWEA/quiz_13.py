T = int(input())
A = []
B = 0
for k in range(1, T+1):
    N = int(input())
    for i in range(1, N+1):
        if i % 2 == 1:
            A.append(i)
        elif i % 2 == 0:
            A.append(-i)
    for j in range(len(A)):
        B += A[j]
    print("#{0} {1}".format(k, B))
    A = []
    B = 0