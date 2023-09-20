rub_duck = input()
rub_duck_end = 1
Q = []
if rub_duck == "고무오리 디버깅 시작":
    rub_duck_end = 0

while rub_duck_end != True:
    baek_joon = input()
    if baek_joon == "문제":    
        Q.append(baek_joon)

    if baek_joon == "고무오리" and len(Q) >= 1:
        Q.pop()
    elif baek_joon == "고무오리" and len(Q) == 0:
        Q.append("문제")
        Q.append("문제")

    if baek_joon == "고무오리 디버깅 끝":
        if len(Q) >= 1:
            print("힝구")
        elif len(Q) == 0:
            print("고무오리야 사랑해")
        rub_duck_end = True
