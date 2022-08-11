a = []
cnt = 0
for _ in range(5):
    S = input()
    a.append(S)

for i in range(len(a)):
    if "FBI" in a[i]:
        a[i] = a[i].replace("FBI", "*")
        print(a.index(a[i])+1, end = ' ')
    else:
        cnt += 1
    
if cnt == 5:
    print("HE GOT AWAY!")
    