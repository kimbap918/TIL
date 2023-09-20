#일반유닛
class Unit:
    def __init__(self, name, hp, speed): # __init__은 파이썬에서 쓰이는 생성자 
        self.name = name # self -> 멤버변수
        self.hp = hp     # 클래스 내에서 정의된 변수 
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))

#공격유닛
class AttackUnit(Unit): # 괄호를 열고 상속받을 클래스명을 넣음.
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed) # 상속받은 name과 hp를 사용
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
        AttackUnit.__init__(self, name, hp, 0,  damage) #지상 스피드 0
        Flyable.__init__(self, flying_speed)

    def move(self, location): # move를 재정의, overloading
        print("[공중 유닛 이름]")
        self.fly(self.name, location)

# 벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루저 : 공중 유닛, 체력도 굉장이 좋음, 공격력도 좋음
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("9시")
battlecruiser.move("9시")