# 모듈 -> 필요한것들끼리 교체하기 쉬운 부품처럼 만드는것
# 모듈은 같은 워크스페이스 내 경로에 있어야하거나, 파이썬 라이브러리가 모여있는 폴더에 있어야함

# 일반 가격
def price(people):
    print("{0}명 가격은 {1}원 입니다.".format(people, people * 10000))

# 조조 할인 가격
def price_morning(people):
    print("{0}명 조조 할인 가격은 {1}원 입니다.".format(people, people * 6000))

# 군인 할인 가격
def price_soldier(people):
    print("{0}명 군인 할인 가격은 {1}원 입니다.".format(people, people * 4000))