#일반유닛
class Unit:
    def __init__(self, name, hp): # __init__은 파이썬에서 쓰이는 생성자 
        self.name = name # self -> 멤버변수
        self.hp = hp     # 클래스 내에서 정의된 변수 

#공격유닛
class AttackUnit(Unit): # 괄호를 열고 상속받을 클래스명을 넣음.
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp) # 상속받은 name과 hp를 사용
        self.damage = damage

# 드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송 공격기능 x
#날수있는 기능을 가지는 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable): # 다중상속
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie, "3시")
