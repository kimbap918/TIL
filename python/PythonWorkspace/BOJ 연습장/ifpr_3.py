# 가위바위보
# srp라는 변수에 srp = "가위"일 경우 "이겼다"를 출력
# srp = "바위"인 경우 졌다.
# srp = "보"인 경우 비겼다.

import random
scp = ["가위", "바위", "보"]


while True:
    srp = input("가위, 바위, 보 중 입력하세요 : ")
    com = scp[random.randrange(0, 3)]


    if com == srp:
        print("상대 : " + com)
        print("비겼다!!")
        break
    
    elif com == "가위":
        print("상대 : " + com)
        if srp == "보":
            print("졌다ㅠㅠ")
        elif srp == "바위":
            print("이겼다!!")
        break

    elif com == "바위":
        print("상대 : " + com)
        if srp == "보":
            print("이겼다!!")
        elif srp == "가위":
            print("졌다ㅠㅠ")
        break

    elif com == "보":
        print("상대 : " + com)
        if srp == "가위":
            print("이겼다!!")
        elif srp == "바위":
            print("졌다ㅠㅠ")
        break
            


