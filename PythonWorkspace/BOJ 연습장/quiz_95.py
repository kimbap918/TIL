
om = {"black":0, "brown":1, "red":2, "orange":3, "yellow":4,
    "green":5, "blue":6, "violet":7, "grey":8, "white":9}

A = input()
B = input()
C = input()
cnt = 0
om_sum = ((om.get(A)*10)+om.get(B))*(10**om.get(C))
print(om_sum)


