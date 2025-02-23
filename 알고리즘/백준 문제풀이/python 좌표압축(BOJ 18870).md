## 파이썬 좌표압축(백준 BOJ 18870)

<br>

## 문제

수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.

Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.

X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.

<br>

## 입력

첫째 줄에 N이 주어진다.

둘째 줄에는 공백 한 칸으로 구분된 X1, X2, ..., XN이 주어진다.

<br>

## 출력

첫째 줄에 X'1, X'2, ..., X'N을 공백 한 칸으로 구분해서 출력한다.

<br>

## 제한

- 1 ≤ N ≤ 1,000,000
- -109 ≤ Xi ≤ 109

<br>

## 예제 입력 1 

```
5
2 4 -10 4 -9
```

## 예제 출력 1

```
2 3 0 3 1
```

## 예제 입력 2 

```
6
1000 999 1000 999 1000 999
```

## 예제 출력 2

```
1 0 1 0 1 0
```

<br>

## 📝 풀어보기

📌 시간초과를 방지하기 위해 `readline`을 사용했다.

좌표값을 입력받아 리스트에 담을 `S`와 S의 중복값을 없애 리스트에 담은 `set_S`를 생성한다.

``` python
# 자신보다 작은 수 -> 압축좌표
import sys
input = sys.stdin.readline
N = int(input())
S = list(map(int, input().split()))
set_S = sorted(list(set(S)))
```

<br>

📌 딕셔너리에 set_S의 길이만큼 반복하면서 set_S[i]의 요소들을 자신보다 작은 수의 개수와 함께 담는다.

S만큼 반복하면서 dic[i]의 요소를 공백과 함께 출력한다.

``` python
dic = {set_S[i] : i for i in range(len(set_S))}
# print(dic)
# print(set_S)

for i in S:
    print(dic[i], end=' ')
```

<br>

#### 전체코드

``` python
# 자신보다 작은 수 -> 압축좌표
import sys
input = sys.stdin.readline
N = int(input())
S = list(map(int, input().split()))
set_S = sorted(list(set(S)))

dic = {set_S[i] : i for i in range(len(set_S))}
# print(dic)
# print(set_S)

for i in S:
    print(dic[i], end=' ')
```

