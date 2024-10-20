


### 정규 표현식이란?
* 정규표현식(Regular Expression)은 텍스트에서 특정 패턴을 찾고, 그 패턴에 맞는 문자열을 검색하거나 치환하는 도구



<br>



### 왜 사용될까?
1. **데이터 다듬기**: 데이터 분석을 위해 크롤링한 데이터는 종종 원하는 형태가 아니기 때문에, 정규표현식을 사용해 데이터를 정제하고 필요한 정보만을 추출 해야한다.
2. **정보 추출**: 정제된 데이터에서 특정 패턴을 찾아내어 새로운 컬럼을 만들거나 원하는 정보를 추출할 수 있다. 예를 들어, 이메일 주소, 전화번호, 날짜 등을 정규표현식을 사용해 추출할 수 있다.
3. **패턴 매칭**: 텍스트 내에서 특정 패턴이 발생하는 경우를 찾아내거나, 특정 조건을 만족하는 문자열을 찾을 때 유용하다.



아래의 예시를 보자.

```python
import re

# 이메일이 포함된 문자
text = "Please contact us at email@example.com for more information or support@example.org for assistance."

# 정규표현식 사용
emails = re.findall(r'[A-Za-z0-9]+@[A-Za-z0-9]+\.[A-Za-z]{2,}', text)

# 추출
for email in emails:
    print(email)

```

```python
# 결과
email@example.com
support@example.org
```



<br>



### 메타 문자
원래 그 문자가 가진 뜻이 아니라 특별한 의미를 가진 문자, 정규표현식에 메타 문자를 사용하면  패턴 매칭 및 검색 시 사용된다. 
```no-highligt
. ^ $ * + ? { } [ ] \ | ( )
```
#### 1. `.` (점)
- **역할**: 줄바꿈 문자를 제외한 모든 문자와 매칭된다
- **예시**: 정규표현식 `a.c`는 a(문자)c의 패턴을 가진 3글자 단어를 추출하는 것으로, "abc", "a_c" 등의 단어를 추출한다.

#### 2. `^` (캐럿)
- **역할**: 문자열의 시작 부분과 매칭된다
- **예시**: 정규표현식 `^abc`는 "abc"로 시작하는 문자열과 매칭된다. 

```python
import re

# 문자열이 'abc'로 시작하는지 검사
pattern = r'^abc'

test_string1 = "abc123"
test_string2 = "123abc"

match1 = re.match(pattern, test_string1)
match2 = re.match(pattern, test_string2)

print(bool(match1))  # True: 'abc123'는 'abc'로 시작한다.
print(bool(match2))  # False: '123abc'는 'abc'로 시작하지 않는다.

```

### 3. `$` (달러 기호)
- **역할**: 문자열의 끝 부분과 매칭된다.
- **예시**: 정규표현식 `abc$`는 "abc"로 끝나는 문자열과 매칭된다. 

```python
import re

# 문자열이 'abc'로 끝나는지 검사
pattern = r'abc$'

test_string1 = "abc123"
test_string2 = "123abc"

match1 = re.search(pattern, test_string1)
match2 = re.search(pattern, test_string2)

print(bool(match1))  # False: 'abc123'는 'abc'로 끝나지 않는다.
print(bool(match2))  # True: '123abc'는 'abc'로 끝난다.

```



#### 4. `*` (별표)
- **역할**: 앞의 문자나 그룹이 0회 이상 반복되는 패턴을 매칭한다.
- **예시**: 정규표현식 `ab*c`는 "ac", "abc", "abbbc" 등을 추출한다.

#### 5. `+` (플러스)
- **역할**: 앞의 문자나 그룹이 1회 이상 반복되는 패턴을 매칭한다.
- **예시**: 정규표현식 `ab+c`는 "abc", "abbc", "abbbc" 등을 추출하지만, "ac"는 추출하지 못한다.(1회 이상 반복되야하기 때문)

#### 6. `?` (물음표)
- **역할**: 앞의 문자나 그룹이 0회 또는 1회 등장하는 패턴을 매칭한다 (존재 여부를 나타냄)
- **예시**: 정규표현식 `ab?c`는 "ac"와 "abc"를 추출한다. "asc"는 추출하지 못한다. 

