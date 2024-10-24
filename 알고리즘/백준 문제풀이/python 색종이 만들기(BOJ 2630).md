## 파이썬 색종이 만들기(백준 BOJ 2630)

<br>

## 문제

아래 <그림 1>과 같이 여러개의 정사각형칸들로 이루어진 정사각형 모양의 종이가 주어져 있고, 각 정사각형들은 하얀색으로 칠해져 있거나 파란색으로 칠해져 있다. 주어진 종이를 일정한 규칙에 따라 잘라서 다양한 크기를 가진 정사각형 모양의 하얀색 또는 파란색 색종이를 만들려고 한다.

![img](https://www.acmicpc.net/upload/images/bwxBxc7ghGOedQfiT3p94KYj1y9aLR.png)

전체 종이의 크기가 N×N(N=2k, k는 1 이상 7 이하의 자연수) 이라면 종이를 자르는 규칙은 다음과 같다.

전체 종이가 모두 같은 색으로 칠해져 있지 않으면 가로와 세로로 중간 부분을 잘라서 <그림 2>의 I, II, III, IV와 같이 똑같은 크기의 네 개의 N/2 × N/2색종이로 나눈다. 나누어진 종이 I, II, III, IV 각각에 대해서도 앞에서와 마찬가지로 모두 같은 색으로 칠해져 있지 않으면 같은 방법으로 똑같은 크기의 네 개의 색종이로 나눈다. 이와 같은 과정을 잘라진 종이가 모두 하얀색 또는 모두 파란색으로 칠해져 있거나, 하나의 정사각형 칸이 되어 더 이상 자를 수 없을 때까지 반복한다.

위와 같은 규칙에 따라 잘랐을 때 <그림 3>은 <그림 1>의 종이를 처음 나눈 후의 상태를, <그림 4>는 두 번째 나눈 후의 상태를, <그림 5>는 최종적으로 만들어진 다양한 크기의 9장의 하얀색 색종이와 7장의 파란색 색종이를 보여주고 있다.

![img](https://www.acmicpc.net/upload/images/VHJpKWQDv.png)

입력으로 주어진 종이의 한 변의 길이 N과 각 정사각형칸의 색(하얀색 또는 파란색)이 주어질 때 잘라진 하얀색 색종이와 파란색 색종이의 개수를 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에는 전체 종이의 한 변의 길이 N이 주어져 있다. N은 2, 4, 8, 16, 32, 64, 128 중 하나이다. 색종이의 각 가로줄의 정사각형칸들의 색이 윗줄부터 차례로 둘째 줄부터 마지막 줄까지 주어진다. 하얀색으로 칠해진 칸은 0, 파란색으로 칠해진 칸은 1로 주어지며, 각 숫자 사이에는 빈칸이 하나씩 있다.

## 출력

첫째 줄에는 잘라진 햐얀색 색종이의 개수를 출력하고, 둘째 줄에는 파란색 색종이의 개수를 출력한다.

<br>

## 예제 입력 1

```
8
1 1 0 0 0 0 1 1
1 1 0 0 0 0 1 1
0 0 0 0 1 1 0 0
0 0 0 0 1 1 0 0
1 0 0 0 1 1 1 1
0 1 0 0 1 1 1 1
0 0 1 1 1 1 1 1
0 0 1 1 1 1 1 1
```

## 예제 출력 1 

```
9
7
```

<br>

## 📝 풀어보기

이 문제는 분할정복에 관한 문제다.

분할정복이 뭘까?

분할정복이 뭔지 궁금해서 찾아보니 간단하게는 `재귀적으로 자신을 호출하면서 그 연산의 단위를 조금씩 줄여가는 방식` 이라고 되어있다.

이 말이 잘 와닿지 않아서 좀 더 찾아보니 더 와닿는 표현이 있었다.

`주어진 문제를 작은 사례로 나누고(Divide), 각각의 작은 문제들을 해결하여 정복(Conquer) 하는 방식.`

<br>

이 문제는 주어진 정사각형의 색종이 판이 있으면, 종이가 모두 같은 색으로 칠해져 있지 않을때 가로와 세로의 중간 부분을 잘라서 

4등분하여 문제를 풀어야한다. 마찬가지로 4등분된 종이에서도 전부 색이 같지 않다면 다시 종이를 4등분한다.

좌표평면에 대해서 공부할때 사분면(quadrant) 이라는 말을 들어봤을것이다. 

사분면을 생각하면서 이 문제를 풀어보자.

<br>

📌 종이 한 변의 길이 N을 입력받는다. 그리고 정사각형 칸들의 색 상태(하얀색, 파란색 중 하나)를 각각 입력받는다.

파란색과 하얀색의 개수를 저장할 리스트를 생성해둔다.

``` python
import sys

N = int(sys.stdin.readline()) # 종이 한 변의 길이
# 정사각형 칸들의 색 상태
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] 
# 파란색, 흰색 결과값을 담을 리스트
res = []
```

<br>

📌  종이의(x, y)좌표와 한 변의 길이(N)를 받아 작동하는 함수를 만든다. 처음 x,y는 [0,0]에서 시작할것이고 색종이 크기는 N이므로 paper_cnt(0, 0, N)이 실행될것이다.

색깔의 초기 값을 담기 위해 변수를 하나 생성해서 저장한다. `papaer[x][y]`의 색깔이 담긴다.

x부터 x+N, y부터 y+N범위까지 반복하면서 초기에 저장한 색과 다르다면 

`paper_cnt(x, y, N//2)` x,y 좌표는 그대로, N의 가로와 세로 크기는 반씩 줄어든 즉, 제 1사분면

`paper_cnt(x, y+N//2, N//2)` x의 좌표는 그대로, y는 y에 N//2만큼 더한, N의 가로와 세로 크기는 반씩 줄어든 즉, 제 2사분면

 `paper_cnt(x+N//2, y, N//2)` x의 좌표는 x에 N//2만큼 더한, y의 좌표는 그대로, N의 가로와 세로 크기는 반씩 줄어든 즉, 제 3사분면

` paper_cnt(x+N//2, y+N//2, N//2)` x,y 좌표는 x,y에 각각 N//2만큼 더한, N의 가로와 세로 크기는 반씩 줄어든 즉, 제 4사분면

이렇게 4등분하여 다시 재귀의 형태로 호출한다.

마지막으로 색깔을 구분해 리스트에 넣고 각각의 개수를 출력한다.

``` python
def paper_cnt(x, y, N):
    color = paper[x][y] # 색깔이 초기 값
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != paper[i][j]: # 종이가 모두 같은 색으로 칠해져 있지 않다면?
                paper_cnt(x, y, N//2) # 제 1사분면 
                paper_cnt(x, y+N//2, N//2) # 제 2사분면
                paper_cnt(x+N//2, y, N//2) # 제 3사분면
                paper_cnt(x+N//2, y+N//2, N//2) # 제 4사분면
                return
    if color == 0:
        res.append(0)
    else:
        res.append(1)
        
paper_cnt(0,0,N) # 시작지점
print(res.count(0))
print(res.count(1))
```

<br>

## 전체코드

``` python
# 분할정복 : 재귀적으로 자신을 호출하면서 그 연산의 단위를 조금씩 줄여가는 방식
# 주어진 문제를 작은 사례로 나누고(Divide) 각각의 작은 문제들을 해결하여 정복(Conquer)
import sys

N = int(sys.stdin.readline()) # 종이 한 변의 길이
# 정사각형 칸들의 색 상태
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] 
# 파란색, 흰색 결과값을 담을 리스트
res = []

def paper_cnt(x, y, N):
    color = paper[x][y] # 색깔이 초기 값
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != paper[i][j]: # color의 값이 현재 위치의 값과 다르다면
                paper_cnt(x, y, N//2) # 제 1사분면 
                paper_cnt(x, y+N//2, N//2) # 제 2사분면
                paper_cnt(x+N//2, y, N//2) # 제 3사분면
                paper_cnt(x+N//2, y+N//2, N//2) # 제 4사분면
                return
    if color == 0:
        res.append(0)
    else:
        res.append(1)

paper_cnt(0,0,N) # 시작지점
print(res.count(0))
print(res.count(1))
```

