s1, s2 = map(int, input().split())
li1 = [list(map(int, input().split())) for _ in range(s1)]
li2 = [list(map(int, input().split())) for _ in range(s2)]
for i in range(s1):
    if li1[i][0] != li1[i][1]:
        print("Wrong Answer")
        exit()
for i in range(s2):
    if li2[i][0] != li2[i][1]:
        print("Why Wrong!!!")
        exit()
print("Accepted")