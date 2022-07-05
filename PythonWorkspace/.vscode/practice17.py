# 튜플
# list와는 다르게 내용 변경이나 추가는 불가능하지만
# list보다 속도가 빠름

menu = ("돈까스", "치즈까스") #()와 , 로 구성
print(menu[0])
print(menu[1])

# menu.add("생선까스") 오류

name = "김종국"
age = 20
hobby = "coding"
print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)