#Print 0 if the number does not contain 7 and is not divisible by 7.
# 주어진 숫자에 7이 포함되어 있지 않고 7로 나누어지지 않는것
# Print 1 if the number does not contain 7 but is divisible by 7.
# 주어진 숫자에 7이 포함되지 않지만 7로 나누어지는것 
# Print 2 if the number does contain 7 but is not divisible by 7.
# 주어진 숫자에 7이 포함되지만, 7로 나누어지지 않는것
#Print 3 if the number does contain 7 and is divisible by 7.
# 주어진 숫자에 7이 포함되고 7로 나누어지는것

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



