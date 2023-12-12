import sys
input = sys.stdin.readline

n = int(input())
tmp = []
tmp.append(int(input()))
for i in range(n):
    a, b = map(int, input().split())
    tmp.append(tmp[i] + a - b)

for i in range(n + 1):
    if tmp[i] < 0:
        print(0)
        exit()
print(max(tmp))