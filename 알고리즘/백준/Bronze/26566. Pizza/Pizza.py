from math import pi

for _ in range(int(input())) :
    A, P1 = map(float, input().split())
    R, P2 = map(float, input().split())
    val1, val2 = A / P1, (pi * R**2) / P2
    print(["Slice of pizza", "Whole pizza"][val1 < val2])