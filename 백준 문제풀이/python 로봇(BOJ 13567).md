## 파이썬 로봇(백준 BOJ 13567)

<br>

## 문제

로봇은 명령어를 읽어들여 정사각형 영역 S를 x축 또는 y축과 평행한 방향으로 움직인다. S의 왼쪽 아래 꼭짓점은 (0, 0)이고, 오른쪽 위의 꼭짓점은 (M, M)이다. 처음에 로봇은 (0, 0)에 위치해 있고, 동쪽 방향을 향하고 있다.

명령어는 로봇이 현재 위치에서 행할 동작과 그 동작과 관련된 값으로 주어진다. 동작은 두 가지가 있는데, `TURN`과 `MOVE`이다. `TURN 0` 명령은 현재 위치에서 왼쪽으로 90도 회전, `TURN 1` 명령은 현재 위치에서 오른쪽으로 90도 회전을 의미한다. `MOVE d` 명령은 로봇이 향하고 있는 방향으로 d만큼 움직이는 것을 의미한다. 여기서 d는 양수이다.

명령의 수행 후 로봇이 S의 경계 또는 내부에 있으면 이 명령어는 유효하다. 만일 명령어 수행 후 로봇이 S의 바깥으로 완전히 나가게 된다면 명령어는 유효하지 않다. 일련의 명령어 열을 이루는 각 명령어가 모두 유효하다면, 이 명령어 열을 유효하다고 한다.

예를 들어 로봇이 왼쪽 그림과 같이 (`MOVE 6, TURN 0, MOVE 5, TURN 0, MOVE 2, TURN 0, MOVE 2, TURN 0, MOVE 4, TURN 0, MOVE 3, MOVE 2`) 명령어를 읽어들인다면, 최종적으로 로봇은 (8, 8) 위치에 있게 된다. 가운데 그림과 같이 (`MOVE 10, TURN 0, MOVE 2, TURN 0, MOVE 5, TURN 1, MOVE 5, TURN 1, MOVE 2, TURN 1, MOVE 3, TURN 0, TURN 0, MOVE 6`) 명령어를 읽어들인다면, 로봇은 (7, 10)에 위치하게 된다. 오른쪽 그림과 같이 로봇이 S 바깥으로 나간다면, 명령어 열은 유효하지 않다.

![img](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/userupload/topology/20161106/27f7884c99f7c66d952a1102296b4d62.png)

그림 1. M = 11일 때 세 가지 명령어 열을 받은 로봇의 경로

한 변의 길이가 M인 정사각형과 n개의 명령어, 그리고 로봇이 (0, 0) 위치에서 시작해 동쪽을 바라보고 있을 때, n개의 명령어를 따라 움직였을 때 최종 위치를 출력하는 프로그램을 작성하라.

<br>

## 입력

입력은 표준 입력으로부터 받는다. 첫 줄에는 두 정수 M과 n (1 ≤ M ≤ 1,000, 1 ≤ n ≤ 1,000)이 주어진다. M은 정사각형 S의 한 변의 길이, 즉 오른쪽 맨 위의 좌표는 (M, M)이 된다. n은 로봇이 수행할 n개의 명령어이다. 그 다음 n개의 줄에는 명령어가 하나씩 주어진다. 각 명령어는 `TURN`과 `dir` 또는 `MOVE`와 `d`의 쌍으로 주어진다. 여기서 `dir`은 0 또는 1이며 `d`는 1,000 이하의 양의 정수이다. 로봇의 처음 위치는 (0, 0)이며 동쪽을 바라보고 있음에 유의하라.

<br>

## 출력

표준 출력으로 정확히 한 줄을 출력한다. 명령어 열이 유효하다면 두 음 아닌 정수를 출력하며, 이는 각각 명령어 수행 후 로봇의 위치의 x좌표와 y좌표이고 빈 칸으로 구분되어 있다. 명령어 열이 유효하지 않다면 -1을 출력한다.

<br>

## 예제 입력 1 

