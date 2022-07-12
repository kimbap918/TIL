## 제어문(Control Statement)

* 파이썬은 기본적으로 위에서부터 아래로 순차적으로 명령을 수행
* 특정 상황에 따라 코드를 선택적으로 실행(분기/조건) 하거나 계속 실행(반복) 하는 제어가 필요함
* 제어문은 순서도(flow chart)로 표현이 가능

<br>

## 조건문

조건문은 참/거짓을 판단할 수 있는 조건식과 함께 사용

#### 기본형식

* expression에는 참/거짓에 대한 조건식

  * 조건이 참인 경우 등여쓰기 되어있는 코드 블럭을 실행

  * 이외의 경우 else 이후 들여쓰기 되어있는 코드 블럭을 실행

    * else는 선택적으로 활용이 가능

      ``` python
      a = 10
      if a >= 0:
        print("양수")
      else:
        print("음수")
      ```

<br>

#### 복수 조건문

복수의 조건식을 활용할 경우 elif를 활용하여 표현함

* 복수 조건문

  ``` python
  dust = int(input())
  if dust >= 150:
      print("매우 나쁨")
  elif dust <= 150 and dust >= 81:
      print("나쁨")
  elif dust <= 80 and dust >= 31:
      print("보통")
  elif dust <= 30 and dust >= 0:
      print("좋음")  
  ```

  <br>

#### 중첩 조건문

조건문은 다른 조건문에 중첩되어 사용할 수 있음

* 들여쓰기를 유의하여 작성

``` python
dust = int(input())
if dust >= 150:
  if dust > 300:
    print('실외 활동을 자제하세요')
	print("매우 나쁨")
elif dust <= 150 and dust >= 81:
    print("나쁨")
elif dust <= 80 and dust >= 31:
    print("보통")
elif dust <= 30 and dust >= 0:
    print("좋음")
else:
    if dust < 0:
        print('음수값 입니다.')
    else:
        print('좋음')
```

<br>

#### 조건 표현식

``` python
value = num if num >= 0 else -num
# 참일결우	  # <expression> # 거짓일 경우

# 위 코드는 아래와 같다.
if num >= 0: # <expression>
  value = num # 참일경우
else:
  value = -num # 거짓일 경우
```

<br>

## 반복문

특정 조건을 도달할 때 까지, 계속 반복되는 문장

* while
  * 종료 조건에 해당하는 코드를 통해 반복문을 종료시켜야 함
* for
  * 반복가능한  객체를 모두 순회하면 종료

<br>

#### while

조건식이 참인 경우 반복적으로 코드를 실행

* 조건이 참인 경우 들여쓰기 되어 있는 코드 블록이 실행된다
* 코드 블록이 모두 실행되고, 다시 조건식을 검사하며 반복적으로 실행
* while문은 무한 루프를 하지 않도록 종료조건이 반드시 필요하다

``` python
a = 0
while a < 5:
  print(a)
  a += 1
print("끝")
```

<br>

#### for

for문은 시퀀스(string, tuple, list, range)를 포함한 순회 가능한 객체(iterable) 요소를 모두 순회한다.

* 처음부터 끝까지 모두 순회하므로 별도의 종료조건이 필요하지 않다.

``` python
for <변수명> in <iterable>:
  #code block
  
for fruit in ['apple', 'mango', 'banana']:
  print(fruit)
print('끝')
```

<br>

* 문자열(string) 순회

  ``` python
  chars = input()
  # hi
  
  for idx in range(len(chars)):
    print(chars[idx])
  # idx를 기준으로 순회를 한다.
  ```

* enumerate()

  * 인덱스와 객체를 쌍으로 담은 열거형(enumerate) 객체 반환

    * (index, value) 형태의 tuple로 구성된 열거 객체를 반환

      ``` python
      members = ['민수', '영희', '철수']
      
      for i in range(len(members)):
        print(f'{i} {members[i]}')
        
      for i, member in enumerate(members):
        print(i, member)
        
      enumerate(members)
      
      list(enumerate(members))
      # 리스트로 변환시 [(0, '민수'), (1, '영희'), (2, '철수')]로 인덱스 값과, 해당값을 나타내줌
      list(enumerate(members, start=1))
      # 리스트로 변환시 [(1, '민수'), (2, '영희'), (3, '철수')]
      ```

* 딕셔너리 순회

  * 딕셔너리는 기본적으로 key를 순회하며, key를 통해 값을 활용

  ``` python
  grades = {'john':80, 'eric':90}
  for name in grades:
    print(name)
  # john
  # eric
  grades = {'john':80, 'eric':90}
  for name in grades:
    print(name, grades[name])
  # john 80
  # eric 90
  ```

<br>

## 반복문 제어

* break
  * 반복문을 종료
* continue
  * continue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행
* for-else
  * 끝까지 반복문을 실행한 이후에 else문 실행
    * break를 통해 중간에 종료되는 경우 else문은 실행되지 않음

<br>

#### break

``` python
n = 0
while True:
  if n == 3:
    break
  print(n)
  n += 1
# 0
# 1
# 2
```

<br>

#### continue

continue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행

``` python
for i in range(6):
  if i % 2 == 0:
    continue
  print(i)
# 1
# 3
# 5
```

<br>

#### for-else

``` python
for char in 'apple':
  if char == 'b':
    print('b!')
    break
else:
  print('b가 없습니다.')
# b가 없습니다.
```

* 끝까지 반복문을 실행한 이후에 else문 실행

* break를 통해 중간에 종료되는 경우 else문은 실행되지 않음

<br>

