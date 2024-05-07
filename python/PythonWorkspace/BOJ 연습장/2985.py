import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

while True:
    if A + B == C:
        print(str(A)+"+"+str(B)+"="+str(C))
        break
    if A == B + C:
        print(str(A)+"="+str(B)+"+"+str(C))
        break
    elif A - B == C:
        print(str(A)+"-"+str(B)+"="+str(C))
        break
    elif A == B - C:
        print(str(A)+"="+str(B)+"-"+str(C))
        break
    elif A * B == C:
        print(str(A)+"*"+str(B)+"="+str(C))
        break
    elif A == B * C:
        print(str(A)+"="+str(B)+"*"+str(C))
        break
    elif A / B == C:
        print(str(A)+"/"+str(B)+"="+str(C))
        break
    elif A == B / C:
        print(str(A)+"="+str(B)+"/"+str(C))
        break
