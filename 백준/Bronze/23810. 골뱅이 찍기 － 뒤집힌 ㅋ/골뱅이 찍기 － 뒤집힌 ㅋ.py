import sys
input = sys.stdin.readline

# 입력
N = int(input())

for i in range(N*5):
    if i < N:
        for j in range(N*5):
            print("@", end="")
    elif 2*N <= i < 3*N:
        for j in range(N*5):
            print("@", end="")
    else:
        for j in range(N):
            print("@", end="")
    print()