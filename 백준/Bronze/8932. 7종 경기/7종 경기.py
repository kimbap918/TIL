def track(A, B, C, P):
    return int(A * (B-P)**C)

def field(A, B, C, P):
    return int(A * (P-B)**C)

for _ in range(int(input())):
    li = list(map(int, input().split()))
    res = track(9.23076, 26.7, 1.835, li[0]) + field(1.84523, 75, 1.348, li[1]) + \
        field(56.0211, 1.5, 1.05, li[2]) + track(4.99087, 42.5, 1.81, li[3]) + \
        field(0.188807, 210, 1.41, li[4]) + field(15.9803, 3.8, 1.04, li[5]) + \
        track(0.11193, 254, 1.88, li[6])
    print(res)