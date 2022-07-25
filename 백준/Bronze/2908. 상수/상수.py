import sys

A, B = map(int, sys.stdin.readline().split())
rev_A = list(reversed(str(A)))
rev_B = list(reversed(str(B)))
a = ''
b = ''
for i in range(3):
    a += rev_A[i]
    b += rev_B[i]

if int(a) > int(b):
    print(a)
else:
    print(b)