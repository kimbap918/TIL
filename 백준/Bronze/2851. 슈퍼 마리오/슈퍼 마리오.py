sc_list = [] # 점수를 담을 리스트
sc_big = 0

for i in range(10):
    sc_list.append(int(input()))
sc = sum(sc_list)

# 입력한 점수의 총합이 100과 같거나 넘지 않을경우 
if sc <= 100:
    print(sc)
else: # 리스트의 역순으로 진행 
    for j in range(9, -1, -1):
        if sc > 100: # 점수가 100이 넘으면 
            sc -= sc_list[j] # 리스트 역순으로 sc에서 뺀다 
        elif sc == 100: # 100일경우 종료 
            break
        else:
            sc_big = sc + sc_list[j+1] # 아닐경우 sc에 직전의 값을 더한다. 
            break

    if sc == 100: # sc가 100이면 출력
        print(sc)
    else: # 아닐경우 (sc-100)의 절대값과 (sc_big-100) 
        if abs(sc-100) >= abs(sc_big-100):
            print(sc_big)
        else:
            print(sc)
