import sys
input = sys.stdin.readline
N = int(input())
arr = []
rapin = ["ChongChong"]
for i in range(N):
    p1, p2 = map(str, input().split())
    if p1 in rapin or p2 in rapin:
        rapin.append(p1)
        rapin.append(p2)
print(len(set(rapin)))