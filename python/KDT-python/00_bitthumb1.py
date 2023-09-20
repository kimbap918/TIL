import requests

# URL로
order_currency = 'ALL'
payment_currency = 'KRW'
URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'
response = requests.get(URL).json()
coins = response.get('data')
print(coins.get('closing_price'))
# # coins : 딕셔너리임
# # key : coin이름
# # value : 딕셔너리(코인의 정보)
# for coin in coins:
#     # closing_price 를 모두 모아보고싶다
#     # coins.get(coin) <- 코인의 정보인 딕셔너리
#     # 그 딕셔너리의 closing_price
#     print(coin, coins.get(coin).get('closing_price')) # AttributeError: 'str' object has no attribute 'get'
#     # coins 가 문자열이거나,  get(coin)이 문자열
#     if coin != 'date':
#         continue
#     print(coin, coins.get(coin).get('closing_price'))
#     print(coins.get(coin))
