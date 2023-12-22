ot = input()
while len(ot) != 4 :
    ot = "0" + ot
print(int(ot), "in Ottawa")
ot_hour, ot_min = ot[:2], ot[2:]
if int(ot_hour) - 3 < 0 : print(int(str(int(ot_hour) - 3 + 24) + ot_min), "in Victoria")
else : print(int(str(int(ot_hour) - 3) + ot_min), "in Victoria")
if int(ot_hour) - 2 < 0 : print(int(str(int(ot_hour) - 2 + 24) + ot_min), "in Edmonton")
else : print(int(str(int(ot_hour) - 2) + ot_min), "in Edmonton")
if int(ot_hour) - 1 < 0 : print(int(str(int(ot_hour) - 1 + 24) + ot_min), "in Winnipeg")
else : print(int(str(int(ot_hour) - 1) + ot_min), "in Winnipeg")
print(int(ot), "in Toronto")
if int(ot_hour) + 1 == 24 : print(int(ot_min), "in Halifax")
else : print(int(str(int(ot_hour) + 1) + ot_min), "in Halifax")
st_min = int(ot_min) + 30
if st_min >= 60 :
    st_hour = str(int(ot_hour) + 2)
    st_min -= 60
else : st_hour = str(int(ot_hour) + 1)
if st_min == 0 and st_hour != 0 : st_min = "00"
else : st_min = str(st_min)
if int(st_hour) > 23 : st_hour = str(int(st_hour) - 24)
print(int(st_hour + st_min), "in St. John's")