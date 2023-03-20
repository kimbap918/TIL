# Equilateral :  세 변의 길이가 모두 같은 경우
# Isosceles : 두 변의 길이만 같은 경우
# Scalene : 세 변의 길이가 모두 다른 경우
# 가장 긴 변 길이보다 나머지 두 변의 합이 짧은경우 삼각형 성립이 되지않는다.

while True:
    bucket = []
    A, B, C = map(int, input().split())
    if A == 0 and B == 0 and C == 0:
        break
    bucket.append(A)
    bucket.append(B)
    bucket.append(C)
    max_val = max(bucket) 
    bucket.pop(bucket.index(max_val))
    if max_val >= sum(bucket):
        print("Invalid")
    elif A == B and A == C:
        print("Equilateral")
    elif A == B or B == C or A == C:
        print("Isosceles")
    else:
        print("Scalene")
