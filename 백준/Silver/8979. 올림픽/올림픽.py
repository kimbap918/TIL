# 1. 금메달 수가 더 많은 나라
# 2. 금메달 수가 같으면, 은메달 수가 더 많은 나라
# 3. 금, 은메달 수가 모두 같으면, 동메달 수가 더 많은 나라

import sys
from collections import defaultdict
input = sys.stdin.readline


N, K = map(int, input().split())
nations = defaultdict(list)

for i in range(N):
    r, g, s, b = list(map(int, input().split()))
    nations[g, s, b].append(r)

record = sorted(nations.keys(), reverse=True)
rank = 1

for i in record:
    if K in nations[i]:
        print(rank)
    rank += len(nations[i])