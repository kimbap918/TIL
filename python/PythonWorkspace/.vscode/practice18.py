# 집합(set)
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

#교집합 -> 자바와 파이썬을 모두 할수있는
print(java & python)
print(java.intersection(python))

#합집합 -> 자바나 파이썬을 할수있는
print(java | python)
print(java.union(python))

#차집합 -> 자바를 할수있지만 파이썬을 할수없는
print(java - python)
print(java.difference(python))

# python을 할수있는 사람 추가
python.add("김태호")
print(python)

# java를 까먹음
java.remove("김태호")
print(java)