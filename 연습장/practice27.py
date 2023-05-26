from collections import deque
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
island = [[] for _ in range(M)]

for _ in range(M):
    a, b = map(int, input().split())
    island[a].append(b)
    island[b].append(a)

print(island)