## 파이썬 단어정렬(백준 BOJ 1181)

<br>

## 문제

알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

1. 길이가 짧은 것부터
2. 길이가 같으면 사전 순으로

<br>

## 입력

첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 주어지는 문자열의 길이는 50을 넘지 않는다.

<br>

## 출력

조건에 따라 정렬하여 단어들을 출력한다. 단, 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력한다.

<br>

## 예제 입력 1

```
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours
```

## 예제 출력 1

```
i
im
it
no
but
more
wait
wont
yours
cannot
hesitate
```

<br>

## 📝 풀어보기

📌 입력받을 횟수 `N`을 만든다. 중복은 제거되어야하므로 `set`을 생성하고 중복이 제거된 값을 담을 리스트 `std_ary`를 생성한다. 

N만큼 반복하면서 단어를 입력받고 set에 담아 중복을 제거한다.

``` python
N = int(input())
ary = set()
std_ary = []
for _ in range(N):
    S = input()
    ary.add(S) # set에 담아 중복 제거
```

<br>

📌 ary 내에 요소를 std_ary에 담고 std_ary를 정렬한다.

key를 지정하지 않으면 알파벳순에 따라 정렬되는데, 여기서 다시한번 key에 길이값(len)을 입력해서 길이에 따라 정렬한다.

그리고 std_ary의 요소를 출력한다.

``` python
for i in ary:
    std_ary.append(i) # 중복 제거된 값을 리스트에 담음

std_ary.sort() # 알파벳순에 따라 정렬
std_ary.sort(key = len) # 길이에 따라 정렬 
for i in std_ary:
    print(i)
```

<br>

#### 전체코드

``` python
N = int(input())
ary = set()
std_ary = []
for _ in range(N):
    S = input()
    ary.add(S) # set에 담아 중복 제거

for i in ary:
    std_ary.append(i) # 중복 제거된 값을 리스트에 담음

std_ary.sort() # 알파벳순에 따라 정렬
std_ary.sort(key = len) # 길이에 따라 정렬 
for i in std_ary:
    print(i)
```

