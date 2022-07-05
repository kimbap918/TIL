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

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage)) # 이름과 공격력은 self로 클래스 자기 자신의 멤버를 사용, location은 값을 가져옴
    
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))