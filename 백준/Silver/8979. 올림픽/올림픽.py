# 1. 금메달 수가 더 많은 나라
# 2. 금메달 수가 같으면, 은메달 수가 더 많은 나라
# 3. 금, 은메달 수가 모두 같으면, 동메달 수가 더 많은 나라

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nations = []

for i in range(N):
    nation = list(map(int, input().split()))
    nations.append(nation)


nations.sort(key=lambda x : (-x[1], -x[2], -x[3]))


rank = 1
same_rank = 1
prev = nations[0][1:]
rank_dict = {nations[0][0] : 1}


# print(rank_dict)

for i in range(1, N):
    curr = nations[i][1:]
    if curr == prev:
        rank_dict[[i][0]] = rank
        same_rank += 1

    else:
        rank += same_rank
        same_rank = 1
        prev = curr
        rank_dict[[i][0]] = rank


print(rank_dict[K-1])