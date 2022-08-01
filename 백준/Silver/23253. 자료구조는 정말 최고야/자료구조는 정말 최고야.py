import sys

N, M = map(int, sys.stdin.readline().split())

for i in range(M):
    b_dummy = int(sys.stdin.readline())
    book = list(map(int, sys.stdin.readline().split()))

    for j in range(b_dummy-1):
        if book[j] < book[j+1]:
            print("No")
            exit(0)
print("Yes")