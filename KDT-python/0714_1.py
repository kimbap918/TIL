# 리스트 메서드 활용
a = [10, 1, 100]
# 정렬(sort)
new_a = a.sort()
print(a, new_a)
# 결과 [1, 10, 100] -> None
# 리스트 메서드를 활용하면, 그 메서드를 정렬된 상태로 변경(원본 변경)


# 리스트 sorted 함수를 활용
b = [10, 1, 100]
# 정렬(sort)
new_b = sorted(b)
print(b, new_b)
# [10, 1, 100][1, 10, 100]
# sorted 함수를 활용하면, 원본을 변경하지 않음
# return되는 것은 정렬된 리스트
# 메서드와 함수는 다르다!

# 실제 활용 코드
a = [10, 1, 100]
a.sort()

b = [10, 1, 100]
b.sorted(b) # 차이가 보이나요?

numbers = ' '.join([10, 20, 30])
numbers = ' '.join(map(str, [10, 20, 30]))

# 기본 순회
my_dict = {'apple': '사과', 'banana': '바나나'}

for word in my_dict:
    print(word, my_dict[word])

# 다양한 방법 => 일종의 리스트!
print(my_dict.keys(), type(my_dict.keys()))

print(my_dict.value())

for value in my_dict.values():
    print(value)

print(my_dict.items())
for key, value in my_dict.items():
    print(key, value)
    # 일종의 리스트 안에, tuple