import sys
input = sys.stdin.readline

N, M = map(int, input().split())

if N*100 >= M:
    print("Yes")
else:
    print("No")