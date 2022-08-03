## 2차원 배열의 합(백준 BOJ 2167)

<br>

## 문제

2차원 배열이 주어졌을 때 (i, j) 위치부터 (x, y) 위치까지에 저장되어 있는 수들의 합을 구하는 프로그램을 작성하시오. 배열의 (i, j) 위치는 i행 j열을 나타낸다.

<br>

## 입력

첫째 줄에 배열의 크기 N, M(1 ≤ N, M ≤ 300)이 주어진다. 다음 N개의 줄에는 M개의 정수로 배열이 주어진다. 배열에 포함되어 있는 수는 절댓값이 10,000보다 작거나 같은 정수이다. 그 다음 줄에는 합을 구할 부분의 개수 K(1 ≤ K ≤ 10,000)가 주어진다. 다음 K개의 줄에는 네 개의 정수로 i, j, x, y가 주어진다(1 ≤ i ≤ x ≤ N, 1 ≤ j ≤ y ≤ M).

<br>

## 출력

K개의 줄에 순서대로 배열의 합을 출력한다. 배열의 합은 231-1보다 작거나 같다.

<br>

## 예제 입력 1

```
2 3
1 2 4
8 16 32
3
1 1 2 3
1 2 1 2
1 3 2 3
```

## 예제 출력 1

```
63
2
36
```

<br>

## 📝 풀어보기

문제를 이해하는데에 시간이 걸렸던 문제같다.

📌 빠른 입력을 위해 `sys.stdin.readline` 을 사용한다.

먼저 배열의 크기값을 정할 `N, M` 을 입력받는다. N은 행이고, M은 열이다.

N의 값 만큼 `N_list`로 입력받는다. List Comprehension으로 작성했다. 

``` python
import sys
input = sys.stdin.readline
N, M = map(int, input().split()) # 주어지는 배열의 크기
# M개의 정수로 배열이 주어질 리스트
N_list = [list(map(int, input().split())) for _ in range(N)]
```

<br>

📌 그다음 합을 구할 부분의 개수를 `K` 로 입력받는다.

K의 값만큼 반복을 돌면서 행렬의 위치를 입력받는다.

여기서 `i` `j` 는 초기 행렬의 위치값이고, `x` `y` 는 마지막 행렬의 위치값이다.

`i-1 부터 x` 까지, `j-1 부터 y`까지 범위에서 반복을 돌면서 cnt에 리스트의 값을 누적시키고 출력한다.

``` python
K = int(input()) # 합을 구할 부분의 개수
for _ in range(K):
    # i행 j열 위치, x, y위치 
    i, j, x, y = map(int, input().split())
    cnt = 0
    for a in range(i-1, x):
        for b in range(j-1, y):
            cnt += N_list[a][b]
    print(cnt)
```

<br>

#### 전체코드

``` python
import sys
input = sys.stdin.readline
N, M = map(int, input().split()) # 주어지는 배열의 크기
# M개의 정수로 배열이 주어질 리스트
N_list = [list(map(int, input().split())) for _ in range(N)]

K = int(input()) # 합을 구할 부분의 개수
for _ in range(K):
    # i행 j열 위치, x, y위치 
    i, j, x, y = map(int, input().split())
    cnt = 0
    for a in range(i-1, x):
        for b in range(j-1, y):
            cnt += N_list[a][b]
    print(cnt)

# 2 3 -> 2행 3열의 크기를 가진 배열 
# 1 2 4 -> M열(3개)로 
# 8 16 32 -> N행(2줄)이 만들어짐
# 3 -> 합을 구할 연산 K개(테스트 케이스 3개)
# 1 1 2 3 -> (1행 1열부터 2행 3열까지 합을 구하라)
# 1 2 1 2 -> (1행 2열부터 1행 2열까지 합을 구하라)
# 1 3 2 3 -> (1행 3열부터 2행 3열까지 합을 구하라)
```

