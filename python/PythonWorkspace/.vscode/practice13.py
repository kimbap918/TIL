#문자열 포맷
#print("a" + "b")
#print("a", "b")

# 1. %d % 
# 2. {}.format 
# 3. {변수}.format(변수=값) 
# 4. 변수 선언 후 print(f {변수}) 

# 방법 1
print("나는 %d살입니다." % 20) #d 정수
print("나는 %s을 좋아해요." % "파이썬") #s 문자열
print("Apple은 %c로 시작해요." % "A") #c 문자
# %s
print("나는 %s살입니다." % 20)
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("빨간", "파란"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요".format(age=20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요".format(color="빨간", age=20))

#방법 4
color =  "빨간"
age = 20
print(f"나는 {age}살이며, {color}색을 좋아해요.")