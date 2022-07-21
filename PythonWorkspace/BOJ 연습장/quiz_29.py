import sys
A = []
B = []
C = []

while A != 0 and B != 0:
    A, B = map(int, sys.stdin.readline().split())
    C.append(A+B)
    if A == 0 and B == 0:
        C.pop(-1)
        break
for i in range(len(C)):
    print(C[i])


