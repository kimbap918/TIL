import sys
input = sys.stdin.readline
N = int(input())
dic = {}
card = list(map(int, input().split()))
M = int(input())
sang_card = list(map(int, input().split()))
for i in sang_card:
    dic[i] = 0

for j in card:
    if j in dic:
        dic[j] = 1

for v in dic.values():
    print(v, end = ' ')

