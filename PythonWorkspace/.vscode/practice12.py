python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper()) #해당 문자가 대문자인지 
print(len(python)) #문자의 길이
print(python.replace("Python", "Java")) #replace 바꾸기 함수

index = python.index("n")
print(index)
index = python.index("n", index + 1) #index의 첫번째 위치 다음에서 다시 n을 찾는것
print(index)

print(python.find("n"))
print(python.find("Java")) #index와 기능이 같으나, 원하는 값이 없을 시 -1을 반환
#print(python.index("Java")) #원하는 값이 없으면 오류를 반환

print("hi")
print(python.count("n")) #해당하는게 몇번이나 나왔는지 카운트