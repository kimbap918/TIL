## 객체지향프로그래밍(2) - 클래스



#### 클래스 속성(attribute)

* 한 클래스의 모든 인스턴스라도 똑같은 값을 가지고 있는 속성

* 클래스 선언 내부에서 정의

* <classname>.<name>으로 접근 및 할당

  ``` python
  class Circle:
    pi = 3.14
    
  c1 = Circle() # 인스턴스
  c2 = Circle()
  
  print(Circle.pi)
  print(c1.pi)
  print(c2.pi)
  # 3.14
  # 3.14
  # 3.14
  ```

  <br>

#### 인스턴스와 클래스 간의 이름 공간(namespace)

* 클래스를 정의하면, 클래스와 해당하는 이름 공간 생성
* 인스턴스를 말하면, 인스턴스 객체가 생성되고 이름 공간 생성
* 인스턴스에서 특정 속성에 접근하면, 인스턴스-클래스 순으로 탐색

``` python
class Person:
  species  = 'human' 
  
  def __init__(self, name):
    self.name = name
    
p1 = Person('Hong') # 인스턴스
p2 = Person('Choi')
```

<br>

#### 클래스 메서드

* 클래스가 사용할 메서드

* @classmethod 데코레이터를 사용하여 정의

  * 데코레이터 : 함수를 어떤 함수로 꾸며서 새로운 기능을 부여

* 호출 시, 첫번째 인자로 클래스(cls)가 전달됨

  ``` python
  class MyClass:
    
    @classmethod
    def class_method(cls, arg1, ...)
  ```

#### 스태틱 메서드

* 인스턴스 변수, 클래스 변수를 전혀 다루지 않는 메서드

**언제 사용하는가?**

* 속성을 다루지 않고 단지 기능(행동)만을 하는 메서드를 정의할때 사용

* @staticmethod 데코레이터를 사용하여 정의

* 호출 시, 어떠한 인자도 전달되지 않음(클래스 정보에 접근/수정 불가)

  ``` python
  class MyClass:
    
    @staticmethod
    def class method(arg1, ...)
  ```

  ``` python
  class MyClass:
    class_variable = '클래스 변수'
    
    # 메서드를 정의했습니다.
   
    def __init__(self):
      self.instance_variable = '인스턴스 변수'
    # 인스턴스 메서드
    def instance_method(self):
      return self
    # 클래스 메서드 정의
    @classmethod # 데코레이터 : 함수를 꾸며주는 것
    def class_method(cls):
      return cls
    # 스태틱 메서드 정의
    @staticmethod
    def static_method():
      return '스태틱'
  
  c1 = MyClass()
  print('인스턴스 변수 호출', c1.instance_variable)
  print('인스턴스 메서드 호출', c1.instance_method())
  print('클래스 메서드 호출', c1.class_method())
  print('스태틱 메서드 호출', c1.static_method())
  
  # 인스턴스 변수 호출 인스턴스 변수
  # 인스턴스 메서드 호출 <__main__.MyClass object at 0x10e076d90> -> 아무것도 넣지 않았는데 self, 인스턴스 그 자신이 넘어옴
  # 클래스 메서드 호출 <class '__main__.MyClass'> -> 아무것도 넘겨주지 않았는데 cls 그 자체가 넘어옴
  # 스태틱 메서드 호출 
  
  # 인스턴스 메서드 -> 인스턴스가 호출하면서 메서드 내부에 인스턴스 그 자체가 필요한 경우 사용
  # 클래스 메서드 -> 클래스가 호출하는데 내부적으로 메서드 내부에 클래스가 필요한 경우 사용
  # 스태틱 메서드 -> 내부적으로 클래스, 인스턴스 모두 필요없을때 사용, 스태틱 메서드 안에서는 클래스나 인스턴스를 전혀 사용할수 없음.
  ```

<br>

#### 정리

* 클래스 구현
  * 클래스 정의
  * 데이터 속성 정의(객체의 정보는 무엇인지)
  * 메서드 정의(객체를 어떻게 사용할 것인지)
