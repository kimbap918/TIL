## 📦 함수(function)

* 특정한 기능을 하는 코드의 조각

* 특정 명령을 수행하는 코드를 매번 다시 작성하지 않고, 필요 시에만 호출하여 간편히 사용

  <br>

## 🤔 왜 우리는 함수를 사용할까?

* Decomposition : 기능을 분해해서 재사용 가능

  ``` python
  # 코드
  numbers = [1, 10, 100]
  result = 0
  cnt = 0
  for number in numbers:
    result += number # 합을 구하는 기능
    cnt += 1 # 카운트 기능
  print(result/cnt)
  
  # 함수
  print(sum(numbers)/len(numbers)) # 함수로 분리해서 활용, 그 결과 편해지고 간결해짐
  ```

* Abstraction : 복잡한 내용을 숨기고, 기능에 집중하여 사용할 수 있음.(블랙박스) 재사용성, 가독성, 생산성

  ``` python
  print('happy!')
  # 우리가 출력을 함수 없이 구현하려면 얼마나 복잡할까?
  ```

<br>

## 함수의 정의

* 특정한 기능을 하는 코드의 조각

* 특정 명령을 수행하는 코드를 매번 다시 작성하지 않고, 필요 시에만 호출하여 간편히 사용

* 사용자 함수(Custom Function)

  * 구현되어 있는 함수가 없는 경우, 사용자가 직접 함수를 작성 가능하다.

    ``` python
    def add(a, b): # a, b를 더하는 함수를 선언
      return a+b
    
    add(5, 10) # 사용
    ```

<br>

#### 📌 함수의 기본 구조

* 선언과 호출(define & call)
* 입력(Input)
* 범위(Scope)
* 결과값(Output)

<br>

#### 📌 선언과 호출(define & call)

* 선언은 def 키워드를 활용한다.
* 들여쓰기를 통해 Function body(실행될 코드 블록)를 작성
* 함수는 파라미터를 넘겨줄 수 있음
* 함수는 동작 후에 return을 통해 결과값을 전달함

``` python
def foo(): # 함수의 선언
  return True
foo() # 함수의 호출

def add(x,y):
  return x + y
add(2,3) # 5
```

<br>

#### 📌 예시

``` python
num1 = 0
num2 = 1

def func1(a, b): # 3. 0 + 5 = 5
  return a + b

def func2(a, b): # 4. 5 - 1 = 4
  return a - b

def func3(a, b): # 2. 호출되는 함수 확인
  return func1(a, 5) + func2(5, b) # 5. 5 + 4 = 9

result = func3(num1, num2) # 1. 호출
print(result) # 6. 9
```

<br>

#### 📌 함수의 결과값(output)

#### return

* 함수는 반드시 값을 하나만 return한다.
  * 명시적 return이 없는 경우에도 None을 반환한다.
* 함수는 return과 동시에 실행이 종료된다.

``` python
def minus_and_product(x,y):
  return x - y
	return x * y
# x - y 만 실행이 되고 함수는 종료된다.

def minus_and_product(x,y):
  return x - y, x * y

minus_and_product(4, 5)
# -> (-1, 20) 튜플 반환이 됨
```

<br>

#### 📌 함수의 입력(Input)

* Parameter : 함수를 실행할 때, 함수 내부에서 사용되는 식별자
* Argument : 함수를 호출 할 때, 넣어주는 값
  * 필수 Argument : 반드시 전달되어야 하는 argument
  * 선택 Argument : 값을 전달하지 않아도 되는 경우는 기본 값이 전달

``` python
def function(ham): # parameter : ham
  return ham

function('spam') # argument : spam
```

<br>

#### 📌 Argument

* positional arguments

  * 기본적으로 함수 호출 시 Argument는 위치에 따라 함수 내에 전달됨

    ``` python
    def add(x, y):
      return x + y
    
    add(2, 3)# 2의 위치 x, 3의 위치 y
    ```

* keyword arguments

  * 직접 변수의 이름으로 특정 Argument를 전달할 수 있음

  * Keyword Argument 다음에 Positional Argument를 활용할 수 없음

    ``` python
    def add(x, y):
      return x + y
    
    add(x=2, y=5)
    add(2, y=5)
    ```

