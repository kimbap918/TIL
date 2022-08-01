
om = {"black":"0", "brown":"1", "red":"2", "orange":"3", "yellow":"4",
    "green":"5", "blue":"6", "violet":"7", "grey":"8", "white":"9"}

A = input()
B = input()
C = input()
cnt = 0
om_sum = om.get(A)+om.get(B)+(int(om.get(C))*"0")

for i in range(len(om_sum)):
    if om_sum[i] != "0":
        cnt += 1 

if cnt != 0:
    print(om_sum)
elif cnt == 0:
    print(0)