* 클래스 활용
  * 해당 객체 타입의 인스턴스 생성 및 조작

#### 메서드 정리

* 인스턴스 메서드
  * 호출한 인스턴스를 의미하는 self 매개변수를 통해 인스턴스를 조작
* 클래스 메서드
  * 클래스를 의미하는 cls 매개 변수를 통해 클래스를 조작
* 스태틱 메서드
  * 인스턴스나 클래스를 의미하는 매개변수는 사용하지 않음
    * 즉, 객체 상태나 클래스 상태를 수정할 수 없음
  * 일반 함수처럼 동작하지만 클래스의 이름공간에 귀속 됨
    * 주로 해당 클래스로 한정하는 용도로 사용

<br>

## 객체지향의 핵심개념

#### 객체지향의 핵심 4가지

* 추상화 
* 상속 
* 다형성
* 캡슐화

<br>

### 추상화

*  클래스 사용과 구현을 분리하는 것
* 클래스의 구현을 사용자로 부터 숨기는것을 의미

### 상속

* 두 클래스 사이 부모 - 자식 관계를 정립하는 것
* 클래스는 상속이 가능
  * 모든 파이썬 클래스는 object를 상속
* 하위 클래스는 상위 클래스에 정의된 속성, 행동, 관계 및 제약 조건을 모두 상속 받음
* 부모클래스의 속성, 메소드가 자식 클래스에 상속되므로, 코드 재사용성이 높아짐

``` python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
class Professor(Person): # Person 상속
  def __init__(self, name, age, department):
    self.name = name
    self.age = age
    self.department = department
```

#### 정리

* 파이썬의 모든 클래스는 object로 부터 상속됨
* 부모 클래스의 모든 요소(속성, 메서드)가 상속됨
* super()를 통해 부모 클래스의 요소를 호출할 수 있음
* 메서드 오버라이팅을 통해 자식 클래스에서 재정의 가능
  * 오버라이딩 : 메서드를 덮어쓰기해서 재정의 하는것
* 상속관계에서의 이름 공간은 인스턴스, 자식 클래스, 부모 클래스 순으로 탐색

#### 다중 상속

* 두개 이상의 클래스를 상속 받는 경우
* 상속 받은 모든 클래스의 요소를 활용 가능함
* 중복된 속성이나 메서드가 있는 경우 상속 순서에 의해 결정됨

<br>

### 다형성(Polymorphism)

* 여러 모양을 뜻함
* 동일한 메소드가 클래스에 따라 다르게 행동할 수 있음을 의미
* 서로 다른 클래스에 속해있는 객체들이 **동일한 메시지에 대해 다른 방식으로 응답될 수 있음**

#### 메서드 오버라이딩

* 상속 받은 메서드를 재정의
* 클래스 상속 시, 부모 클래스에서 정의한 메서드를 자식 클래스에서 변경
* 부모 클래스의 메서드 이름과 기본 기능은 그대로 사용하지만, 특정 기능을 바꾸고 싶을 때 사용

``` python
class Person:
  def __init__(self, name):
    self.name = name
	
  def talk(self):
    print(f'반갑습니다. {self.name}입니다.')
# 자식 클래스 - Professor   
class Professor(Person): # Person 상속
    def talk(self):
    print(f'{self.name}일세.')
    
# 자식 클래스 - Student  
class Student(Person): # Person 상속
    super().talk()
    print(f'저는 학생입니다..')
    
p1 = Professor('김교수')
p1.talk
s1 = Student('이학생')
s1.talk
```

<br>

### 캡슐화

* 객체의 일부 구현 내용에 대해 외부로부터 직접적인 액세스를 차단

* 파이썬에서는 기능상으로 존재하지 않지만, 관용적으로 사용되는 표현이 있음

  #### 접근제어자 종류

  * Public : 어디서나 호출이 가능
  * Protected : 부모/자식 클래스에서만 호출이 가능
  * Private : 본인(클래스 그 자체)에서만 호출이 가능

