N = input()
flag_1 = False
flag_2 = False

for i in N:
    if i == '7':
        flag_1 = True

if int(N) % 7 == 0:
    flag_2 = True


if flag_1 == False and flag_2 == False:
    print(0)
elif flag_1 == False and flag_2 == True:
    print(1)
elif flag_1 == True and flag_2 == False:
    print(2)
else:
    print(3)


