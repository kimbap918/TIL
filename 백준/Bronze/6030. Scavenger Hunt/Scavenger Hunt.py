P, Q = map(int, input().split())
plst, qlst = [], []
for i in range(1, max(P, Q) + 1) :
    if P % i == 0 : plst.append(i)
    if Q % i == 0 : qlst.append(i)
for p in plst :
    for q in qlst :
        print(p, q)
