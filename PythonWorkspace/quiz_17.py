A, B, C = map(int, input().split())
if A == B and B == C: # 같은 눈이 3개가 나온 경우
    result = 10000 + (A * 1000)
elif (A == B or A == C) or (B == C or B == A): # 같은 눈이 2개가 나온 경우
    if A == B or A == C:
        result = 1000 + (A * 100)
    elif B == C or B == A:
        result = 1000 + (B * 100)
elif A != B and B != C: # 모두 다른경우
    if A > B and A > C:
        result = A * 100
    elif B > C and B > A:
        result = B * 100
    else:
        result = C * 100

print(result)