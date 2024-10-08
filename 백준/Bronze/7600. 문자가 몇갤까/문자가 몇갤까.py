while 1 :
    s = input()
    if s == '#' :
        break
    lst = [0] * 26	# 알파벳 확인 리스트
    for i in s.lower() :	# 소문자로 바꿈
        if i.isalpha() :	# i가 알파벳이면
            lst[ord(i)-97] = 1	# 리스트의 해당 인덱스 1
        else :
            continue
    print(lst.count(1))