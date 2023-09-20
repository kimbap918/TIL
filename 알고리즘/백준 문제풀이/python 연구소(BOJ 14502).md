

## 파이썬 연구소(BOJ 14502)

<br>

## 문제

인체에 치명적인 바이러스를 연구하던 연구소에서 바이러스가 유출되었다. 다행히 바이러스는 아직 퍼지지 않았고, 바이러스의 확산을 막기 위해서 연구소에 벽을 세우려고 한다.

연구소는 크기가 N×M인 직사각형으로 나타낼 수 있으며, 직사각형은 1×1 크기의 정사각형으로 나누어져 있다. 연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다. 

일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다. 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.

예를 들어, 아래와 같이 연구소가 생긴 경우를 살펴보자.

```
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
```

이때, 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 곳이다. 아무런 벽을 세우지 않는다면, 바이러스는 모든 빈 칸으로 퍼져나갈 수 있다.

2행 1열, 1행 2열, 4행 6열에 벽을 세운다면 지도의 모양은 아래와 같아지게 된다.

```
2 1 0 0 1 1 0
1 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 1 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
```

바이러스가 퍼진 뒤의 모습은 아래와 같아진다.

```
2 1 0 0 1 1 2
1 0 1 0 1 2 2
0 1 1 0 1 2 2
0 1 0 0 0 1 2
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
```

벽을 3개 세운 뒤, 바이러스가 퍼질 수 없는 곳을 안전 영역이라고 한다. 위의 지도에서 안전 영역의 크기는 27이다.

연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하는 프로그램을 작성하시오.

<br>

## 입력

첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 8)

둘째 줄부터 N개의 줄에 지도의 모양이 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치이다. 2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수이다.

빈 칸의 개수는 3개 이상이다.

<br>

## 출력

첫째 줄에 얻을 수 있는 안전 영역의 최대 크기를 출력한다.

<br>

## 예제 입력 1 

```
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
```

## 예제 출력 1 

```
27
```

## 예제 입력 2 

```
4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2
```

## 예제 출력 2 

```
9
```

## 예제 입력 3 

```
8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
```

## 예제 출력 3 

```
3
```

<br>

## 📝 풀어보기

BFS문제지만, 벽을 반드시 3개를 세우고, 벽을 세워서 얻을 수 있는 안전영역의 크기가 가장 큰 값을 출력해야한다.

이 문제 또한 원본 배열을 계속 사용해야하므로 deepcopy를 사용한다.

``` python
from collections import deque
import sys
from copy import deepcopy
input = sys.stdin.readline
```

<br>

이 문제를 풀려면 **BFS를 수행하기 전에 반드시 3개의 벽을 먼저 세워야한다.** 그러므로 BFS를 수행하기 전, makeWall이라는 함수를 만들어 벽을 먼저 세운다.

세로의 크기 N, 가로의 크기 M을 입력받는다. graph에는 N개의 줄에 지도의 정보를 입력받는다. **0은 빈칸, 1은 벽, 2는 바이러스다.**

상, 하, 좌, 우를 탐색하기 위해 dx, dy를 생성해 좌표를 저장해둔다.

ans는 벽을 세운 경우의 수들 중에 가장 안전지대가 큰 값을 저장할 변수다.

```python
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
ans = 0

makeWall(0)
```

<br>

makeWall 함수를 정의한다. 

기둥 3개가 전부 설치되면 BFS를 실행하고 리턴한다.

graph의 N과 M의 범위를 순회하면서 0(안전지대)에 벽을 세우고 makeWall의 인자를 1증가시켜 실행한다. makeWall의 인자값이 3이 되면 BFS를 실행할 것이다. 함수를 실행한 후에는 graph의 순회하고 있는 요소의 값을 0으로 되돌린다

```python
def makeWall(cnt):
    # 기둥 3개가 전부 설치되면 BFS실행
    if cnt == 3:
        BFS()
        return
    
    for i in range(N):
        for j in range(M):
            # 기둥이 없는 곳에 기둥을 세운다.
            if graph[i][j] == 0:
                graph[i][j] = 1
                makeWall(cnt+1)
                # 원래대로 되돌림(백트래킹)
                graph[i][j] = 0
```

<br>

BFS 함수를 정의한다.

deque Q를 생성하고 tmp에는 graph를 깊은 복사해서 저장한다.

복사한 tmp의 요소를 순회하면서 2(바이러스)를 만나면 해당 위치값을 Q에 추가한다.

 해당 위치값을 꺼내어 x, y에 저장하고 x, y를 상하좌우로 4방위 탐색을 한다. 

탐색하는 값이 범위를 벗어나면 건너뛰고 안전지대를 만나면 감염시키고 Q에 감염된 위치값을 추가한다.

감염이 끝나고 tmp를 한줄씩 순회하면서 감염되지 않은 안전지대의 개수를 cnt에 누적시키고 ans에 누적된 cnt와 ans중 큰 값을 저장한다.

```python
def BFS():
    global ans
    Q = deque()
    # 깊은 복사
    tmp = deepcopy(graph)
    for i in range(N):
        for j in range(M):
            if tmp[i][j] == 2:
                Q.append([i, j])


    while Q:
        x, y = Q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                Q.append([nx, ny])
    cnt = 0
    for i in range(N):
        cnt += tmp[i].count(0)
    ans = max(ans, cnt)
```

<br>

#### 전체코드

``` python
from collections import deque
import sys
from copy import deepcopy
input = sys.stdin.readline

def BFS():
    global ans
    Q = deque()
    # 깊은 복사
    tmp = deepcopy(graph)
    for i in range(N):
        for j in range(M):
            if tmp[i][j] == 2:
                Q.append([i, j])


    while Q:
        x, y = Q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                Q.append([nx, ny])
    cnt = 0
    for i in range(N):
        cnt += tmp[i].count(0)
    ans = max(ans, cnt)

def makeWall(cnt):
    # 기둥 3개가 전부 설치되면 BFS실행
    if cnt == 3:
        BFS()
        return
    
    for i in range(N):
        for j in range(M):
            # 기둥이 없는 곳에 기둥을 세운다.
            if graph[i][j] == 0:
                graph[i][j] = 1
                makeWall(cnt+1)
                # 원래대로 되돌림(백트래킹)
                graph[i][j] = 0

    

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
ans = 0

makeWall(0)
print(ans)
```

