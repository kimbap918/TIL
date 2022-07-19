## OOP(Object Oriented Programming)

> 파이썬은 모든것이 객체(Object)다.

<br>

#### 객체가 뭘까?

**클래스에서 정의한 것을 토대로 메모리(실제 저장공간)에 할당된것** 으로 프로그램에서 사용되는 데이터 또는 식별자에 의해 참조되는 공간을 의미하며, 변수, 자료구조, 함수 또는 메소드가 될수있다.

<br>

#### 그렇다면 객체 지향 프로그래밍은?

컴퓨터 패러다임 중 하나, OOP는 컴퓨터 **프로그램을 명령어의 목록으로 보는 시각에서 벗어나** 여러개의 독립된 단위, 즉 "객체"들의 모임으로 파악하고자 하는 것이다. 각각의 객체는 메세지를 주고받고, 데이터를 처리할수 있다.

<br>

#### 파이썬은?

파이썬은 모든 것이 객체다(object)

위의 말처럼 각각의 객체는 **메세지를 주고받고**, **데이터를 처리한다.**

즉, 어떠한 대상이 정보를 가지고있고 동작할 수 있도록 하고있다.

아래의 코드를 보자.

 ``` python
 # 복소수.실수
 (3+4j).real
 ```

이건 복소수(complex) 타입이 가지고 있는 실제 값의 어떠한 정보다.

또한 어떠한 행위를 담당하는것도 있다.

<br>

``` python
# 리스트.정렬()
[3, 2, 1].sort()
# 리스트가. 정렬한다
```

<br>

타입(종류)과 값, 행동(실제 사례)의 주어와(S) 동사 형태(V)로 이뤄진것들이 모두 객체 지향 프로그래밍이다.

<br>

## 객체지향 프로그래밍

> 객체(object)는 특정 타입(class)의 인스턴스(instance)이다.

123, 900, 5는 모두 int의 인스턴스

'hello', 'bye'는 모두 string의 인스턴스

[1, 2, 3]은 모두 list의 인스턴스

#### 객체의 특징

* 타입 : 어떤 연산자와 조작이 가능한가?

  ``` python
  # 연산자(operater)
  ==, >=, <= ...
  # 조작
  'a'.upper() # upper
  a.append() # append
  ```

* 속성 : 어떤 상태를 가지는가?

* 조작법 : 어떤 행위를 할 수 있는가?

#### 객체지향 프로그래밍이란?

* 프로그램을 여러 개의 독립된 객체들과 그 객체들 간의 상호작용으로 파악하는 프로그래밍 방법

* 데이터와 기능(메소드) 분리, 추상화된 구조(인터페이스)

  ``` python
  word_list = ['abc', 'banana', 'apple']
  
  def transform_uppercase(word):
    result = ''
    for char in word:
      number = ord(char)
      number = number -32
      result += char(number)
    return result
  
  for word in word_list:
    print(transform_uppercase(word))
    
  # 우리는 위와 같은 구조로 만든 
  transform_uppercase('abc') # 를
  # 객체 지향 프로그래밍으로 'abc'.uppper()로 쓸수있다.
  ```

* 현실 세계를 프로그램 설계에 반영(추상화)

  ``` python
  class Person:
    def __init__(self, name, gender):
      self.name = name
      self.gender = gender
      
    def greeting_message(self):
      return f'안녕하세요, {self.name}입니다.'
    
  jimin = Person('지민', '남')
  print(jimin.greeting_message())
  # 안녕하세요, 지민입니다.
  jieun = Person('지은', '여')
  print(jieun.greeting_message())
  # 안녕하세요, 지은입니다.
  
  # Person - 클래스(class)
  # jimin, jieun - 인스턴스(instance)
  # jimin, jieun의 정보('지민', '남') - 속성(attribute)
  # Person의 행동/기능(인사를 한다) - 메소드(method)
  
  # 클래스 : str, int, Person
  # 인스턴스 : '123', 'iu'
  # 객체 : 모든 것
  # 준혁은 Person 클래스의 하나의 인스턴스다.
  ```

  <br>

## OOP 기초

#### 기본 문법

``` python
# 클래스 정의
class MyClass: # class는 CamelCase로 작성한다.
  pass

# 인스턴스 생성
my_instance = MyClass() # 인스턴스는 snake_case로 작성한다.
# 메서드 호출
my_instance.my_method()
# 속성
my_instance.my_attribute
```

* 클래스 : 객체들의 분류
* 인스턴스 : 하나하나의 실체
* 속성 : 특정 데이터 타입/클래스의 객체들이 가지게 될 상태/데이터를 의미
* 메서드 : 특정 데이터 타입/클래스의 객체에 공통적으로 적용 가능한 행위(함수)

<br>

#### 객체 비교하기

* ==

  * 동등한(equal)
  * 변수가 참조하는 객체가 동등한 경우 True
  * 두 객체가 같아 보이지만 실제로 동일한 대상을 가리키고 있다고 확인해 준 것은 아님

* is

  * 동일한(identical)
  * 두 변수가 동일한 객체를 가리키는 경우 True

  ``` python
  a = [1, 2, 3] # 값은 같으나 주소가 다름
  b = [1, 2, 3]
  
  print(a == b, a is b)
  # True False
  
  a = [1, 2, 3]
  b = a
  
  print(a == b, a is b)
  # True True
  ```

<br>

#### 인스턴스

* 인스턴스 변수
  * 인스턴스가 개인적으로 가지고 있는 속성
  * 각 인스턴스들의 고유한 변수
* 생성자 메소드에서 self.<name>으로 정의
* 인스턴스가 생성된 이후<instance>.<name>으로 접근 및 할당

``` python
class Person:
  
  def __init__(self, name):
    self.name = name # 인스턴스 변수 정의
    
john = Person('John')
print(john.name) # 인스턴스 변수 접근 및 할당
```

<br>

#### 인스턴스 메서드

* 인스턴스 변수를 사용하거나, 인스턴스 변수에 값을 설정하는 메서드

* 클래스 내부에 정의되는 메서드의 기본

* 호출 시, 첫번째 인자로 인스턴스 자기자신(self)이 전달됨

  ``` python
  class MyClass:
    def instance_method(self, arg1...)
  ```

  **self** 

  * 인스턴스 자기자신
  * 파이썬에서 인스턴스 메소드는 호출 시 첫번째 인자로 인스턴스 자신이 전달되게 설계
    * 매개변수 이름으로 self를 첫번째 인자로 정의 
    * 다른 단어로 사용이 가능하지만, 파이썬의 암묵적 규칙

<br>

#### 생성자(constructor) 메서드

* 인스턴스 객체가 생성될 때 자동으로 생성되는 메서드

* 인스턴스 변수들의 초기값을 설정

  * 인스턴스 생성
  * `__init__` 메소드 자동 호출

  ``` python
  class Person:
    # 생성자, 인스턴스가 생성될때 어떠한 작업
    def __init__(self, name):
      print('응애!')
      # 그 인스턴스의 이름을 name으로 해주세요
      self.name = name
      
  # Person 클래스의 인스턴스인 iu를 생성
  iu = Person('아이유')
  print(iu.name)
  jimin = Person('지민')
  print(jimin.name)
  ```

<br>

#### 소멸자(destructor) 메서드

* 인스턴스 객체가 소멸(파괴)되기 직전에 호출되는 메소드

``` python
class Person:
  def __del__(self):
    print('인스턴스가 사라졌습니다.')
    
person1 = Person()
del person1
# 인스턴스가 사라졌습니다.
```



