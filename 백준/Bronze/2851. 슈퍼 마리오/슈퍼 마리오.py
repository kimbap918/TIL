score_list = []
sc_big = 0
for i in range(10):
    score_list.append(int(input()))
sc = sum(score_list)

if sc <= 100:
    print(sc)

else:
    for i in range(9, -1, -1):
        if sc > 100:
            sc -= score_list[i]
        elif sc == 100:
            break
        else:
            sc_big = sc + score_list[i+1]
            break

    if sc == 100:
        print(100) 
    else:
        if abs(sc-100) >= abs(sc_big-100):
            print(sc_big)
        else:
            print(sc)
