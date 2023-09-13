for num in range(1, int(input()) + 1) :
    if num % 7 == 0 and num % 11 != 0 : print('Hurra!')
    elif num % 7 != 0 and num % 11 == 0 : print("Super!")
    elif num % 7 == 0 and num % 11 == 0 : print("Wiwat!")
    else : print(num)