import sys
A = []
B = []
N, X = map(int, input().split())
A = sys.stdin.readline().split()

for i in range(0, N):
    if X > int(A[i]):
       print(A[i]+" ", end='')
print('')