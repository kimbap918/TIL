import sys

input = sys.stdin.readline

n = int(input())
total = 0

for i in range(1, n+1):
    total += i**3

print(total)