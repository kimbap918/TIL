for _ in range(int(input())) :
    res = 0
    for _ in range(int(input())) :
        _, cnt, price = input().split()
        res += float(cnt) * float(price)
    print('$%.2f'%res)