* default arguments values

  * 기본값을 지정하여 함수 호출 시 argument 값을 설정하지 않도록 함

  * 정의된 것 보다 더 적은 개수의 argument들로 호출될 수 있음

    ``` python
    def add(x, y=0):
      return x + y
    
    add(2)
    ```

* 정해지지 않은 개수의 arguments

  * 여러개의 Positional Argument를 하나의 필수 parameter로 받아서 사용

  * 몇 개의 Positional Argument를 받을지 모르는 함수를 정의할 때 유용

    ``` python
    def add(*args):
      for args in args:
        print(arg)
        
    add(2)
    add(2, 3, 4, 5) # 이 경우 타입이 tuple로 나옴
    ```

* 정해지지 않은 개수의 keyword arguments

  * 함수가 임의의 개수 Argument를 Keyword Argument로 호출될 수 있도록 지정

  * Argument들은 딕셔너리로 묶여 처리되며, parameter에 **를 붙여 표현한다.

    ``` python
    def family(**kwargs):
      for key, value in kwargs:
        print(key, ":", value)
        
    family(father='John', mother='Jane', me='Jone Jr.')
    ```

<br>

#### 📌 함수의 범위(scope)

* 함수는 코드 내부에 local scope를 생성하며, 그 외의 공간인 global scope로 구분한다.

* scope

  * global scope : 코드 어디에서든 참조할 수 있는 공간
  * local scope : 함수가 만든 scope. 함수 내부에서만 참조 가능

* variable

  * global variable : global scope 내부에 정의된 변수

  * local variable : local scope 내부에 정의된 변수

    ``` python
    def func(): 
      a = 20
      print('local', a)# local scope
      
    func() 
    print('global', a) # global scope
    # NameError : name 'a' is not defined
    ```

<br>

#### 📌 객체 수명주기

* 객체는 각자의 수명주기가 존재
  * built-in scope `(print, sum, len..)`
    * 파이썬이 실행된 이후부터 영원히 유지됨
  * global scope `a=3`
    * 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
  * local scope `def ___ a = 1..`
    * 함수가 호출될 때 생성되고, 함수가 종료될 때 까지 유지

<br>

#### 📌 이름 검색 규칙(Name Resolution)

* 파이썬에서 사용되는 이름(식별자)들은 이름공간(namespace)에 저장되어 있음

* 아래와 같은 순서로 이름을 찾아나가며, LEGB Rule이라고 부름

  * Local scope : 함수
  * Enclosed scope : 특정 함수의 상위 함수
  * Global scope : 함수 밖의 변수, Import 모듈
  * Built-in scope : 파이썬 안에 내장되어 있는 함수 또는 속성

* 즉, 함수 내에서는 바깥 Scope의 변수에 접근 가능하나 수정 할 수 없음

  ``` python
  print(sum)
  print(sum(range(2)))
  sum = 5
  print(sum)
  print(sum(range(2)))
  # TypeError TraceBack(most recent call last)
  # 3 sum = 5
  # 4 print(sum)---->
  # 5 print(sum(range(2)))
  # TypeError: 'int' object is not callable
  ```

<br>

## 함수의 응용

#### 📌 map

* 순회 가능한 데이터구조(iterable)의 모든 요소에 함수 적용하고, 그 결과를 map object로 반환

  ``` python
  numbers = ['1', '2', '3']
  new_numbers_2 = map(int, numbers)
  print(list(new_numbers))#[1, 2, 3]
  
  n, m = map(int, input().split())
  # int
  # input() = 타입 : String(문자열)
  # split() = 타입 : list(리스트)
  # input().split = 타입 : list
  # map = 어떤 함수를 반복가능한 것들의 요소에 모두 적용
  # int 함수를 input().split() 리스트의 모든 요소에 적용한 결과 => map object n, m = [10, 20]
  
  def plus10(n):
    return n + 10
  
  numbers = [10, 20, 30]
  new_numbers = list(map(plus10, numbers))
  print(new_numbers)
  #[20, 30, 40]
  ```

  

