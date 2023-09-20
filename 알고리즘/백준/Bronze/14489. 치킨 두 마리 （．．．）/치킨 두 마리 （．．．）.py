A, B = map(int, input().split())
C = int(input())
print(A+B - 2*C if A+B >= 2*C else A+B)