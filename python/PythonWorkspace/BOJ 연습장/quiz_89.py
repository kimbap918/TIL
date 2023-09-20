T = int(input())

for i in range(1, T+1):
    card = list(map(int, input().split()))
    hole = 0
    jjak = 0
    for num in range(len(card)):
        if num % 2 == 0:
            hole += card[num]*2
        elif num % 2 == 1:
            jjak += card[num]
    print(hole, jjak)
    digit = (hole+jjak) % 10

    if digit == 0:
        result = 0
    else:
        result = 10 - digit
    
    print("#{} {}".format(i, result))