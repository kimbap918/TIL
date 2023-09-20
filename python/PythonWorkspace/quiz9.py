chicken = 10
waiting = 1 # 홀 안에는 현재 만석, 대기번호 1부터 시작

class SoldOutError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg
    

try:
    while(True):
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order > chicken:
            print("재료가 부족합니다.")
        else:
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다." \
                .format(waiting, order))
            waiting += 1
            chicken -= order
        if chicken == 0:
            raise SoldOutError("[남은 치킨 : {0}]".format(chicken))
except ValueError:
    print("잘못된 값을 입력하였습니다.")
except SoldOutError as err:
    print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
    print(err)

