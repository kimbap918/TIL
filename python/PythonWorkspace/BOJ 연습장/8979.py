# 1. 금메달 수가 더 많은 나라
# 2. 금메달 수가 같으면, 은메달 수가 더 많은 나라
# 3. 금, 은메달 수가 모두 같으면, 동메달 수가 더 많은 나라

# import sys
# from collections import defaultdict
# input = sys.stdin.readline


# N, K = map(int, input().split())
# nations = defaultdict(list)

# for i in range(N):
#     r, g, s, b = list(map(int, input().split()))
#     nations[g, s, b].append(r)

# record = sorted(nations.keys(), reverse=True)
# rank = 1

# for i in record:
#     if K in nations[i]:
#         print(rank)
#     rank += len(nations[i])

# # print(record)


import sys
input = sys.stdin.readline


N, K = map(int, input().split())
nations = []

for i in range(N):
    r, g, s, b = list(map(int, input().split()))
    nations.append([r, g, s, b])

nations.sort(key=lambda x : (-x[1], -x[2], -x[3]))

rank = 1
rank_dict = {}



# # print(rank_dict)
rank_dict[nations[0][0]] = rank

for i in range(1, N):
    if nations[i][1:] == nations[i-1][1:]:
        rank_dict[nations[i][0]] = rank
    else:
        rank = i+1
        rank_dict[nations[i][0]] = rank

print(rank_dict[K])

# print(rank_dict[K])