#### 7. `{}` (중괄호)
- **역할**: 정확한 반복 횟수를 지정할 수 있는 패턴을 매칭한다.
- **예시**: 정규표현식 `a{3}`는 "aaa"를 매칭해서 추출하며, `a{2,4}`는 "aa", "aaa", "aaaa"를 매칭해서 추출한다.

#### 8. `[]` (대괄호)
- **역할**: 대괄호 안에 포함된 문자 중 하나와 매칭된다.
- **예시**: 정규표현식 `[abc]`는 "a", "b", "c" 중 하나와 매칭된다.
- 두 문자 사이에 하이픈(-)을 사용하면 두 문자 사이의 범위를 의미하며, `[a-z]`는 소문자 알파벳 중 하나와 매칭된다.
- `[]` 안에는 어떤 문자나 메타 문자도 사용할 수 있지만, 주의해야 할 메타 문자가 1가지 있다. 그것은 바로 `^`인데, `[]`안에 ^ 메타 문자를 사용할 경우에는 반대(not)라는 의미를 갖는다. 예를 들어 `[^0-9]`라는 정규 표현식은 숫자가 아닌 문자만 매칭된다.

#### 9. `\` (역슬래시)
- **역할**: 다음 문자의 특수한 의미를 없애거나 특수 문자를 이스케이프
- **예시**: 정규표현식 `\.`는 점 자체를 매칭하고, `\d`는 숫자를 매칭한다.

#### 10. `|` (파이프)
- **역할**: OR 연산자처럼 사용되어 두 개의 패턴 중 하나와 매칭된다.
- **예시**: 정규표현식 `cat|dog`는 "cat" 또는 "dog"와 매칭된다.

#### 11. `()` (괄호)
- **역할**: 그룹을 만들어 특정 부분을 묶거나 캡처할 때 사용된다.
- **예시**: 정규표현식 `(abc)+`는 "abc", "abcabc", "abcabcabc" 등과 매칭되며, `(ab|cd)`는 "ab" 또는 "cd"와 매칭된다.

```python
import re

# 주어진 문자열
words = "제 메일 주소는 fx887722@naver.com 입니다. reply 부탁드려요. 12345"

# 정규표현식 패턴
pattern = r'[A-Za-z0-9]+@[A-Za-z0-9]+\.[A-Za-z]{2,}'
# 패턴에 매칭된 모든 부분 추출
matches = re.findall(pattern, words)

# 각 매칭된 문자 출력
print(matches)
# ['fx887722@naver.com']
```

- `[A-Za-z0-9]+`: 알파벳 대문자(A-Z), 소문자(a-z), 숫자(0-9) 중 하나 이상 반복(+). 이메일 주소의 로컬 파트를 매칭한다. (예: `fx887722`).
- `@`: 이메일 주소의 구분자인 '@' 문자.
- `[A-Za-z0-9]+`: 알파벳 대문자(A-Z), 소문자(a-z), 숫자(0-9) 중 하나 이상 반복(+). 이메일 주소의 도메인 파트를 매칭한다 (예: `naver`).
- `\.`: 실제 점(.) 문자를 매칭한다.
- `[A-Za-z]{2,}`: 알파벳 대문자(A-Z)와 소문자(a-z)가 최소 2번 이상 반복되는 패턴({2, }). 최상위 도메인(예: `com`, `org`, `net` 등)을 매칭한다.

 

<br>



### 사전 정의된 문자 클래스(predefined character classes)
* 정규표현식에서 자주 사용되는 특별한 문자 집합을 나타내는 패턴
#### 1. **`\d`** - 숫자(digits):
* **역할**:  `[0-9]`와 동일하며, 모든 숫자와 매치된다.
- **예시**: 정규표현식 `a\dc`는 "a1c", "a2c", ..., "a9c"를 추출할수 있다.

#### 2. **`\D`** - 숫자가 아닌 것(non-digits):
* **역할**: `[^0-9](숫자가 아닌것)`와 동일하며, 숫자가 아닌 모든 문자와 매치된다.
- **예시**: 정규표현식 `a\Dc`는 "abc", "a#c", "a@c"와 매치되지만, "a2c"는 추출하지 못한다.
#### 3. **`\w`** - 단어(word characters):
* **역할**: `[a-zA-Z0-9_]`와 동일하며, 알파벳 소문자, 대문자, 숫자 및 밑줄(_)과 매치된다.
* **예시**: 정규표현식 `\w`는 "hello123", "username_1", "Python3"를 추출할수 있다.

