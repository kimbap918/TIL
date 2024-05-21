# 가위바위보
# srp라는 변수에 srp = "가위"일 경우 "이겼다"를 출력
# srp = "바위"인 경우 졌다.
# srp = "보"인 경우 비겼다.

# import random

# def play():
#     scp = ["가위", "바위", "보"]
#     win = 0
#     lose = 0
#     draw = 0

#     for _ in range(10):
#         srp = input("가위, 바위, 보 중 입력하세요 : ")
#         if srp != "가위" and srp != "바위" and srp != "보":
#             print("잘못내셨습니다.")
#             lose += 1
#             continue

#         com = scp[random.randrange(0, 3)]

#         if com == srp:
#             print("상대 : " + com)
#             print("비겼다!!")
#             draw += 1

#         elif com == "가위":
#             print("상대 : " + com)
#             if srp == "보":
#                 print("졌다ㅠㅠ")
#                 lose += 1
#             elif srp == "바위":
#                 print("이겼다!!")
#                 win += 1

#         elif com == "바위":
#             print("상대 : " + com)
#             if srp == "보":
#                 print("이겼다!!")
#                 win += 1
#             elif srp == "가위":
#                 print("졌다ㅠㅠ")
#                 lose += 1

#         elif com == "보":
#             print("상대 : " + com)
#             if srp == "가위":
#                 print("이겼다!!")
#                 win += 1
#             elif srp == "바위":
#                 print("졌다ㅠㅠ")
#                 lose += 1

#     print(f'승 :{win}')
#     print(f'패 :{lose}')
#     print(f'비김 :{draw}')

# play()


                


import random

def play():
    scp = ["가위", "바위", "보"]
    win = 0
    lose = 0
    draw = 0

    for _ in range(10):
        srp = input("가위, 바위, 보 중 입력하세요 : ")
        if srp not in scp:
            print("잘못내셨습니다.")
            lose += 1
            continue
        
        com = random.choice(scp)
        print(f"상대 : {com}")

        if com == srp:
            print("비겼다!!")
            draw += 1
        elif (srp == "가위" and com == "보") or (srp == "바위" and com == "가위") or (srp == "보" and com == "바위"):
            print("이겼다!!")
            win += 1
        else:
            print("졌다ㅠㅠ")
            lose += 1

    print(f'승 : {win}')
    print(f'패 : {lose}')
    print(f'비김 : {draw}')

play()
