N = int(input())
# 문제를 쉽게 풀기 위한 [0] 추가
cards = list(map(int, input().split())) + [0] 

result = []
tmp = []
for i in range(N) :
    tmp.append(cards[i])

	# 이웃한 수가 아니라면 result에 추가 및 tmp 초기화
    if (cards[i+1] - cards[i]) != 1 :
        result.append(tmp)
        tmp = []

total = 0
for j in result :
    total += j[0]

print(total)
