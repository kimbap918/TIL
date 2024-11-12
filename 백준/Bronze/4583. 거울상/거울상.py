mirror1 = ['i', 'o', 'v', 'w', 'x']	# 자신과 거울상 관계
mirror2 = ['b', 'd', 'p', 'q']	# 서로 거울상 관계

while 1 :
    s = input()[::-1]	# 문자열 뒤집어서 받기
    result = ''	# 결과값
    
    if s == '#' :
        break

    for i in range(len(s)) :
        if s[i] in mirror1 :
            result += s[i]
        elif s[i] in mirror2 :
            if s[i] == 'b' :
                result += 'd'
            elif s[i] == 'd' :
                result += 'b'
            elif s[i] == 'p' :
                result += 'q'
            elif s[i] == 'q' :
                result += 'p'
    
    if len(result) == len(s) :
        print(result)
    else :
        print('INVALID')
