## 데이터 구조(Data Structure)

<br>

[1, 2, 3].append(4) -> 리스트.append(4) -> 타입.메서드()

이번 파트에서는 input과 output이 어떤지를 확인하는 것이 중요하다.

#### 예시

``` python
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
# S.V() -> 메서드
# sum() -> 함수
```

<br>

## 메서드(method)

* 시퀀스
  * 문자열(String) 
    * 문자열은 스스로 바뀌는  경우가 없다(immutable) 
    * 모두 바뀐 결과를 반환한다.
  * 리스트(List)
    * 변경 가능한 값들의 나열된 자료형
    * 순서를 가짐, 서로 다른 타입의 요소를 가짐
    * 변경 가능하며, 반복 가능함
    * 항상 대괄호 형태로 정의, 요소는 콤마로 구분
* 컬렉션
  * 세트(Set)
  * 딕셔너리(Dictionary) : 키와 값 쌍으로 이루어져 있음



### 📌 문자열 탐색/검증

s.find(x) : x의 첫 번째 위치를 반환. 없으면 -1을 반환한다.

``` python
'apple'.find('p')
# 1
'apple'.find('k')
# -1
```

<br>

s.index(x) : x의 첫 번째 위치를 반환. 없으면 오류 발생

``` python
'apple'.index('p')
# 1
'apple'.index('k')
# ValueError: substring not found 
```

<br>

문자열 관련 검증 메소드

``` python
'abc'.isalpha()
# 알파벳인지 -> True
'ab'.isupper()
# 대문자인지 -> False
'ab'.islower()
# 소문자인지 -> True
'Title Title'.istitle()
# 앞이 대문자인지 -> True
```

<br>

### 📌  문자열 변경

.replace(old, new[,count])

* 바꿀 대상 글자를 새로운 글자로 바꿔서 반환
* count를 지정하면, 해당 개수만큼만 시행

``` python
'coone'.replace('o', 'a')
# caane
'woowoo'.replace('o', '!', 2)
# w!!woo
```

<br>

.strip([chars])

* 특정한 문자들을 지정하면, 양쪽을 제거하거나(strip), 왼쪽을 제거하거나(lstrip), 오른쪽을 제거(rstrip)
* 문자열을 지정하지 않으면 공백을 제거

```python
'		와우!\n'.strip()
# '와우!'
'		와우!\n'.lstrip()
# '와우!\n'
'		와우!\n'.rstrip()
# '		와우!'
'안녕하세요???'.rstrip()
# '안녕하세요'
```

<br>

.split(sep=None, maxsplit=-1)

* 문자열을 특정한 단위로 나눠 **리스트로 반환**
  * sep이 None이거나 지정되지 않으면 연속된 공백문자를 단일한 공백문자로 간주, 선행/후행 공백은 빈 문자열에 포함시키지 않음.
  * maxsplit이 -1인 경우에는 제한이 없음.

``` python
'a, b, c'.split(' ')
# [a,b,c]
'a b c'.split()
# ['a', 'b', 'c']
```

<br>

' '.join([iterable])

* 반복가능한 컨테이너 요소들을 구분자로 합쳐 **문자열 반환**
  * iterable에 문자열이 아닌 값이 있으면 TypeError 발생

``` python
''.join(['3', '5'])
# 35

numbers = ' '.join([10, 20, 30]) # TypeError 에러
numbers = ' '.join(map(str, [10, 20, 30])) # 102030
```

<br>

### 📌 리스트

.append(x) : 리스트의 **마지막** 에 x값을 추가함

.extend(iterable) : 리스트에 iterable의 항목을 추가함

``` python
cafe = ['스타벅스', '탐앤탐스', '할리스']
# ['스타벅스', '탐앤탐스', '할리스']
cafe.append('바나프레소')
# ['스타벅스', '탐앤탐스', '할리스', '바나프레소']
cafe.extend(['카페베네', '테스트'])
# ['스타벅스', '탐앤탐스', '할리스', '바나프레소', '카페베네', '할리스'] 순차적으로 하나씩 들어감
```

<br>

.insert(i, x) : **인덱스 위치 i에 x 값을 추가**함

``` python
cafe = ['스타벅스', '탐앤탐스', '할리스']
cafe.insert(0, 'start')
['start', '스타벅스', '탐앤탐스', '할리스']
```

<br>

.remove(x) : 리스트에 값이 이  x인것 삭제

``` python
numbers = [1, 2, 3, 'hi']
numbers.remove('hi')
# [1, 2, 3]
```

<br>

.pop(i) 

* 정해진 위치 i에 있는 값을 삭제하고, 그 항목을 반환함
* i가 지정되지 않으면, **마지막 항목**을 삭제하고 반환

``` python
numbers = ['hi', 1, 2, 3]
# ['hi', 1, 2, 3]
pop_number = number.pop()
# 3
# ['hi', 1, 2]
pop_number = number.pop(0)
# [1, 2]
```

<br>

.clear() : 모든 항목을 삭제

``` python
numbers = [1, 2, 3]
numbers.clear()
# []
```

<br>

### 📌 리스트 탐색 및 정렬

.index(x) : x 값을 찾아 index 값을 반환

``` python
numbers = [1, 2, 3, 4]
print(numbers)
# [1, 2,3 ,4]
print(numbers.index(3))
# 2
print(numbers.index(100))
# ValueError : 100 is not in list
```

<br>

.count(x) : 원하는 값의 개수를 반환

``` python
numbers = [1, 2, 3, 1, 1]
numbers.count(1)
# 3
numbers.count(100)
# 0
```

<br>

.sort()

* **원본 리스트를 정렬**하고 **None 반환**
* sorted 함수와 비교할것

``` python
# .sort() 메서드
numbers = [3, 2, 5, 1]
result = numbers.sort()
print(numbers, result)
# [1, 2, 3, 5] None

# sorted() 함수
numbers = [3, 2, 5, 1]
result = sorted(numbers)
print(numbers, result)
# [3, 2, 5, 1][1, 2, 3 ,5]
```

<br>

.reverse() : 순서를 반대로 뒤집음(정렬되는 것이 아님). **None 반환.**

``` python
numbers = [3, 2, 5, 1]
result = numbers.revers()
print(numbers, result)
# [1, 5, 2, 3]
```

<br>

### 딕셔너리 

.get(key[,default])

* key를 통해 value를 가져옴
* keyError가 발생하지 않으며,
* default 값을 설정할 수 있음(기본:None)

``` python
my_dict = {'apple': '사과', 'banana': '바나나'}
my_dict['pineapple']
# keyError: 'pineapple'

print(my_dict.get('pineapple'))
# None
print(my_dict.get('apple'))
# 사과
print(my_dict.get('pineapple, 0'))
# 0
```

<br>

### 딕셔너리 추가 및 삭제

.pop(key[,default])

* key가 딕셔너리에 있으면 제거하고 해당 값을 반환
* 그렇지 않으면 default를 반환
* default 값이 없으면 keyError

``` python
my_dict = {'apple': '사과', 'banana': '바나나'}
my_dict.pop('apple')
# {'banana': 바나나}
my_dict.pop('pineapple')
print(data, my_dict)
# keyError : 'pineapple'
```

<br>

.update([other]) : 값을 제공하는 key, value로 덮어씀

``` python
my_dict = {'apple': '사', 'banana': '바나나'}
my_dict.update(apple='사과')
{'apple': '사과', 'banana': '바나나'}
```

<br>

