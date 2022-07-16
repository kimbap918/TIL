import json
# from pprint import pprint

# 파일을 열고,
f = open('stocks.json', 'r', encoding='utf-8')
# json을 파이썬 객체 형식으로 한다!
kospi = json.load(f)
samsung = kospi['stocks'][0] # 딕셔너리
print(kospi['stocks'][0]) # 리스트

# 04.py의 큰 힌트!!
# stockName 정보랑, closePrise 정보만 가진 딕셔너리를 만들고 싶다!
result = {
    'stockName' : samsung.get('stockName'),
    'closePrice' : samsung.get('closePrice')
}

print(result)