```
11 14
MOVE 10
TURN 0
MOVE 2
TURN 0
MOVE 5
TURN 1
MOVE 5
TURN 1
MOVE 2
TURN 1
MOVE 3
TURN 0
TURN 0
MOVE 6
```

## 예제 출력 1

```
7 10
```

## 예제 입력 2

```
11 7
MOVE 5
TURN 0
MOVE 4
TURN 1
MOVE 2
TURN 1
MOVE 5
```

## 예제 출력 2

```
-1
```

## 예제 입력 3

```
2 7
MOVE 2
TURN 0
MOVE 3
TURN 0
MOVE 2
TURN 0
MOVE 2
```

## 예제 출력 3

```
-1
```



## 📝 풀어보기

📌 입력이 많으므로 readline를 사용했다.

방향 계산을 위해 dx, dy에 좌표값을 넣었다. 아래에서 계산을 해서 사용하는 좌표라 순서가 중요하다.

맵의 크기 `M`, 로봇의 이동 횟수 `n`을 입력받는다. x, y는 로봇이 움직일 좌표, dir은 로봇이 움직일 방향이다. check는 이동이 가능한 좌표인지 확인하는 변수다.

``` python
import sys
input = sys.stdin.readline

# 방향 및 x, y 계산을 위함
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# M = 맵의 크기, n = 로봇의 이동 횟수
M, n = map(int, input().split()) 
x, y = 0, 0 # 좌표
dir = 0 # 방향 
check = False
```

<br>

📌 로봇의 이동 횟수만큼 커맨드와 이동숫자를 입력받는다.

 커맨드가 `TURN` 이라면, `1(오른쪽)`일 경우 dir 에서 1을 빼고 dir이 0보다 작다면 3으로 만든다.

`0(왼쪽)` 일 경우 dir을 1 더하고 dir이 3을 넘어가면 0으로 만든다.

커맨드가 `MOVE` 라면 각각의 좌표에 숫자로 형변환 한 num * d[(dir의 숫자)]를 합산한다.

만약 합산된 좌표가 맵을 벗어나면 check를 True로 만들고 반복을 벗어난다. check가 False일 경우엔 좌표를 출력하고 끝낸다.

``` python
for _ in range(n):
    # 로봇의 커맨드 MOVE, TURN..  / 횟수 2, 3..
    com, num = map(str, input().rstrip().split()) # MOVE 10

    if com == "TURN": # 회전일 경우 
        if num == "1": # 1일 경우 (오른쪽 이동)
            dir -= 1 # 3
            if dir < 0:
                dir = 3 
        else: # 0일 경우 (왼쪽 이동) 
            dir += 1 # 1
            if dir > 3: 
                dir = 0 
    elif com == "MOVE":
        x += int(num) * dx[dir] 
        y += int(num) * dy[dir] 
    if x < 0 or x >= M or y < 0 or y >= M:
        print(-1)
        check = True
        break
if not check:
    print(x, y)
```

<br>

#### 전체코드

``` python
import sys

input = sys.stdin.readline

# 방향 및 x, y 계산을 위함
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# M = 맵의 크기, n = 로봇의 이동 횟수
M, n = map(int, input().split()) 
x, y = 0, 0 # 좌표
dir = 0 # 방향 
check = False

for _ in range(n):
    # 로봇의 커맨드 MOVE, TURN..  / 횟수 2, 3..
    com, num = map(str, input().rstrip().split()) # MOVE 10

    if com == "TURN": # 회전일 경우 
        if num == "1": # 1일 경우 (오른쪽 이동)
            dir -= 1 # 3
            if dir < 0:
                dir = 3 
        else: # 0일 경우 (왼쪽 이동) 
            dir += 1 # 1
            if dir > 3: 
                dir = 0 
    elif com == "MOVE":
        x += int(num) * dx[dir] 
        y += int(num) * dy[dir] 
    if x < 0 or x >= M or y < 0 or y >= M:
        print(-1)
        check = True
        break
if not check:
    print(x, y)
```

