import sys
input = sys.stdin.readline

n = int(input())
numlist = list(map(int, input().split()))

baseball = 0 
for idx, num in enumerate(numlist, 1):
    if idx != num:
        baseball += 1
print(baseball)