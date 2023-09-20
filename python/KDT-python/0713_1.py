# 정의
# 1. def
# 2. add : 함수의 이름
# 3. Input : a, b
def add(a, b):
    # 4. return : 값을 반환
    return a + b
# 호출
add(5, 10)

def minus(a, b):
    return a - b

minus(10, 5)

# 내장 함수 호출
print(sum([1, 2, 3]))

def no():
    a = 1

result = no() # None <class 'None Type'>

# print 함수는
# 출력을 해주고, return 값은 없다.(None)
a = print('hi')
print(a, type(a)) # None <class 'None Type'>


# 정해지지 않은 개수의 인자
def my_add(*numbers):
    # 내부적으로 numbers가 tuple
    return numbers

result = my_add(1, 2, 3)
print(result, type(result))

def family(**kwargs):
  for key, value in kwargs:
    print(key, ":", value)

# 'father': 'John', 'mother': 'Jane', 'me': 'Jone Jr.'    
family(father='John', mother='Jane', me='Jone Jr.')
