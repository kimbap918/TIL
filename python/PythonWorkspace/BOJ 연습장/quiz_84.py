import sys

N = int(input()) # 제시된 숫자 카드의 개수 
# 숫자 카드에 적힌 정수  
cards = list(map(str, sys.stdin.readline().split()))
# 상근이가 가지고 있는 숫자카드 수
M = int(input())

sang_card = {}
test = []
# 상근이의 카드 
input_card = sys.stdin.readline().split()

for card in cards:
    if card in sang_card:
        sang_card[card] += 1
    else:
        sang_card[card] = 1

for target in input_card:
    result = sang_card.get(target)
    if result == None:
        print(0, end=" ")
    else:
        print(result, end=" ")
# for k in sang_card.values():
#     print(k, end = ' ')




# import sys
# N = int(input())
# card = list(map(str, sys.stdin.readline().split()))
# M = int(input())
# sang_card = {}
# test = []
# input_card = sys.stdin.readline().split()
# for _ in card:
#     if _ in input_card:
#         test.append(_)
# for i in range(len(input_card)):
#     sang_card[input_card[i]] = 0

# for j in range(len(test)):
#     if test[j] not in sang_card:
#         sang_card[test[j]] = 0
#     else:
#         sang_card[test[j]] += 1

# for k in sang_card.values():
#     print(k, end = ' ')