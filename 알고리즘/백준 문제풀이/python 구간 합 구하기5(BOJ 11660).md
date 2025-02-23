## 파이썬 구간 합 구하기5(백준 BOJ 11660)

<br>

## 문제

N×N개의 수가 N×N 크기의 표에 채워져 있다. (x1, y1)부터 (x2, y2)까지 합을 구하는 프로그램을 작성하시오. (x, y)는 x행 y열을 의미한다.

예를 들어, N = 4이고, 표가 아래와 같이 채워져 있는 경우를 살펴보자.

| 1    | 2    | 3    | 4    |
| ---- | ---- | ---- | ---- |
| 2    | 3    | 4    | 5    |
| 3    | 4    | 5    | 6    |
| 4    | 5    | 6    | 7    |

여기서 (2, 2)부터 (3, 4)까지 합을 구하면 3+4+5+4+5+6 = 27이고, (4, 4)부터 (4, 4)까지 합을 구하면 7이다.

표에 채워져 있는 수와 합을 구하는 연산이 주어졌을 때, 이를 처리하는 프로그램을 작성하시오.

<br>

## 입력

첫째 줄에 표의 크기 N과 합을 구해야 하는 횟수 M이 주어진다. (1 ≤ N ≤ 1024, 1 ≤ M ≤ 100,000) 둘째 줄부터 N개의 줄에는 표에 채워져 있는 수가 1행부터 차례대로 주어진다. 다음 M개의 줄에는 네 개의 정수 x1, y1, x2, y2 가 주어지며, (x1, y1)부터 (x2, y2)의 합을 구해 출력해야 한다. 표에 채워져 있는 수는 1,000보다 작거나 같은 자연수이다. (x1 ≤ x2, y1 ≤ y2)

<br>

## 출력

총 M줄에 걸쳐 (x1, y1)부터 (x2, y2)까지 합을 구해 출력한다.

<br>

## 예제 입력 1

```
4 3
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7
2 2 3 4
3 4 3 4
1 1 4 4
```

## 예제 출력 1

```
27
6
64
```

## 예제 입력 2

```
2 4
1 2
3 4
1 1 1 1
1 2 1 2
2 1 2 1
2 2 2 2
```

## 예제 출력 2

```
1
2
3
4
```

<br>

## 📝 풀어보기

📌 표의 크기 N과 합을 구해야하는 횟수 M을 입력받는다.

요소의 크기와 리스트의 크기를 N+1 로 생성해서 저장한다.

N개의 줄만큼 숫자를 입력 받아 저장할 리스트 nums_table을 입력받는다.

``` python
import sys
input = sys.stdin.readline
N, M = map(int, input().split()) # 4 3
# N+1 크기로 2차원 리스트 생성
dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
nums_table = []
```

<br>

📌 N만큼 반복하면서 숫자를 입력받고 nums_table에 저장해둔다.

``` python
for _ in range(N):
    nums = list(map(int, input().split()))
    nums_table.append(nums)
```

<br>

📌 N만큼 행과 열을 반복하면서 dp의 2번째 행 `dp[i+1][j+1]`부터 (구하는 dp의 이전행 dp + 다음행 이전열 dp - 이전행 이전열 dp) + 숫자가 저장된 테이블 위치의 값을 저장한다. 이렇게 저장되는 dp는 각 행의 맨 마지막 요소가 nums_table의 각 행을 합친 값이 된다.

``` python
for i in range(N): # 0 1 2 3 4 행
    for j in range(N): # 0 1 2 3 4 열
        # dp의 1번째 1번요소부터 저장, (dp[0][1] + dp[1][0] - dp[0][0]) + nums_table[0][0](1)
        # dp[2][1] = dp[1][1](1) + dp[2][0](0) - dp[1][0](0) + nums_table[1][0](2)
        # 구하는 dp의 이전행 dp + 다음행 이전열 dp - 이전행 이전열 dp + 숫자가 저장된 테이블위치의 값 
        # dp의 각 행별 마지막 요소는 해당 구간까지의 합임. 10, 24, 42, 64
        dp[i+1][j+1] = (dp[i][j+1] + dp[i+1][j] - dp[i][j]) + nums_table[i][j]
```

<br>

📌 M만큼 반복하면서 x1, y1 / x2, y2를 입력받는다.

`dp[x2][y2]` 는 구하고자 하는 범위가 만약 C라면 A+B+C가 합쳐진 값이다. 그래서 x1, y1 좌표에서 x2, y2좌표까지만 합이 포함되도록 여기에서 빼나가야한다. 뺀 값을 출력하면 된다.

``` python
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    # dp[3][4](42) - (dp[1][4](10) + dp[3][1](6) - dp[1][1](1))
    print(dp[x2][y2] - (dp[x1-1][y2] + dp[x2][y1-1] - dp[x1-1][y1-1]))
```

<br>

#### 전체코드

``` python
import sys
input = sys.stdin.readline
N, M = map(int, input().split()) # 4 3
# N+1 크기로 2차원 리스트 생성
dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
nums_table = []

for _ in range(N):
    nums = list(map(int, input().split()))
    nums_table.append(nums)

for i in range(N): # 0 1 2 3 4 행
    for j in range(N): # 0 1 2 3 4 열
        # dp의 1번째 1번요소부터 저장, (dp[0][1] + dp[1][0] - dp[0][0]) + nums_table[0][0](1)
        # dp[2][1] = dp[1][1](1) + dp[2][0](0) - dp[1][0](0) + nums_table[1][0](2)
        # 구하는 dp의 이전행 dp + 다음행 이전열 dp - 이전행 이전열 dp + 숫자가 저장된 테이블위치의 값 
        # dp의 각 행별 마지막 요소는 해당 구간까지의 합임. 10, 24, 42, 64
        dp[i+1][j+1] = (dp[i][j+1] + dp[i+1][j] - dp[i][j]) + nums_table[i][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    # dp[3][4](42) - (dp[1][4](10) + dp[3][1](6) - dp[1][1](1))
    print(dp[x2][y2] - (dp[x1-1][y2] + dp[x2][y1-1] - dp[x1-1][y1-1]))
```

