

## 파이썬 Solved.Ac(BOJ 18110)

<br>

## 문제

[solved.ac](http://solved.ac/)는 Sogang ICPC Team 학회원들의 알고리즘 공부에 도움을 주고자 만든 서비스이다. 지금은 서강대뿐만 아니라 수많은 사람들이 solved.ac의 도움을 받아 알고리즘 공부를 하고 있다.

![img](https://www.acmicpc.net/problem/18110)

ICPC Team은 백준 온라인 저지에서 문제풀이를 연습하는데, 백준 온라인 저지의 문제들에는 난이도 표기가 없어서, 지금까지는 다양한 문제를 풀어 보고 싶더라도 난이도를 가늠하기 어려워 무슨 문제를 풀어야 할지 판단하기 곤란했기 때문에 solved.ac가 만들어졌다. solved.ac가 생긴 이후 전국에서 200명 이상의 기여자 분들께서 소중한 난이도 의견을 공유해 주셨고, 지금은 약 7,000문제에 난이도 표기가 붙게 되었다.

어떤 문제의 난이도는 그 문제를 푼 사람들이 제출한 **난이도 의견**을 바탕으로 결정한다. 난이도 의견은 그 사용자가 생각한 난이도를 의미하는 정수 하나로 주어진다. solved.ac가 사용자들의 의견을 바탕으로 난이도를 결정하는 방식은 다음과 같다.

- 아직 아무 의견이 없다면 문제의 난이도는 0으로 결정한다.
- 의견이 하나 이상 있다면, 문제의 난이도는 모든 사람의 난이도 의견의 30% 절사평균으로 결정한다.

절사평균이란 극단적인 값들이 평균을 왜곡하는 것을 막기 위해 가장 큰 값들과 가장 작은 값들을 제외하고 평균을 내는 것을 말한다. 30% 절사평균의 경우 위에서 15%, 아래에서 15%를 각각 제외하고 평균을 계산한다. 따라서 20명이 투표했다면, 가장 높은 난이도에 투표한 3명과 가장 낮은 난이도에 투표한 3명의 투표는 평균 계산에 반영하지 않는다는 것이다.

제외되는 사람의 수는 위, 아래에서 각각 반올림한다. 25명이 투표한 경우 위, 아래에서 각각 3.75명을 제외해야 하는데, 이 경우 반올림해 4명씩을 제외한다.

마지막으로, 계산된 평균도 정수로 반올림된다. 절사평균이 16.7이었다면 최종 난이도는 17이 된다.

사용자들이 어떤 문제에 제출한 난이도 의견 목록이 주어질 때, solved.ac가 결정한 문제의 난이도를 계산하는 프로그램을 작성하시오.

<br>

## 입력

첫 번째 줄에 난이도 의견의 개수 *n*이 주어진다. (0 ≤ *n* ≤ 3 × 105)

이후 두 번째 줄부터 1 + *n*번째 줄까지 사용자들이 제출한 난이도 의견 *n*개가 한 줄에 하나씩 주어진다. 모든 난이도 의견은 1 이상 30 이하이다.

<br>

## 출력

solved.ac가 계산한 문제의 난이도를 출력한다.

<br>

## 예제 입력 1 

```
5
1
5
5
7
8
```

## 예제 출력 1 

```
6
```

5명의 15%는 0.75명으로, 이를 반올림하면 1명이다. 따라서 solved.ac는 가장 높은 난이도 의견과 가장 낮은 난이도 의견을 하나씩 제외하고, {5, 5, 7}에 대한 평균으로 문제 난이도를 결정한다.

## 예제 입력 2 

```
10
1
13
12
15
3
16
13
12
14
15
```

## 예제 출력 2 

```
13
```

<br>

## 📝 풀어보기

문제 자체는 쉽지만 파이썬의 반올림 함정이 숨어있어서 작성한다.

<br>

파이썬은 math 라이브러리를 사용하지 않아도 round()함수 사용이 가능하다.

```python
print(round(2.5))
print(round(1.5))
print(round(0.5))
```

위의 반올림을 한번 보자. 우리의 머릿속에는 3, 2, 1이 각각 출력될것이라 생각한다.

하지만 파이썬의 출력에서는 

``` python
2
2
0
```

이 나온다. 왜일까?

#### 4사5입

**반올림 자리가 4이하면 버리고, 5이상이면 올린다** 는 뜻이다. 우리가 학교에서 배운 반올림은 4사5입 방식이다. 하지만 데이터가 .5로 끝나는 숫자가 아주 많다면 어떨까. 4사5입 방식으로 반올림을 하면 전체적인 결과가 0.5정도 커지게된다.

이런 통계적 오류를 막기위해 파이썬에서는 5사5입 방식을 적용하는데 **반올림 자리가 5인 경우, 앞자리가 홀수면 올리고 짝수면 버림을 한다.** 그래서 위의 문제를 round 함수를 사용해서 풀려고 하면 몇가지 테스트 케이스에서 오답이 생긴다.

<br>

#### 4사5입 반올림 만들기

그렇다면 반올림 함수를 만드는 방법이 있을것이다.

n이 들어오면 n에서 소숫점을 버린 n을 뺐을때, 나머지가 0.5보다 크거나 같으면 올려주고 그외엔 버림을 한 n을 반환하면 된다.

``` python
def round_(n):
    return int(n)+1 if n-int(n) >= 0.5 else int(n)
```

<br>

#### decimal 사용

decimal을 사용하는 방법도 있다. 

``` python
import decimal

context = decimal.getcontext()
context.rounding = decimal.ROUND_HALF_UP
print(round(decimal.Decimal(2.5), 0))

>> 3
```

<br>

#### 전체코드

``` python
import sys
from collections import deque
input = sys.stdin.readline

def round_(n):
    return int(n)+1 if n-int(n) >= 0.5 else int(n)

N = int(input())
rate = round_(N * 0.15)
score = deque(sorted(int(input()) for _ in range(N)))

for i in range(rate):
    score.popleft()
    score.pop()

if sum(score) != 0:
    print(round_((sum(score)/len(score))))
else:
    print(0)
```

