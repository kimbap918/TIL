N = int(input())
price = int(input())
sale = [0]	# N이 5 미만일 때 처리하기 위한 0

if N >= 5 :
    sale.append(500)	# 500원 할인
if N >= 10 :
    sale.append(price // 10)	# 10% 할인
if N >= 15 :
    sale.append(2000)	# 2000원 할인
if N >= 20 :
    sale.append(price // 4)	# 25% 할인

result = price - max(sale)
if result < 0 :	# 원래 금액 - 할인 금액이 0 미만일 때
    result = 0	# 지불할 금액은 0원
print(result)