#### 4. **`\W`** - 단어 문자가 아닌 것(non-word characters):
- **역할**: `[^a-zA-Z0-9_]`와 동일하며, 알파벳 소문자, 대문자, 숫자 및 밑줄(_)이 아닌 모든 문자와 매치된다.
- **예시**: 정규표현식 `\W`는 공백, 특수문자 등을 추출한다.

#### 5. **`\s`** - 공백 문자(whitespace):
- **역할**: `[ \t\n\r\f\v]`와 동일하며, 공백(space), 탭(tab), 개행 문자(newline), 캐리지 리턴(carriage return), 폼 피드(form feed), 수직 탭(vertical tab)과 매치된다.
- **예시**: 정규표현식 `a\sb`는 "`a b`", "`a\tb`", "`a\nb`"를 추출한다.

#### 6. **`\S`** - 공백 문자가 아닌 것(non-whitespace):
- **역할**: `[^\s]`와 동일하며, 공백 문자(space, tab 등)가 아닌 모든 문자와 매치된다.
* **예시**: 정규표현식 `\S+`는 "hello", "123", "Special@123"와 매치된다.

```python
import re

# 주어진 문자열
words = "제 메일 주소는 fx887722@naver.com 입니다. reply 부탁드려요. 12345"

# 정규표현식 패턴
pattern = r'[\w]+@[\w]+\.[\w]{2,}'
# 패턴에 매칭된 모든 부분 추출
matches = re.findall(pattern, words)

# 각 매칭된 문자 출력
print(matches)
```

- `[\w]+`: 알파벳 대문자, 소문자, 숫자(`\w`) 중 하나 이상 반복(+). 이메일 주소의 로컬 파트를 매칭한다. (예: `fx887722`).
- `@`: 이메일 주소의 구분자인 '@' 문자.
- `[\w]+`: 알파벳 대문자, 소문자, 숫자(`\w`) 중 하나 이상 반복(+). 이메일 주소의 도메인 파트를 매칭한다 (예: `naver`).
- `\.`: 실제 점(.) 문자를 매칭한다.
- `[\w]{2,}`: 알파벳 대문자(A-Z)와 소문자(a-z)가 최소 2번 이상 반복되는 패턴({2, }). 최상위 도메인(예: `com`, `org`, `net` 등)을 매칭한다.



<br>



### 정규표현식 관련 주요 함수 및 메서드

#### 1. re.search(pattern, string)

* **설명**: 문자열 전체에서 패턴과 일치하는 첫 번째 부분을 찾는다.
* **반환값**: 매칭된 객체를 반환하며, 매칭되지 않으면 'None'을 반환한다.

```python
import re
result = re.search(r'\d+', '123abc')
print(result.group())  # 출력: 123
```

#### 2. re.match(pattern, string)

- **설명**: 주어진 패턴이 문자열의 시작 부분과 일치하는지 검사한다. 
- **반환값**: 매칭된 객체를 반환한다. 매칭되지 않으면 `None`을 반환한다.

```python 
import re
result = re.match(r'\d+', '123abc')
print(result.group())  # 출력: 123
```



#### 3. re.findall(pattern, string)

- **설명**: 문자열 전체에서 패턴과 일치하는 모든 부분을 찾아 리스트로 반환한다.
- **반환값**: 매칭된 부분을 리스트 형태로 반환한다.

```python
result = re.findall(r'\d+', 'abc123def456ghi')
print(result)  # 출력: ['123', '456']
```

#### 4. re.sub(pattern, repl, string)

- **설명**: 문자열에서 패턴과 일치하는 부분을 다른 문자열로 치환한다.
- **반환값**: 치환된 문자열을 반환한다.

```python
result = re.sub(r'\d+', '#', 'abc123def456ghi')
print(result)  # 출력: abc#def#ghi, 연속된 숫자(\d+)가 #로 치환됨
```

#### 5. re.split(pattern, string)

- **설명**: 패턴과 일치하는 부분을 기준으로 문자열을 분할한다.
- **반환값**: 분할된 문자열의 리스트를 반환한다.

```python
result = re.split(r'\d+', 'abc123def456ghi')
print(result)  # 출력: ['abc', 'def', 'ghi'], 연속된 숫자(\d+) 기준으로 분할됨
```



