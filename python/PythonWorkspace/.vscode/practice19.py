# 자료구조의 변경
# 커피숍
menu = {"커피", "우유", "주스"} #set으로 만듦.
print(menu, type(menu))

menu = list(menu) # list로 감싼다
print(menu, type(menu)) # list로 출력됨

menu = tuple(menu) #tuple로 감싼다
print(menu, type(menu)) # tuple로 출력됨

menu = set(menu)
print(menu, type(menu))

