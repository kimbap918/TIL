# 클래스 외부에서 매물 추가

class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year


    # 매물 정보 표시
    def show_detail(self):
        print("{0} {1} {2} {3} {4}년 "
        .format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))


house1 = House("강남", "아파트", "매매", "10억", "2010")
house2 = House("마포", "오피스텔", "전세", "5억", "2007") 
house3 = House("송파", "빌라", "월세", "500/50", "2000")
count = 0
info_house = [house1, house2, house3]


for i in info_house:
    count += 1
print("총 {0}대의 매물이 있습니다.".format(count))

for j in range(0, 3):
    info_house[j].show_detail()