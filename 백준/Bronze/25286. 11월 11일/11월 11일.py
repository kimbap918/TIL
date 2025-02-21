for _ in range(int(input())) :
    y, m = map(int, input().split())
    check = False	# 윤년인지 아닌지 확인하는 변수
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0) :
        check = True	# 윤년이면 True로 변경
    
    if check :	# 윤년
        days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else :	# 윤년 X
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if m == 1 :
        print(y-1, m+11, days[m+10])
    else :
        print(y, m-1, days[m-2])