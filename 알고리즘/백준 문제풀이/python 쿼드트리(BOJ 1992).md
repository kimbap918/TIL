## 파이썬 쿼드트리(백준 BOJ 1992)

<br>

## 문제

흑백 영상을 압축하여 표현하는 데이터 구조로 쿼드 트리(Quad Tree)라는 방법이 있다. 흰 점을 나타내는 0과 검은 점을 나타내는 1로만 이루어진 영상(2차원 배열)에서 같은 숫자의 점들이 한 곳에 많이 몰려있으면, 쿼드 트리에서는 이를 압축하여 간단히 표현할 수 있다.

주어진 영상이 모두 0으로만 되어 있으면 압축 결과는 "0"이 되고, 모두 1로만 되어 있으면 압축 결과는 "1"이 된다. 만약 0과 1이 섞여 있으면 전체를 한 번에 나타내지를 못하고, 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래, 이렇게 4개의 영상으로 나누어 압축하게 되며, 이 4개의 영역을 압축한 결과를 차례대로 괄호 안에 묶어서 표현한다

![img](https://www.acmicpc.net/JudgeOnline/upload/201007/qq.png)

위 그림에서 왼쪽의 영상은 오른쪽의 배열과 같이 숫자로 주어지며, 이 영상을 쿼드 트리 구조를 이용하여 압축하면 "`(0(0011)(0(0111)01)1)`"로 표현된다. N ×N 크기의 영상이 주어질 때, 이 영상을 압축한 결과를 출력하는 프로그램을 작성하시오.

<br>

## 입력

첫째 줄에는 영상의 크기를 나타내는 숫자 N 이 주어진다. N 은 언제나 2의 제곱수로 주어지며, 1 ≤ N ≤ 64의 범위를 가진다. 두 번째 줄부터는 길이 N의 문자열이 N개 들어온다. 각 문자열은 0 또는 1의 숫자로 이루어져 있으며, 영상의 각 점들을 나타낸다.

## 출력

영상을 압축한 결과를 출력한다.

<br>

## 예제 입력 1

```
8
11110000
11110000
00011100
00011100
11110000
11110000
11110011
11110011
```

## 예제 출력 1 

```
((110(0101))(0010)1(0001))
```

<br>

## 📝 풀어보기

이 문제는 색종이 만들기(BOJ 2630)과 푸는 방법이 거의 같다.

📌 영상의 크기를 나타내는 숫자 N 을 입력받고 N의 길이만큼 문자열을 입력받아 저장한다.

``` python
input = sys.stdin.readline
N = int(input())
video = [ list(map(int, input().rstrip())) for i in range(N)]
```

<br>

📌 (x, y)좌표값, 그리고 크기 N을 받아 작동하는 함수를 생성한다.

영상의 초기값을 변수에 저장해둔다.

x 부터 x+N까지, y부터 y+N범위까지 반복하면서 초기값과 탐색값의 값이 서로 다를경우에 -1을 저장하고 반복을 종료한다.

``` python
def quardtree(x, y, N):
    dot = video[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            # 0과 1이 섞여있을경우
            if dot != video[i][j]:
                dot = -1
                break
```

<br>

📌 dot 가 -1일 경우 출력의 시작과 끝에 괄호를 넣고 

`quardtree(x, y, N)` x,y 좌표는 그대로, N의 가로와 세로 크기는 반씩 줄어든 즉, 제 1사분면

`quardtree(x, y+N, N)` x의 좌표는 그대로, y는 y에 N//2만큼 더한, N의 가로와 세로 크기는 반씩 줄어든 즉, 제 2사분면

 `quardtree(x+N, y, N)` x의 좌표는 x에 N//2만큼 더한, y의 좌표는 그대로, N의 가로와 세로 크기는 반씩 줄어든 즉, 제 3사분면

` quardtree(x+N, y+N, N)` x,y 좌표는 x,y에 각각 N//2만큼 더한, N의 가로와 세로 크기는 반씩 줄어든 즉, 제 4사분면

4가지를 재귀하여 탐색한다. (초기값과 탐색값이 다르기 때문)

영상이 전부 1일 경우엔 1을, 0일 경우엔 0을 출력한다.

``` python
    if dot == -1:
        print("(", end='')
        N = N // 2
        quardtree(x, y, N)
        quardtree(x, y+N, N)
        quardtree(x+N, y, N)
        quardtree(x+N, y+N, N)
        print(")", end='')
    elif dot == 1: # 영상이 전부 1일 경우
        print(1, end='')
    else: # 영상이 전부 0인 경우
        print(0, end='')
```

<br>

## 전체코드

``` python
# 쿼드트리
import sys

input = sys.stdin.readline
N = int(input())
video = [ list(map(int, input().rstrip())) for i in range(N)]

def quardtree(x, y, N):
    dot = video[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            # 0과 1이 섞여있을경우
            if dot != video[i][j]:
                dot = -1
                break
    if dot == -1:
        print("(", end='')
        N = N // 2
        quardtree(x, y, N)
        quardtree(x, y+N, N)
        quardtree(x+N, y, N)
        quardtree(x+N, y+N, N)
        print(")", end='')
    elif dot == 1: # 영상이 전부 1일 경우
        print(1, end='')
    else: # 영상이 전부 0인 경우
        print(0, end='')
quardtree(0, 0, N)
```

