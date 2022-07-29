import sys

N = int(input())
card = list(map(str, sys.stdin.readline().split()))
M = int(input())
sang_card = {}
test = []
input_card = sys.stdin.readline().split()

for _ in card:
    if _ in input_card:
        test.append(_)

for i in range(len(input_card)):
    sang_card[input_card[i]] = 0

for j in range(len(test)):
    if test[j] not in sang_card:
        sang_card[test[j]] = 0
    else:
        sang_card[test[j]] += 1

for k in sang_card.values():
    print(k, end = ' ')

