#  a**2 + b**2 = c**2
# d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
import math

def length(x1, y1, x2, y2):
    d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return d

def checkTri(len1, len2, len3):
    tolerance = 1e-6 

    # 삼각형이 성립하지 않는 경우
    if len1 + len2 <= len3:
        return "X"

    if len1 == len2 and len2 == len3:  # 정삼각형
        return "JungTriangle"
    elif len1 == len2 or len2 == len3:  # 이등변삼각형
        if len1**2 + len2**2 < len3**2:
            return "Dunkak2Triangle"
        elif abs(len1**2 + len2**2 - len3**2) < tolerance:
            return "Jikkak2Triangle"
        else:
            return "Yeahkak2Triangle"
    else:  # 일반 삼각형
        if len1**2 + len2**2 < len3**2:
            return "DunkakTriangle"
        elif abs(len1**2 + len2**2 - len3**2) < tolerance:
            return "JikkakTriangle"
        else:
            return "YeahkakTriangle"

a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())
c1, c2 = map(int, input().split())

A = length(a1, a2, b1, b2)
B = length(b1, b2, c1, c2)
C = length(c1, c2, a1, a2)

triangle = sorted([A, B, C])
short1, short2, long = triangle
print(checkTri(short1, short2, long))
