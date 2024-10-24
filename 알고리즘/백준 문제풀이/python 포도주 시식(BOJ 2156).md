## 파이썬 포도주 시식(백준 BOJ 2156)

<br>

## 문제

효주는 포도주 시식회에 갔다. 그 곳에 갔더니, 테이블 위에 다양한 포도주가 들어있는 포도주 잔이 일렬로 놓여 있었다. 효주는 포도주 시식을 하려고 하는데, 여기에는 다음과 같은 두 가지 규칙이 있다.

1. 포도주 잔을 선택하면 그 잔에 들어있는 포도주는 모두 마셔야 하고, 마신 후에는 원래 위치에 다시 놓아야 한다.
2. 연속으로 놓여 있는 3잔을 모두 마실 수는 없다.

효주는 될 수 있는 대로 많은 양의 포도주를 맛보기 위해서 어떤 포도주 잔을 선택해야 할지 고민하고 있다. 1부터 n까지의 번호가 붙어 있는 n개의 포도주 잔이 순서대로 테이블 위에 놓여 있고, 각 포도주 잔에 들어있는 포도주의 양이 주어졌을 때, 효주를 도와 가장 많은 양의 포도주를 마실 수 있도록 하는 프로그램을 작성하시오. 

예를 들어 6개의 포도주 잔이 있고, 각각의 잔에 순서대로 6, 10, 13, 9, 8, 1 만큼의 포도주가 들어 있을 때, 첫 번째, 두 번째, 네 번째, 다섯 번째 포도주 잔을 선택하면 총 포도주 양이 33으로 최대로 마실 수 있다.

<br>

## 입력

첫째 줄에 포도주 잔의 개수 n이 주어진다. (1 ≤ n ≤ 10,000) 둘째 줄부터 n+1번째 줄까지 포도주 잔에 들어있는 포도주의 양이 순서대로 주어진다. 포도주의 양은 1,000 이하의 음이 아닌 정수이다.

<br>

## 출력

첫째 줄에 최대로 마실 수 있는 포도주의 양을 출력한다.

## 예제 입력 1

```
6
6
10
13
9
8
1
```

## 예제 출력 1

```1
33
```

<br>

## 📝 풀어보기

출처 : https://pacific-ocean.tistory.com/152 깨지고 부서져라

|                             |           |            |                           |                                     |                                               |            |
| --------------------------- | --------- | ---------- | ------------------------- | ----------------------------------- | --------------------------------------------- | ---------- |
| 포도주의 양                 | 6         | 10         | 13                        | 9                                   | 8                                             | 1          |
| 순서                        | wine1     | wine2      | wine3                     | wine4                               | wine5                                         | wine6      |
| 경우의 수                   | w1        | w1 + w2    | w1 + w2, w1 + w3, w2 + w3 | w2 + w3, w1 + w3 + w4, w1 + w2 + w4 | w1 + w2 + w4 + w5, w1 + w3 + w4, w2 + w3 + w5 | ...        |
| 해당 순서까지의 양의 최댓값 | dp[1] = 6 | dp[2] = 16 | dp[3] = 23                | dp[4] = 28                          | dp[5] = 33                                    | dp[6] = 33 |

위의 표에서 경우의 수를 살펴보면, 공통적인 부분에서 dp[3]의 경우의 수에서 w1 + w2는 dp[2]와 같다.

dp[4]의 경우를 알아보자. w2 + w3 은 dp[3]과 같다. 

w1 + w3 + w4 에서 w1은 dp[1]이므로 dp[1] + w3 + w4와 같다.

w1 + w2 + w4 는 w1 + w2가 dp[2]와 같으므로 dp[2] + w4와 같다.

이것을 정리해보자면 dp[4]의 경우의 수는 dp[4-1], dp[4-3] + w[3]  + w[4], dp[4-2] + w[4]가 된다.

이것을 다시 바꾸면 dp[i-1], dp[i-3] + w[i-1] + w[i], dp[i-2] + w[i] 중에 가장 큰 값을 넣어주면 가장 많은 양을 먹을 수 있는 경우의 수가 된다.

``` python
N = int(input())
wine = [0]
for i in range(N):
    wine.append(int(input())) # [0, 6, 10, 13, 9, 8, 1]
dp = [0]
dp.append(wine[1]) # [0, 6]
if N > 1: # 와인잔이 2개 이상일 경우
    dp.append(wine[1] + wine[2]) # dp에 와인의 양 1, 2번 인덱스 값을 추가
for i in range(3, N+1): # 3부터 N+1까지
    dp.append(max(dp[i-1], dp[i-3] + wine[i-1] + wine[i], dp[i-2] + wine[i]))
print(dp[N])
```

