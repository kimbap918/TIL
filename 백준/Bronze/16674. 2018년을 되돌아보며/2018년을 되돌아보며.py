N = list(map(int, str(input())))
dict_2018 = {2:0, 0:0, 1:0, 8:0} #dict로 인풋 받음
answer = False #0일 경우 탈출문

for i in N:
    try:
        dict_2018[i] += 1
    except: #2018이 아닌 다른 수가 있을 경우
        print(0)
        answer = True
        break
        
if answer == False:
    if dict_2018[2] != 0 and dict_2018[0] != 0 and dict_2018[1] != 0 and dict_2018[8] != 0:
        if dict_2018[2] == dict_2018[0] == dict_2018[1] == dict_2018[8]:
            print(8)
        else:
            print(2)
    else:
        print(1)