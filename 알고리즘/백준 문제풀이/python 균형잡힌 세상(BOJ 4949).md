## 파이썬 균형잡힌 세상(백준 BOJ 4949)

<br>

## 문제

세계는 균형이 잘 잡혀있어야 한다. 양과 음, 빛과 어둠 그리고 왼쪽 괄호와 오른쪽 괄호처럼 말이다.

정민이의 임무는 어떤 문자열이 주어졌을 때, 괄호들의 균형이 잘 맞춰져 있는지 판단하는 프로그램을 짜는 것이다.

문자열에 포함되는 괄호는 소괄호("()") 와 대괄호("[]")로 2종류이고, 문자열이 균형을 이루는 조건은 아래와 같다.

- 모든 왼쪽 소괄호("(")는 오른쪽 소괄호(")")와만 짝을 이뤄야 한다.
- 모든 왼쪽 대괄호("[")는 오른쪽 대괄호("]")와만 짝을 이뤄야 한다.
- 모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재한다.
- 모든 괄호들의 짝은 1:1 매칭만 가능하다. 즉, 괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다.
- 짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다.

정민이를 도와 문자열이 주어졌을 때 균형잡힌 문자열인지 아닌지를 판단해보자.

<br>

## 입력

하나 또는 여러줄에 걸쳐서 문자열이 주어진다. 각 문자열은 영문 알파벳, 공백, 소괄호("( )") 대괄호("[ ]")등으로 이루어져 있으며, 길이는 100글자보다 작거나 같다. 각 줄은 마침표(".")로 끝난다.

입력의 종료조건으로 맨 마지막에 점 하나(".")가 들어온다.

<br>

## 출력

각 줄마다 해당 문자열이 균형을 이루고 있으면 "yes"를, 아니면 "no"를 출력한다.

<br>

## 예제 입력 1

```
So when I die (the [first] I will see in (heaven) is a score list).
[ first in ] ( first out ).
Half Moon tonight (At least it is better than no Moon at all].
A rope may form )( a trail in a maze.
Help( I[m being held prisoner in a fortune cookie factory)].
([ (([( [ ] ) ( ) (( ))] )) ]).
 .
.
```

## 예제 출력 1

```
yes
yes
no
no
no
yes
yes
```

<br>

## 힌트

7번째의 " ."와 같이 괄호가 하나도 없는 경우도 균형잡힌 문자열로 간주할 수 있다.

<br>

## 📝 풀어보기 

📌 while을 무한반복 시키고 그 안에 입력을 받을 변수와 괄호를 넣고 빼며 균형 유무를 확인할 리스트를 생성한다.

``` python
while True:
    S = input()
    stack = []
```

<br>

📌 `.` 을 입력받을 시 종료가 될수있게 작성하고 반복문을 통해 입력받는 값 내에서 `(` 및 `[` 문자 유무를 확인한다.

문자가 있는 경우 `stack` 리스트에 삽입하고 문자가 `]` 인 경우 stack의 길이가 0이 아니고 stack의 마지막이 `[` 일때 스택의 값을 꺼낸다. 그외엔 stack에 `]`문자를 삽입하고 break한다.

``` python
    if S == ".":
        break

    for i in S:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == "]":
            if len(stack) != 0 and stack[-1] == "[":
                stack.pop()
            else:
                stack.append("]")
                break
```

<br>

📌 문자가 `)` 인 경우도 위의 elif문과 절차가 같다.

스택의 길이가 0 이되면 모든 값이 빠져나가 균형을 이룬것이므로 yes를 출력하고, 남아있는 경우엔 no를 출력한다.

``` python
				elif i == ")":
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(")")
                break
    if len(stack) == 0:
        print("yes")
    else:
        print("no")
```

<br>

#### 전체 코드

``` python

while True:
    S = input()
    stack = []

    if S == ".":
        break

    for i in S:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == "]":
            if len(stack) != 0 and stack[-1] == "[":
                stack.pop()
            else:
                stack.append("]")
                break
        elif i == ")":
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(")")
                break
    if len(stack) == 0:
        print("yes")
    else:
        print("no")
```

