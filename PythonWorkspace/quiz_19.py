T = int(input())
a = []
b = []

for i in range(T):
   A, B = map(int, input().split())
   a.append(A)
   b.append(B)

for i in range(T):
    print(a[i] + b[i])
