from random import *

customer = range(1, 51) # 1~50까지 손님 생성
customer = list(customer)
count = 0

for i in customer:
    time = randint(5, 50)
    if time >= 5 and time <= 15:
        match = "[o]"
        count += 1
    else:
        match = "[ ]"
    print("{0} {1}번째 손님 (소요시간 : {2}분)".format(match, i, time))
print("총 탑승 승객 : {0}분".format(count))

