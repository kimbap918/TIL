import sys

input = sys.stdin.readline
N, M = map(int, input().split())

for i in range(M):
    b_dummy = int(input())
    book = list(map(int, input().split()))

    for j in range(b_dummy-1):
        if book[j] < book[j+1]:
            print("No")
            exit(0)
print("Yes")