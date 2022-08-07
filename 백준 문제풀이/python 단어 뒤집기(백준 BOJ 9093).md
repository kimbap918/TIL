## 파이썬 단어 뒤집기(백준 BOJ 9093)

<br>

## 문제

문장이 주어졌을 때, 단어를 모두 뒤집어서 출력하는 프로그램을 작성하시오. 단, 단어의 순서는 바꿀 수 없다. 단어는 영어 알파벳으로만 이루어져 있다.

<br>

## 입력

첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있으며, 문장이 하나 주어진다. 단어의 길이는 최대 20, 문장의 길이는 최대 1000이다. 단어와 단어 사이에는 공백이 하나 있다.

<br>

## 출력

각 테스트 케이스에 대해서, 입력으로 주어진 문장의 단어를 모두 뒤집어 출력한다.

<br>

## 예제 입력 1

```
2
I am happy today
We want to win the first prize
```

## 예제 출력 1

```
I ma yppah yadot
eW tnaw ot niw eht tsrif ezirp
```

<br>

## 📝 풀어보기

문제를 너무 복잡하게 생각한것같다.

📌 테스트 케이스를 입력받고 리스트 하나를 생성한다.

테스트 케이스가 반복하는동안 뒤집을 단어를 입력받는다.

``` python
T = int(input())
a = []
for _ in range(T):
    S = input()
```

<br>

📌  입력받은 S의 역순으로 리스트에 저장하고 a를 공백문자별로 각 단어를 붙힌뒤에 split으로 나눈다. a는 한번 초기화하고 s1의 역순으로 우측공백을 없애고 단어의 끝마다 공백을 줘서 출력한다.  

``` python
    for i in range(len(S)-1, -1, -1):
       a.append(S[i])
    s = ''.join(a)
    s1 = list(s.split())
    a = []
    for j in range(len(s1)-1, -1, -1):
        print(s1[j].rstrip(), end = ' ')
```

<br>

#### 전체코드

``` python
T = int(input())
a = []
for _ in range(T):
    S = input()

    for i in range(len(S)-1, -1, -1):
       a.append(S[i])
    s = ''.join(a)
    s1 = list(s.split())
    a = []
    for j in range(len(s1)-1, -1, -1):
        print(s1[j].rstrip(), end = ' ')

# 수정코드 
for i in range(T):
    string = list(input().split())
    for j in string:
        print(j[::-1], end = ' ')
```

