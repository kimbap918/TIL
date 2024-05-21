import time

def vendingmachine():
    coke = 101

    try:
        money = int(input("현금을 입력하세요 : "))
    except ValueError:
        print("숫자로 입력해주세요.")
        return

    while True:
        if coke == 0:
            print("콜라가 없습니다.")
            break

        if money < 1000:
            print("잔액이 부족합니다. 돈을 더 넣어주세요.")
            break

        print(f'남은 콜라 {coke}개')
        try:
            earn = int(input("콜라를 구매하시겠습니까?(1000원 차감) [구매 1번, 취소 0번] : "))
        except ValueError:
            print("숫자로 입력해주세요.")
            continue

        if earn == 1:
            time.sleep(1)
            print("coke 1개를 받으세요")
            coke -= 1
            money -= 1000
            time.sleep(0.5)
            print(f'잔액은 {money}원 입니다.')
            print()
        elif earn == 0:
            time.sleep(0.5)
            print("구매를 취소합니다.")
            time.sleep(0.5)
            print(f'잔액을 반환합니다.') 
            break
        else:
            print("올바른 번호를 입력해주세요.")

    print("이용해 주셔서 감사합니다.")

vendingmachine()
