N = int(input())
card_dict = {}

for i in range(N):
    card = int(input())
    if card not in card_dict:
        card_dict[card] = 1
    else:
        card_dict[card] += 1
# items를 입력값으로 받고, 정렬 기준 key를 lamda를 이용하여-x[1], x[0]순으로 한다.
# 즉, x[1] (카드의 개수)의 -(내림차순)으로 정렬하고
# x[0] (카드 숫자)의 오름차순으로 정렬한다.   
result = sorted(card_dict.items(),key = lambda x : (-x[1],x[0]))
print(result[0][0])
   
    


