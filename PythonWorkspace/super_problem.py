class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        #super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)

dropship = FlyableUnit()
# -> 이 경우 super().__init__()을 하면 파라미터 중 첫번째로 넣은 클래스의 __init__을 탄다.