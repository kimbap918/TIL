# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
import collections
input = sys.stdin.readline

N = int(input())
S = sorted(list(map(int, input().split())), reverse=True)
dic = collections.Counter(S)
square = collections.deque()
ans = 0


for k, v in dic.items():
    if (v // 2) >= 1:
        for i in range(v//2):
            square.append(k)

print(square)
for i in range(1, len(square), 2):
    print(square[i])
    ans += (square[i]*square[i-1])

print(ans)




# import sys
# input = sys.stdin.readline

# N = int(input())
# pair = []
# cnt = [0 for _ in range(1000001)]
# sticks = map(int, input().split())
# for stick in sticks:
#     cnt[stick] += 1

# for length in range(1, 1000001):
#     while cnt[length] > 1:
#         cnt[length] -= 2
#         pair.append(length)

# pair.sort(reverse=True)
# print(pair)
# ans = 0
# for i in range(1, len(pair), 2):
#     ans += pair[i - 1] * pair[i]

# print(ans)