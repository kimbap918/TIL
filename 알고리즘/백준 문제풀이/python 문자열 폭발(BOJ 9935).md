

## 파이썬 문자열 폭발(BOJ 9935)

<br>

## 문제

상근이는 문자열에 폭발 문자열을 심어 놓았다. 폭발 문자열이 폭발하면 그 문자는 문자열에서 사라지며, 남은 문자열은 합쳐지게 된다.

폭발은 다음과 같은 과정으로 진행된다.

- 문자열이 폭발 문자열을 포함하고 있는 경우에, 모든 폭발 문자열이 폭발하게 된다. 남은 문자열을 순서대로 이어 붙여 새로운 문자열을 만든다.
- 새로 생긴 문자열에 폭발 문자열이 포함되어 있을 수도 있다.
- 폭발은 폭발 문자열이 문자열에 없을 때까지 계속된다.

상근이는 모든 폭발이 끝난 후에 어떤 문자열이 남는지 구해보려고 한다. 남아있는 문자가 없는 경우가 있다. 이때는 "FRULA"를 출력한다.

폭발 문자열은 같은 문자를 두 개 이상 포함하지 않는다.

<br>

## 입력

첫째 줄에 문자열이 주어진다. 문자열의 길이는 1보다 크거나 같고, 1,000,000보다 작거나 같다.

둘째 줄에 폭발 문자열이 주어진다. 길이는 1보다 크거나 같고, 36보다 작거나 같다.

두 문자열은 모두 알파벳 소문자와 대문자, 숫자 0, 1, ..., 9로만 이루어져 있다.

<br>

## 출력

첫째 줄에 모든 폭발이 끝난 후 남은 문자열을 출력한다.

<br>

## 예제 입력 1 

```
mirkovC4nizCC44
C4
```

## 예제 출력 1 

```
mirkovniz
```

## 예제 입력 2 

```
12ab112ab2ab
12ab
```

## 예제 출력 2 

```
FRULA
```

<br>

## 📝 풀어보기

빠른 입력을 위해 sys.stdin.readline을 사용한다.

원래 문자열 str1, 폭발할 키워드인 str2를 입력받는다.

빈 stack을 생성해두고 폭발할 키워드의 길이를 쓸 일이 많으므로 len(str2)를 저장해뒀다.

``` python
import sys
input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()
stack = []
length = len(str2)
```

<br>

원래 문자열 str1의 길이만큼 순회하면서 stack에 str의 글자를 1글자씩 담는다.

stack에 글자가 담길때마다 stack에 str2의 길이만큼 join한 글자가 str2와 같다면 stack에서 빼낸다.

``` python
for i in range(len(str1)):
    stack.append(str1[i])
    # print(stack)
    # str2의 길이만큼 
    
    if ''.join(stack[-length:]) == str2:
        # print(stack[-2:])
        for _ in range(length):
            stack.pop()


```

<br>

문자열이 남아있는 경우엔 스택의 값을 join해서 출력하고 값이 남아있지 않은 경우엔 "FRULA"를 출력한다.

``` python
if stack:
    print(''.join(stack))
else:
    print("FRULA")
```

<br>

#### 전체코드

``` python
import sys
input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()
stack = []
length = len(str2)

for i in range(len(str1)):
    stack.append(str1[i])
    # print(stack)
    # str2의 길이만큼 
    
    if ''.join(stack[-length:]) == str2:
        # print(stack[-2:])
        for _ in range(length):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print("FRULA")

```

