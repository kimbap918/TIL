## 에러/예외처리

> "코드의 상태를 신중하게 출력해가며 심사숙고하는 것보다 효과적인 디버깅 도구는 없습니다." - 브라이언 커니핸, Unix for Beginners

<br>

## 🐜 디버깅

branches

* 모든 조건이 원하는대로 동작하는지

for loops

* 반복분에 진입하는지, 원하는 횟수만큼 실행되는지

while loops

* for loops와 동일, 종료조건이 제대로 동작하는지

function

* 함수 호출시, 함수 파라미터, 함수결과가 바뀌면서 코드결과가 바뀌지 않는지

<br>

### 어떻게 접근해야할까?

* print 함수를 활용 

  * 특정 함수 결과, 반복/조건 결과 등을 나눠서 생각하고 코드를 bisection으로 나눠서 생각하자.

    ``` python
    import sys
    T = int(input())
    
    for i in range(T):
        # 높이(H), 너비(W), 몇번째 손님(N)
        H, W, N = map(int, sys.stdin.readline().split())
        ho = N//H+1 # 어? 이 부분 값이 잘 출력되나?
        floor = N % H 
    	  # print(ho)
        if N % H == 0: 
            ho = N//H 
            floor = H  
        print(floor*100+ho) 
    ```

    

* 개발환경(Text Editor, IDE) 등에서 제공하는 기능 활용

  * breakpoint, 변수 조회

    ![스크린샷 2022-07-18 오전 10.31.06](python 에러:예외처리.assets/python3.png)

* Python tutor 활용 (단순 파이썬 코드인 경우)

* 뇌컴파일, 눈디버깅

<br>

## 문법 에러(Syntax Error)

* 문법에러가 발생하면 파이썬 프로그램은 **실행이 되지 않는다.**

* 파일이름, 줄번호, ^문자를 통해 파이썬이 코드를 읽어나 나갈 때 문제가 발생한 위치를 표현해줌

* 줄에서 에러가 감지된 가장 앞의 위치를 가리키는 캐럿(caret) 기호를(^) 표시

  ``` python
  2회차/최준혁 - (master) > python3 -u "/Users/mac/Desktop/TIL/KDT-py
  thon/0718_1.py"
    File "/Users/mac/Desktop/TIL/KDT-python/0718_1.py", line 1
      True = 3
      ^
  SyntaxError: cannot assign to True
  ```

  * EOL(End of Line)
  * EOF(End of File)
  * invalid syntax
  * assign to literal(값 그 자체에 할당을 할 수 없음)

<br>

## 예외(Exception)

* 실행 도중 예상치 못한 상황을 맞이하면, 프로그램 실행을 멈춤
  * 문장이나 표현식이 문법적으로 올바르더라도 발생하는 에러
* 실행 중에 감지되는 에러들을 예외라 부른다
* 예외는 여러 타입으로 나타나고, 타입이 메시지의 일부로 출력된다
  * NameError, TypeError 등은 발생한 예외 타입의 종류
* 모든 내장 예외는 Exception Class를 상속 받아서 이뤄진다
* 사용자 정의 예외를 만들어 관리할 수 있음

#### 예외의 종류

* ZeroDivisionError : 0으로 나눌 경우 

  ``` python
  10/0
  
    File "/Users/mac/Desktop/TIL/KDT-python/0718_1.py", line 1, in <module>
      10/0
  ZeroDivisionError: division by zero
  ```

* NameError : namespace 상에 이름이 없는 경우

  ``` python
  print(name_error)
  
    File "/Users/mac/Desktop/TIL/KDT-python/0718_1.py", line 1, in <module>
      print(name_error)
  NameError: name 'name_error' is not defined
  ```

  <br>

#### 타입 불일치(TypeError)

``` python
# int와 str을 더함
		1 + '1'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
# str을 반올림    
    round('3.5')
TypeError: type str doesn't define __round__ method
# 0개의 인자를 넣는경우
    divmod()
TypeError: divmod expected 2 arguments, got 0
# 인자 개수 초과
    divmod(1, 2, 3)
TypeError: divmod expected 2 arguments, got 3
```

<br>

#### 타입은 올바르나 값이 적절하지 않거나 없는경우(ValueError)

``` python

		int('3.5')
ValueError: invalid literal for int() with base 10: '3.5'
    
    range(3).index(6)
ValueError: 6 is not in range
```

<br>

#### indexError

``` python
    empty_list[2]
IndexError: list index out of range
```

<br>

#### KeyError

``` python
    song ['BTS']
KeyError: 'BTS'
```

<br>

#### 존재하지 않는 모듈을 import 하는 경우(ModuleNotFoundError)

``` python
    import nonamed
ModuleNotFoundError: No module named 'nonamed'
```

<br>

#### 모듈은 있으나 존재하지 않는 클래스/함수를 가져오는 경우(importError)

``` python
    from random import samp
ImportError: cannot import name 'samp' from 'random' (/Users/mac/.pyenv/versions/3.9.13/lib/python3.9/random.py)
```

<br>

#### 들여쓰기가 적절하지 않은 경우(IndentationError) 

``` python
    print(i)
    ^
IndentationError: expected an indented block
```

<br>

#### 임의로 프로그램을 종료하였을때(KeyboardInterrupt)

``` python
while True:
  continue
# 임의로 종료함  
KeyboardInterrupt :
```

<br>

## 예외처리

* try / except을 이용하여 예외 처리를 할 수 있음
* try문
  * 오류가 발생할 가능성이 있는 코드를 실행
* except문
  * 예외가 발생하면, except 절이 실행
  * 예외 상황을 처리하는 코드를 받아서 적절한 조취를 취한다
* finally
  * 예외 발생 여부와 관계없이 항상 실행함

``` python
# 숫자 입력을 받아서 출력
numbers = input('숫자를 입력해주세요:')

try:
  print(100/int(number))
except ZeroDivisionError as err: # 각각 예외처리를 할수있음
  print(err) # as err -> print(err) 파이썬에서 실제로 출력되는 에러를 출력할수 있음
  print('0으로 나눌 수는 없습니다.')
except ValueError:
  print('숫자 형식을 입력해주세요.')
except Exception: 
  print('오류')
finally: # 예외 여부와 관계없이 항상 실행
  print('입력을 종료합니다.')
```

<br>

#### 조건문과 예외처리의 차이?

조건문은 어떠한 상황에서 분기점을 만들어 코드를 처리하는것.

예외처리는 에러 대신에 무언가를 처리하는. 다른 메서드를 실행하거나, 코드를 실행하게 하는 것. 

<br>

#### 예외 발생시키기(raise)

* 라이브러리 등의 내부에서 에러라는것을 알려주기위해 의도적으로 발생시키는것 

``` python
a = 1

raise Exception

---------출력----------
		raise Exception
Exception
```

