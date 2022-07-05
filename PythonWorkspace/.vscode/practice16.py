# 사전(dictionary)

cabinet = {3:"유재석", 100:"김태호"} # 중괄호, 키, 콜론, 값으로 구성 
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3))
#print(cabinet[5]) 오류발생
#print("hi") 출력이 되지않고 끝남
print(cabinet.get(5)) # none을 출력하고 오류가 나지않음
print("hi")
print(cabinet.get(5, "사용가능"))

print(3 in cabinet) # 사전 자료형 안에 값이 있는지 확인가능
print(5 in cabinet) # boolean 으로 반환

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-200"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 클리어
cabinet.clear()
print(cabinet)