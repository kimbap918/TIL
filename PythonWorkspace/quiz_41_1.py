n = int(input())
hansu = 0

for i in range(1, n+1):
    number_list = list(map(int, str(i)))
    if i < 100:
        hansu += 1
    elif number_list[1]-number_list[0] == number_list[2]-number_list[1]:
        hansu += 1
print(hansu)