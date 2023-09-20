## 파이썬 직사각형 네 개의 합집합의 면적 구하기(백준 BOJ 2669)

<br>

## 문제

평면에 네 개의 직사각형이 놓여 있는데 그 밑변은 모두 가로축에 평행하다. 이 네 개의 직사각형들은 서로 떨어져 있을 수도 있고, 겹쳐 있을 수도 있고, 하나가 다른 하나를 포함할 수도 있으며, 변이나 꼭짓점이 겹칠 수도 있다.

이 직사각형들이 차지하는 면적을 구하는 프로그램을 작성하시오.

![img](https://www.acmicpc.net/upload/images/8vR77Ew2O2PqvZ1lER716.png)

## 입력

입력은 네 줄이며, 각 줄은 직사각형의 위치를 나타내는 네 개의 정수로 주어진다. 첫 번째와 두 번째의 정수는 사각형의 왼쪽 아래 꼭짓점의 x좌표, y좌표이고 세 번째와 네 번째의 정수는 사각형의 오른쪽 위 꼭짓점의 x좌표, y좌표이다. 모든 x좌표와 y좌표는 1이상이고 100이하인 정수이다.

## 출력

첫 줄에 네개의 직사각형이 차지하는 면적을 출력한다.

<br>

## 예제 입력 1

```
1 2 4 4
2 3 5 7
3 1 6 5
7 3 8 6
```

## 예제 출력 1

```
26
```

<br>

## 📝 풀어보기

📌 주어지는 배열의 크기 N, M개의 정수를 입력받는다.

N의 길이만큼 반복하면서 M개의 정수를 N_list에 입력받는다.

``` python
import sys
input = sys.stdin.readline
N, M = map(int, input().split()) # 주어지는 배열의 크기
# M개의 정수로 배열이 주어질 리스트
N_list = [list(map(int, input().split())) for _ in range(N)]
```

<br>

📌 합을 구할 부분의 개수 K를 입력받고 K만큼 반복하면서 시작 좌표값 i, j 끝 좌표값 x, y를 입력받는다.

i-1 부터 x까지, j-1부터 y까지 반복하면서 cnt에 N_list의 값을 누적하고 출력한다.

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

#### 전체 코드

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

