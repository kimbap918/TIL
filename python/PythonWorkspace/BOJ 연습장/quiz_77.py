A = list(map(int, input().split()))
B = list(map(int, input().split()))
a = 0
b = 0
gu = -1
for i in range(len(A)):
    if A[i] < B[i]:
        b += 3
    elif A[i] == B[i]:
        a += 1
        b += 1
    else:
        a += 3

if a < b:
    print(a, b)
    print("B")
elif a > b:
    print(a, b)
    print("A")
elif a == b:
    for i in range(9, -1, -1):
        if A[i] == B[i]:
            gu = 0
        elif A[i] < B[i]:
            gu = 1
            break
        else:
            gu = 2
            break
    print(a, b)
    if gu == 0:
        print("D")
    elif gu == 1:
        print("B")
    else:
        print("A")
