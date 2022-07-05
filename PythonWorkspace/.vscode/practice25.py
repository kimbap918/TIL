# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104

students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students] # student라는 리스트에 있는 i들을 하나씩 불러오면서 100을 더한것을 students에 다시 집어넣어라.
print(students)

# 학생 이름을 길이로 전환
students = ["Iron man", "Thor", "Groot"]
students = [len(i) for i in students] 
print(students)

# 학생 이름을 대문자로 전환
students = ["Iron man", "Thor", "Groot"]
students = [i.upper() for i in students]
print(students)

