## 파이썬 응용/심화

#### 추가 문법

**List Comprehension**

* 표현식과 제어문을 통해 특정한 값을 가진 리스트를 간결하게 생성하는 방법

``` python
# 1~3의 세제곱 결과가 담긴 리스트를 만드시오
cubic_list = []
for number in range(1, 4):
  cubic_list.append(number**3)
print(cubic_list)

# list comprehension
# 특정한 원소(요소)로 구성된 리스트를 만들 때 사용가능
[number**3 for number in range(1, 4)]
```

<br>

**Dictionary Comprehension**

``` python
# 1~3의 세제곱 결과가 담긴 딕셔너리를 만드시오
cubic dict = {}
for number in range(1, 4):
  cubic_dict[number] = number ** 3
print(cubic_dict)

# dictionary comprehension
# number(키)/number**3(값)
{number: number**3 for number in range(1,4)}
```

<br>

**lambda [parameter] : 표현식**

* 람다함수
  * 표현식을 계산한 결과값을 반환하는 함수, 이름이 없어서 익명함수로도 불림
* 특징
  * return문을 가질 수 없음
  * 간편 조건문 외 조건문이나 반복문을 가질 수 없음
* 장점
  * 함수를 정의해서 사용하는것보다 간결하게 사용가능
  * def를 사용할 수 없는곳에서도 사용가능

``` python
# map(함수, 반복가능한것)
# 반복 가능한 것들의 모든 요소에 함수를 적용시킨 결과를
# map object로 반환

# map(int, input().split())
# int 형 변환 함수를
# input으로 받은 것을 쪼갠 결과인 리스트에 각각 적용한다.

numbers = [1, 2, 5, 10, 3, 9, 12]
result = []
for number in numbers:
  if number % 3 == 0:
    result.append(number*3)
print(result)

# 만약에 map으로 쓰고싶다면?
# 함수를 정의해야한다.

def multiple_3(number):
  return number * 3

print(list(map(multiple_3, numbers)))

# 이 함수는 계속 사용되지 않고 map에서만 사용된다.
# 만약 임시적인 함수를 만들고싶다면? -> lambda
print(list(map(lambda n: n*3, numbers)))
# lambda(고정), n:(input), n*3(return)
```

<br>

**filter(함수, 반복가능한 객체)**

* 순회가능한 데이터구조의 모든 요소에 함수적용하고 그 결과가 True인 것들을 filter object로 반환

``` python
numbers = [1, 2, 5, 10, 3, 9, 12]
result = []
for number in numbers:
  if number % 3 == 0:
    result.append(number)
print(result)

print(list(filter(lambda n: n%3==0, number)))

# 이런 구문이 위의 filter로 변환되었다
def is_3(n):
  return n % 3 == 0

print(list(filter(is_3, numbers)))
```

<br>

**파이썬 버전별 업데이트**

언어는 버전에 따라서 계속 추가되거나 삭제되는것들이 있다.

최근에 추가되거나 변경된 문법들을 찾아서 익히는 능동적인 개발자가 될 수 있도록 하자.

https://docs.python.org/ko/3/