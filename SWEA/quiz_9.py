T = int(input())

for i in range(1, T+1):
    date = input()
    year = int(date[:4])
    month = int(date[4:6])
    day = int(date[6:])
    print("#{0}".format(i), end = ' ')
    b = 0
    if month < 1 or month > 12:
        print(-1)
        continue
    if month in [1,3,5,7,8,10,12]:
        if day < 1 or day > 31:
            print(-1)
            continue
    if month == 2:
        if day < 1 or day > 28:
            print(-1)
            continue
    if month in [4,6,9,11]:
        if day < 1 or day > 30:
            print(-1)
            continue
    print("%04d/%02d/%02d" %(year,month,day))

