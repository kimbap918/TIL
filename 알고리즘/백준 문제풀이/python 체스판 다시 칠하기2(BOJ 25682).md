## 파이썬 체스판 다시 칠하기2(백준 BOJ 25682)

<br>

## 문제

지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다. 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 지민이는 이 보드를 잘라서 K×K 크기의 체스판으로 만들려고 한다.

체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.

보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 K×K 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 당연히 K×K 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

<br>

## 입력

첫째 줄에 정수 N, M, K가 주어진다. 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다.

<br>

## 출력

첫째 줄에 지민이가 잘라낸 K×K 보드를 체스판으로 만들기 위해 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.

<br>

## 제한

- 1 ≤ N, M ≤ 2000
- 1 ≤ K ≤ min(N, M)

<br>

## 예제 입력 1

```
4 4 3
BBBB
BBBB
BBBW
BBWB
```

## 예제 출력 1

```
2
```

## 예제 입력 2

```
8 8 8
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
```

## 예제 출력 2 

```
1
```

## 예제 입력 3

```
10 13 10
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
WWWWWWWWWWBWB
WWWWWWWWWWBWB
```

## 예제 출력 3 

```
30
```

## 예제 입력 4 

```
9 23 9
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBWWWWWWWW
```

<br>

## 📝 풀어보기

예전의 체스판 다시 칠하기(BOJ 1018)의 확장버전이다.

체스판의 크기가 8x8이 아닌 K값에 따라 바뀐다!

📌 열(N), 행(M), 체스판의 크기(K)를 입력받는다. 그리고 board의 각 행의 상태를 입력받는다.

행과 열을 탐색해서 (1, 1)부터 (c, r)까지 수정해야하는 부분의 개수 합을 저장하기 위해 SUM을 만들어둔다.

``` python
import sys
# from pprint import pprint
input = sys.stdin.readline

N, M, K = map(int, input().split()) # 열, 행, 크기
board = [list(input().rstrip()) for _ in range(N)] # 보드의 각 행의 상태
SUM = [[0] * (M+1) for _ in range(N+1)]
```

<br>

📌 1부터 입력한 M+1, N+1까지 행과 열을 돌면서 c+r이 짝수면, 체스판이 B라고 가정하고 

해당 체스판의 값이 B라면 `SUM[r][c] = SUM[r-1][c] + SUM[r][c-1] - SUM[r-1][c-1]` 을 계산하고, 

해당 체스판의 값이 W라면 `SUM[r][c] = SUM[r-1][c] + SUM[r][c-1] - SUM[r-1][c-1] + 1` 을 계산해서 저장한다.

<br>

c+r이 홀수라면, 위의 계산을 반대로 한다.

``` python
for c in range(1, M+1): # 행 탐색
    for r in range(1, N+1): # 열 탐색
        if (c + r) % 2 == 0: # 행+열이 짝수면, 체스판이 B라고 가정
            if board[r-1][c-1] == 'B': # 해당 체스판의 값이 B면
                SUM[r][c] = SUM[r-1][c] + SUM[r][c-1] - SUM[r-1][c-1]
            else: # 해당 체스판 값이 W면
                SUM[r][c] = SUM[r-1][c] + SUM[r][c-1] - SUM[r-1][c-1] + 1

        else: # 행+열이 홀수면
            if board[r-1][c-1] == 'W': # 해당 체스판 값이 W면
                SUM[r][c] = SUM[r-1][c] + SUM[r][c-1] - SUM[r-1][c-1] 
            else: # 해당 체스판 값이 B면
                SUM[r][c] = SUM[r-1][c] + SUM[r][c-1] - SUM[r-1][c-1] + 1
```

<br>

📌 입력한 KxK모양의 체스판에서 최소값을 구해야 하므로 K부터 M+1, N+1 범위를 탐색하면서 계산한 값의 최대값과 최소값을 저장하고 출력한다.

``` python
max_ = -float('inf')
min_ = float('inf')
for c in range(K, M+1): # K부터 행 탐색
    for r in range(K, N+1): # K부터 열 탐색
        max_ = max(SUM[r][c] - SUM[r-K][c] - SUM[r][c-K] + SUM[r-K][c-K], max_)
        min_ = min(SUM[r][c] - SUM[r-K][c] - SUM[r][c-K] + SUM[r-K][c-K], min_)

print(min(min_, max_, K*K - min_, K*K - max_))
```

<br>

## 전체코드

``` python
import sys
# from pprint import pprint
input = sys.stdin.readline

N, M, K = map(int, input().split()) # 열, 행, 크기
board = [list(input().rstrip()) for _ in range(N)] # 보드의 각 행의 상태
SUM = [[0] * (M+1) for _ in range(N+1)]

# pprint(board)
# pprint(SUM)

for c in range(1, M+1): # 행 탐색
    for r in range(1, N+1): # 열 탐색
        if (c + r) % 2 == 0: # 행+열이 짝수면, 체스판이 B
            if board[r-1][c-1] == 'B': # 해당 체스판의 값이 B면
                SUM[r][c] = SUM[r-1][c] + SUM[r][c-1] - SUM[r-1][c-1]
            else: # 해당 체스판 값이 W면
                SUM[r][c] = SUM[r-1][c] + SUM[r][c-1] - SUM[r-1][c-1] + 1

        else: # 행+열이 홀수면, 체스판이 W
            if board[r-1][c-1] == 'W': # 해당 체스판 값이 W면
                SUM[r][c] = SUM[r-1][c] + SUM[r][c-1] - SUM[r-1][c-1] 
            else: # 해당 체스판 값이 B면
                SUM[r][c] = SUM[r-1][c] + SUM[r][c-1] - SUM[r-1][c-1] + 1
max_ = -float('inf')
min_ = float('inf')
for c in range(K, M+1): # K부터 행 탐색
    for r in range(K, N+1): # K부터 열 탐색
        max_ = max(SUM[r][c] - SUM[r-K][c] - SUM[r][c-K] + SUM[r-K][c-K], max_)
        min_ = min(SUM[r][c] - SUM[r-K][c] - SUM[r][c-K] + SUM[r-K][c-K], min_)

print(min(min_, max_, K*K - min_, K*K - max_))
```

