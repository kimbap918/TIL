N, M = map(int, input().split())
eggs = []

for i in range(M):
    P = int(input())
    eggs.append(P)

eggs = sorted(eggs, reverse=True)
max_profit = 0
price = 0


for i in range(len(eggs)):
    # 판매가능한 달걀 수
    egg = min(i+1, N)
    profit = eggs[i] * egg

    if profit > max_profit:
        max_profit = profit
        price = eggs[i]


print(price, max_profit)

