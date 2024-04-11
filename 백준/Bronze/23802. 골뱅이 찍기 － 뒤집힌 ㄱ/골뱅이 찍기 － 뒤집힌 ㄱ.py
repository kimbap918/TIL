import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    print("@@@@@"*n)
for _ in range(n*4):
    print("@"*n)