## 파이썬 다음 소수(백준 BOJ 4134)

<br>

## 문제

정수 n(0 ≤ n ≤ 4*109)가 주어졌을 때, n보다 크거나 같은 소수 중 가장 작은 소수 찾는 프로그램을 작성하시오.

<br>

## 입력

첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다.

<br>

## 출력

각각의 테스트 케이스에 대해서 n보다 크거나 같은 소수 중 가장 작은 소수를 한 줄에 하나씩 출력한다.

<br>

## 예제 입력 1

```
3
6
20
100
```

## 예제 출력 1

```
7
23
101
```

<br>

## 📝 풀어보기

문제를 풀기에 앞서서 소수 판별에 대해 알아보자.

``` python
# 소수 판별(비효율적)
def primenumber(a):
  for i in range(2, a):
      if a % i == 0:
        return false
  return true
```

위의 함수처럼, 소수는 a라는 숫자가 입력되면 2부터 a까지의 범위에서 a를 i로 나눈 값이 0이면 나누어 떨어지는 것이므로 소수가 아니게 된다. 하지만 이렇게 소수를 판별하게 되면 a가 커질 경우에 굉장히 오랜 시간이 걸린다.

<br>

### 약수의 원리 사용하기

25의 약수는 1, 5, 25이다.

이 약수들의 조합은 아래처럼 앞뒤로 짝지을 수 있다.

1x25 = 25

5x5 = 25

25x1 = 25

이는 1과 자기자신을 제외한 약수가 존재하는지 확인하려면, 자기 자신의 제곱근(루트)까지만 확인하면 된다는 뜻이 된다.

``` python
# 1과 자기자신을 제외한 약수가 존재하는지 확인하려면, 자기자신의 제곱근(루트)까지만 확인
def primenumber(a):
  for i in range(2, int(math.sqrt(x)+1)):
      if a % i == 0:
          return False
  return True
```

<br>

문제를 풀어보자

위의 방법을 참고하여 아래와 같은 함수를 작성한다.

0과 1은 소수가 아니므로 false를 반환한다.

``` python
import math
import sys
input = sys.stdin.readline

def is_prime(a):
    if a == 0 or a == 1:
        return False
    for i in range(2, int(math.sqrt(a))+1):
        if a % i == 0:
            return False
    return True
```

<br>

테스트 케이스의 개수 t를 입력받고

t만큼 반복하면서 숫자를 입력받는다.

while문 안에서 True(소수)를 반환받으면 출력을 하고 반복을 종료한다. 소수가 아닐 경우엔 n값을 1씩 증가시키고 반복한다.

``` python
t = int(input())

for i in range(t):
    n = int(input())
    while True:
        if is_prime(n) == True:
            print(n)
            break
        else:
            n += 1
```

<br>

## 전체코드

``` python
# 소수 판별(비효율적)
# def primenumber(a):
#   for i in range(2, a):
#       if a % i == 0:
#           return false


# 1과 자기자신을 제외한 약수가 존재하는지 확인하려면, 자기자신의 제곱근(루트)까지만 확인하면 된다
# def primenumber(a):
#   for i in range(2, int(math.sqrt(x)+1)):
#       if a % i == 0:
#           return False
#   return True

import math

import sys
input = sys.stdin.readline

def is_prime(a):
    if a == 0 or a == 1:
        return False
    for i in range(2, int(math.sqrt(a))+1):
        if a % i == 0:
            return False
    return True

t = int(input())

for i in range(t):
    n = int(input())
    while True:
        if is_prime(n) == True:
            print(n)
            break
        else:
            n += 1
```

