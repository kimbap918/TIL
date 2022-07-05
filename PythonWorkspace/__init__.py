# __init__

class Unit:
    def __init__(self, name, hp, damage): # __init__은 파이썬에서 쓰이는 생성자 
        self.name = name # self -> 멤버변수
        self.hp = hp     # 클래스 내에서 정의된 변수 
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5) # 마린이나 탱크처럼 class로 부터 만들어지는 것 -> 객체
marine2 = Unit("마린", 40, 5) # 마린와 탱크는 Unit class의 인스턴스
tank = Unit("탱크", 150, 35)


# 레이스 : 공중 유닛, 비행기. 클로킹
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만듦
wraith2 = Unit("레이스", 80, 5)
wraith2.clocking = True # 객체에 추가로 변수를 외부에서 만들어 사용할수있음.

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith1.name))