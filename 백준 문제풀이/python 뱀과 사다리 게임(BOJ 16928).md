

## 파이썬 뱀과 사다리 게임(BOJ 16928)

<br>

## 문제

[뱀과 사다리 게임](https://en.wikipedia.org/wiki/Snakes_and_Ladders)을 즐겨 하는 큐브러버는 어느 날 궁금한 점이 생겼다.

> 주사위를 조작해 내가 원하는 수가 나오게 만들 수 있다면, 최소 몇 번만에 도착점에 도착할 수 있을까?

게임은 정육면체 주사위를 사용하며, 주사위의 각 면에는 1부터 6까지 수가 하나씩 적혀있다. 게임은 크기가 10×10이고, 총 100개의 칸으로 나누어져 있는 보드판에서 진행된다. 보드판에는 1부터 100까지 수가 하나씩 순서대로 적혀져 있다.

플레이어는 주사위를 굴려 나온 수만큼 이동해야 한다. 예를 들어, 플레이어가 i번 칸에 있고, 주사위를 굴려 나온 수가 4라면, i+4번 칸으로 이동해야 한다. 만약 주사위를 굴린 결과가 100번 칸을 넘어간다면 이동할 수 없다. 도착한 칸이 사다리면, 사다리를 타고 위로 올라간다. 뱀이 있는 칸에 도착하면, 뱀을 따라서 내려가게 된다. 즉, 사다리를 이용해 이동한 칸의 번호는 원래 있던 칸의 번호보다 크고, 뱀을 이용해 이동한 칸의 번호는 원래 있던 칸의 번호보다 작아진다.

게임의 목표는 1번 칸에서 시작해서 100번 칸에 도착하는 것이다.

게임판의 상태가 주어졌을 때, 100번 칸에 도착하기 위해 주사위를 굴려야 하는 횟수의 최솟값을 구해보자.

<br>

## 입력

첫째 줄에 게임판에 있는 사다리의 수 N(1 ≤ N ≤ 15)과 뱀의 수 M(1 ≤ M ≤ 15)이 주어진다.

둘째 줄부터 N개의 줄에는 사다리의 정보를 의미하는 x, y (x < y)가 주어진다. x번 칸에 도착하면, y번 칸으로 이동한다는 의미이다.

다음 M개의 줄에는 뱀의 정보를 의미하는 u, v (u > v)가 주어진다. u번 칸에 도착하면, v번 칸으로 이동한다는 의미이다.

1번 칸과 100번 칸은 뱀과 사다리의 시작 또는 끝이 아니다. 모든 칸은 최대 하나의 사다리 또는 뱀을 가지고 있으며, 동시에 두 가지를 모두 가지고 있는 경우는 없다. 항상 100번 칸에 도착할 수 있는 입력만 주어진다.

<br>

## 출력

100번 칸에 도착하기 위해 주사위를 최소 몇 번 굴려야 하는지 출력한다.

<br>

## 예제 입력 1 

```
3 7
32 62
42 68
12 98
95 13
97 25
93 37
79 27
75 19
49 47
67 17
```

## 예제 출력 1 

```
3
```

1. 5를 굴려 6으로 이동한다.
2. 6을 굴려 12로 이동한다. 이 곳은 98로 이동하는 사다리가 있기 때문에, 98로 이동한다.
3. 2를 굴려 100으로 이동한다.

## 예제 입력 2 

```
4 9
8 52
6 80
26 42
2 72
51 19
39 11
37 29
81 3
59 5
79 23
53 7
43 33
77 21
```

## 예제 출력 2 

```
5
```

1. 5를 굴려 6으로 이동하고, 사다리를 이용해 80으로 이동한다. 
2. 6을 굴려 86으로
3. 6을 또 굴려 92로
4. 6을 또 굴려 98로 이동하고
5. 2를 굴려 100으로 이동한다.

<br>

## 📝 풀어보기 

게임 보드의 칸은 총 100칸으로 나눠져있다.

board와 visited에 이동 경로를 기록하기 위해 [0]을 100칸+1만큼 저장해둔다.

ladders, snakes 에는 사다리와 뱀의 시작과 끝 좌표를 각각 키와 값에 기록해둔다.

dice는 주사위의 눈금을 저장한 리스트다.

뱀의 수(N), 사다리의 수(M)를 입력받는다.

``` python
from collections import deque
from pprint import pprint
import sys
input = sys.stdin.readline

board = [0] * 101
visited = [False] * 101 
ladders, snakes = dict(), dict()
dice = [1, 2, 3, 4, 5, 6]

# N = 뱀의 수 = 뱀은 밟으면 뱀을따라 내려간다
# M = 사다리의 수 = 사다리는 밟으면 사다리를 타고 올라간다.
N, M = map(int, input().split())
```

<br>

N의 길이만큼 사다리의 시작과 끝의 좌표를 입력받아 ladders에 저장해둔다.

M의 길이만큼 사다리의 시작과 끝의 좌표를 입력받아 snakes에 저장해둔다.

``` python
for i in range(N):
    # start, end
    x, y = map(int, input().split())
    # [키] = 값
    ladders[x] = y

for i in range(M):
    # start, end
    u, v = map(int, input().split())
    snakes[u] = v
```

<br>

deque Q를 생성해서 처음 시작지점 1을 저장해두고 함수 BFS를 선언한다.

Q에 저장해둔 시작지점을 꺼내 a에 저장하고, a가 도착지점에 도달하면 board의 a번째 인덱스를 출력하고 반복을 종료한다.

dice의 눈금(1, 2, 3, 4, 5, 6)을 순회하면서 시작지점 a에 눈금의 값을 더한다.

더한 눈금이 100을 넘지않고, 방문하지 않은 칸 중에서 사다리를 만나면 위치를 사다리의  도착위치값으로 바꾸고 뱀을 만나면 뱀의 도착위치값으로 바꿔준다.

방문하지 않은곳이 있다면 True로 바꿔주고, 주사위를 굴린 횟수+1 을 누적해서 저장해준다.

Q에 현재 위치값을 다시 넣어준다.

``` python
# 시작지점
Q = deque()
Q.append(1)

def BFS():
    while Q:
        a = Q.popleft()
        # 마지막칸에 도착하면
        if a == 100:
            print(board[a])
            break
        for i in dice:
            next_block = a + i
            if next_block <= 100 and not visited[next_block]:
                if next_block in ladders.keys():
                    next_block = ladders[next_block]
                if next_block in snakes.keys():
                    next_block = snakes[next_block]
                if not visited[next_block]:
                    visited[next_block] = True
                    board[next_block] = board[a] + 1
                    Q.append(next_block)
```

<br>

#### 전체코드

``` python
from collections import deque
from pprint import pprint
import sys
input = sys.stdin.readline

board = [0] * 101
visited = [False] * 101 
ladders, snakes = dict(), dict()
dice = [1, 2, 3, 4, 5, 6]

# N = 뱀의 수 = 뱀은 밟으면 뱀을따라 내려간다
# M = 사다리의 수 = 사다리는 밟으면 사다리를 타고 올라간다.
N, M = map(int, input().split())

for i in range(N):
    # start, end
    x, y = map(int, input().split())
    # [키] = 값
    ladders[x] = y

for i in range(M):
    # start, end
    u, v = map(int, input().split())
    snakes[u] = v

# 시작지점
Q = deque()
Q.append(1)

def BFS():
    while Q:
        a = Q.popleft()
        # 마지막칸에 도착하면
        if a == 100:
            print(board[a])
            break
        for i in dice:
            next_block = a + i
            if next_block <= 100 and not visited[next_block]:
                if next_block in ladders.keys():
                    next_block = ladders[next_block]
                if next_block in snakes.keys():
                    next_block = snakes[next_block]
                if not visited[next_block]:
                    visited[next_block] = True
                    board[next_block] = board[a] + 1
                    Q.append(next_block)

BFS()
```

<br>



