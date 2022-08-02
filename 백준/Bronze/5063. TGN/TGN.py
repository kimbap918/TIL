import sys

N = int(input())
input = sys.stdin.readline

for i in range(N):
    r, e, c = map(int, input().split())
    if r > (e-c):
        print("do not advertise")
    elif r < (e-c):
        print("advertise")
    elif r == (e-c):
        print("does not matter")