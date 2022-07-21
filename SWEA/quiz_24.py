T = int(input())
b = []
c = -1
chk = True
for i in range(1, T+1):
    s = input()
    a = list(s)
    for j in range(len(a), 0, -1):
        b.append(a[j-1])
    for k in range(len(b)):
        if a[k] != b[k]:
            chk = False
            break
        elif a[k] == b[k]:
            chk = True
    if chk == False:
        c = 0
    else:
        c = 1
    print("# {0} {1}".format(i, c))
    a = []
    b = []
        
            



