## 파이썬 스도쿠(백준 BOJ 2580)

<br>

## 문제

스도쿠는 18세기 스위스 수학자가 만든 '라틴 사각형'이랑 퍼즐에서 유래한 것으로 현재 많은 인기를 누리고 있다. 이 게임은 아래 그림과 같이 가로, 세로 각각 9개씩 총 81개의 작은 칸으로 이루어진 정사각형 판 위에서 이뤄지는데, 게임 시작 전 일부 칸에는 1부터 9까지의 숫자 중 하나가 쓰여 있다.

![img](https://www.acmicpc.net/problem/2580)

나머지 빈 칸을 채우는 방식은 다음과 같다.

1. 각각의 가로줄과 세로줄에는 1부터 9까지의 숫자가 한 번씩만 나타나야 한다.
2. 굵은 선으로 구분되어 있는 3x3 정사각형 안에도 1부터 9까지의 숫자가 한 번씩만 나타나야 한다.

위의 예의 경우, 첫째 줄에는 1을 제외한 나머지 2부터 9까지의 숫자들이 이미 나타나 있으므로 첫째 줄 빈칸에는 1이 들어가야 한다.

![img](https://www.acmicpc.net/problem/2580)

또한 위쪽 가운데 위치한 3x3 정사각형의 경우에는 3을 제외한 나머지 숫자들이 이미 쓰여있으므로 가운데 빈 칸에는 3이 들어가야 한다.

![img](https://www.acmicpc.net/problem/2580)

이와 같이 빈 칸을 차례로 채워 가면 다음과 같은 최종 결과를 얻을 수 있다.

![img](https://www.acmicpc.net/problem/2580)

게임 시작 전 스도쿠 판에 쓰여 있는 숫자들의 정보가 주어질 때 모든 빈 칸이 채워진 최종 모습을 출력하는 프로그램을 작성하시오.

## 입력

아홉 줄에 걸쳐 한 줄에 9개씩 게임 시작 전 스도쿠판 각 줄에 쓰여 있는 숫자가 한 칸씩 띄워서 차례로 주어진다. 스도쿠 판의 빈 칸의 경우에는 0이 주어진다. 스도쿠 판을 규칙대로 채울 수 없는 경우의 입력은 주어지지 않는다.

## 출력

모든 빈 칸이 채워진 스도쿠 판의 최종 모습을 아홉 줄에 걸쳐 한 줄에 9개씩 한 칸씩 띄워서 출력한다.

스도쿠 판을 채우는 방법이 여럿인 경우는 그 중 하나만을 출력한다.

## 제한

- 12095번 문제에 있는 소스로 풀 수 있는 입력만 주어진다.
  - C++14: 80ms
  - Java: 292ms
  - PyPy3: 1172ms

## 예제 입력 1

```
0 3 5 4 6 9 2 7 8
7 8 2 1 0 5 6 0 9
0 6 0 2 7 8 1 3 5
3 2 1 0 4 6 8 9 7
8 0 4 9 1 3 5 0 6
5 9 6 8 2 0 4 1 3
9 1 7 6 5 2 0 8 0
6 0 3 7 0 1 9 5 2
2 5 8 3 9 4 7 6 0
```

## 예제 출력 1

```
1 3 5 4 6 9 2 7 8
7 8 2 1 3 5 6 4 9
4 6 9 2 7 8 1 3 5
3 2 1 5 4 6 8 9 7
8 7 4 9 1 3 5 2 6
5 9 6 8 2 7 4 1 3
9 1 7 6 5 2 3 8 4
6 4 3 7 8 1 9 5 2
2 5 8 3 9 4 7 6 1
```

<br>

## 📝 풀어보기

``` python
import sys
graph = []
blank = []

input = sys.stdin.readline

# 1. 먼저 문제에서 빈 칸은 0으로 주어지기 때문에 graph의 0인칸의 위치정보(x, y)를 blank 리스트에 넣어준다.
# 2. 첫 번째 빈칸에 1~9까지의 수 중 넣을 수 있는 수를 넣는다. 넣을 수 있는 수는 빈칸의 행,열,3x3정사각형에 없는 수임을 확인하자. 확인이 되면 그 빈칸에는 그 수를 넣어준다.
# 3. 그 다음 빈칸에 대해서도 같은 방법을 수행한다.
# 4. 마지막 빈칸까지 채우면 스도쿠를 완성하므로 맵을 출력한다.

for i in range(9): # graph에 스도쿠의 입력값을 넣어준다.
    graph.append(list(map(int, input().rstrip().split())))

    # 0 3 5 4 6 9 2 7 8
    # 7 8 2 1 0 5 6 0 9
    # 0 6 0 2 7 8 1 3 5
    # 3 2 1 0 4 6 8 9 7
    # 8 0 4 9 1 3 5 0 6
    # 5 9 6 8 2 0 4 1 3
    # 9 1 7 6 5 2 0 8 0
    # 6 0 3 7 0 1 9 5 2
    # 2 5 8 3 9 4 7 6 0

for i in range(9): # 스도쿠의 값 중 빈칸인 0 값을 찾아서 위치값을 blank에 넣어준다.
    for j in range(9):
        if graph[i][j] == 0:
            blank.append((i, j))

def checkRow(x, a): # 열에서 1~9중 겹치는 숫자가 있는지 확인, 겹치는 숫자가 있다면 False를 반환
    for i in range(9):
        if a == graph[x][i]:
            return False
    return True

def checkCol(y, a): # 행에서 1~9중 겹치는 숫자가 있는지 확인, 겹치는 숫자가 있다면 False를 반환
    for i in range(9):
        if a == graph[i][y]:
            return False
    return True

def checkRect(x, y, a): # 3*3 정사각형 안에서 1~9의 수 중 겹치는 수가 있는지를 확인, 있다면 False를 반환
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if a == graph[nx+i][ny+j]:
                return False
    return True


def dfs(idx):
    if idx == len(blank): # 인덱스가 blank위치정보의 길이와 같아지면 종료, graph의 값들을 전부 출력함
        for i in range(9):
            print(*graph[i])
        exit(0)

    for i in range(1, 10):
        # print(idx)
        x = blank[idx][0]
        y = blank[idx][1]

        if checkRow(x, i) and checkCol(y, i) and checkRect(x, y, i): # 열, 행, 정사각형이 모두 참 값이면 
            graph[x][y] = i # 그래프의 해당 값을 i로 변경
            dfs(idx+1) # idx 1 증가
            graph[x][y] = 0 # 초기화

dfs(0)
```

