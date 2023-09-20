## 파이썬 나이순 정렬(백준 BOJ 10814)

<br>

## 문제

온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다. 이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.

<br>

## 입력

첫째 줄에 온라인 저지 회원의 수 N이 주어진다. (1 ≤ N ≤ 100,000)

둘째 줄부터 N개의 줄에는 각 회원의 나이와 이름이 공백으로 구분되어 주어진다. 나이는 1보다 크거나 같으며, 200보다 작거나 같은 정수이고, 이름은 알파벳 대소문자로 이루어져 있고, 길이가 100보다 작거나 같은 문자열이다. 입력은 가입한 순서로 주어진다.

<br>

## 출력

첫째 줄부터 총 N개의 줄에 걸쳐 온라인 저지 회원을 나이 순, 나이가 같으면 가입한 순으로 한 줄에 한 명씩 나이와 이름을 공백으로 구분해 출력한다.

<br>

## 예제 입력 1 

```
3
21 Junkyu
21 Dohyun
20 Sunyoung
```

## 예제 출력 1 

```
20 Sunyoung
21 Junkyu
21 Dohyun
```

<br>

## 📝 풀어보기

📌 회원의 수를 N개만큼 입력받는다. 빈 리스트 `ary`를 생성하고 `N`번만큼 리스트에 담은 A, B를 입력받아 ary에 삽입한다.

삽입할때 인덱스로 정렬하기 위해 `i`를 같이 삽입해준다.

``` python
N = int(input())
ary = []
for i in range(N):
    [A, B] = input().split()
    ary.append([int(A), i, B])
```

<br>

📌 ary를 정렬한다. 인덱스는 ary의[0]번째, [1]번째 [2]번째 요소 순으로 정렬된다.

N만큼 반복하면서 ary의 `[i][0]` `[i][2]` 요소를 출력한다. (20, Sunyoung)

``` python
ary = sorted(ary)
# print(ary) [[20, 2, 'Sunyoung'], [21, 0, 'Junkyu'], [21, 1, 'Dohyun']]
for i in range(N):
    print(ary[i][0], end= ' ')
    print(ary[i][2])
```

<br>

#### 전체코드 

``` python
N = int(input())
ary = []
for i in range(N):
    [A, B] = input().split()
    ary.append([int(A), i, B])

ary = sorted(ary)
# print(ary) [[20, 2, 'Sunyoung'], [21, 0, 'Junkyu'], [21, 1, 'Dohyun']]
for i in range(N):
    print(ary[i][0], end= ' ')
    print(ary[i][2])
```

