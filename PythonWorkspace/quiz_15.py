A, B = map(int, input().split())# A = 시 B = 분 
C = B - 45
D = A - 1
if C < 0:
    A -= 1
    B = 60
    B += C
    if D < 0:
        A = 23
elif C > 0 and B > 45:
    B = C
elif C == 0:
    B = 0
    
print(A, B) 
