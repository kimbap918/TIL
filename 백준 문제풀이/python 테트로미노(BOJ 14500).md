

## 파이썬 테트로미노(BOJ 14500)

<br>

## 문제

폴리오미노란 크기가 1×1인 정사각형을 여러 개 이어서 붙인 도형이며, 다음과 같은 조건을 만족해야 한다.

- 정사각형은 서로 겹치면 안 된다.
- 도형은 모두 연결되어 있어야 한다.
- 정사각형의 변끼리 연결되어 있어야 한다. 즉, 꼭짓점과 꼭짓점만 맞닿아 있으면 안 된다.

정사각형 4개를 이어 붙인 폴리오미노는 테트로미노라고 하며, 다음과 같은 5가지가 있다.

[![img](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/14500/1.png)](https://commons.wikimedia.org/wiki/File:All_5_free_tetrominoes.svg)

아름이는 크기가 N×M인 종이 위에 테트로미노 하나를 놓으려고 한다. 종이는 1×1 크기의 칸으로 나누어져 있으며, 각각의 칸에는 정수가 하나 쓰여 있다.

테트로미노 하나를 적절히 놓아서 테트로미노가 놓인 칸에 쓰여 있는 수들의 합을 최대로 하는 프로그램을 작성하시오.

테트로미노는 반드시 한 정사각형이 정확히 하나의 칸을 포함하도록 놓아야 하며, 회전이나 대칭을 시켜도 된다.

<br>

## 입력

첫째 줄에 종이의 세로 크기 N과 가로 크기 M이 주어진다. (4 ≤ N, M ≤ 500)

둘째 줄부터 N개의 줄에 종이에 쓰여 있는 수가 주어진다. i번째 줄의 j번째 수는 위에서부터 i번째 칸, 왼쪽에서부터 j번째 칸에 쓰여 있는 수이다. 입력으로 주어지는 수는 1,000을 넘지 않는 자연수이다.

<br>

## 출력

첫째 줄에 테트로미노가 놓인 칸에 쓰인 수들의 합의 최댓값을 출력한다.

## 예제 입력 1 

```
5 5
1 2 3 4 5
5 4 3 2 1
2 3 4 5 6
6 5 4 3 2
1 2 1 2 1
```

## 예제 출력 1 

```
19
```

## 예제 입력 2 

```
4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
```

## 예제 출력 2 

```
20
```

## 예제 입력 3 

```
4 10
1 2 1 2 1 2 1 2 1 2
2 1 2 1 2 1 2 1 2 1
1 2 1 2 1 2 1 2 1 2
2 1 2 1 2 1 2 1 2 1
```

## 예제 출력 3 

```
7
```

<br>

## 📝 풀어보기

DFS 문제. 테트로미노의 모양들은 DFS로 탐색하다 보면 자연스럽게 탐색이 되지만, ㅜ 모양은 따로 처리를 해줘야한다.

<br>

세로 크기 N, 가로 크기 M을 입력받는다.

board에는 종이에 쓰여진 수들을 입력받아 저장한다. visited에는 탐색 시 해당 종이의 요소를 탐색했는지 확인하기 위해 사용한다.

max_val에는 종이에 적힌 숫자 중 가장 큰 값을 저장해둔다. ans는 탐색 후 가장 큰 값을 저장한다.

dx, dy는 해당 탐색 좌표 부터 상하좌우를 탐색하기 위한 좌표를 저장한다.

``` python
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
max_val = max(map(max, board))
ans = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
```

<br>

종이의 가로, 세로를 탐색하면서 방문한곳의 visited값을 True로 바꿔주고 DFS를 수행한 후 다시 해당 위치의 방문 여부를 False로 돌려놓는다.

``` python
for i in range(N):
    for j in range(M):
        visited[i][j] = True
        DFS(i, j, 1, board[i][j])
        visited[i][j] = False

print(ans)
```

<br>

DFS를 수행한다. 인자는 y, x좌표, depth(깊이), s(현재 탐색한 위치의 값)다.

` s + max_val * (4-depth)`는 남아있는 블럭들이 최대로 가질 수 있는 값이다. 이 값이 최대라고 해도 ans보다 작거나 같다면 함수를 조기종료한다.

depth가 4보다 크거나 같으면 테트로미노다. ans가 s보다 작다면, ans를 s로 갱신한다.

depth가 4보다 작으면 상하좌우 탐색을 한다. 종이의 범위를 벗어나지 않고, 방문하지 않은 범위에서 해당 방문위치를 True로 바꾸고, depth를 1 증가시키고, s에 board의 탐색 위치값을 더해 DFS를 수행한다. 

depth가 2일때는 시작점을 자기자신으로 하는(x, y) DFS를 호출한다. 테트로미노 중 `ㅜ` 모양은 depth 2에서 자기자신을 시작점으로 해서 DFS를 수행해야 해당 모양으로 탐색이 가능하다.

```python
def DFS(y, x, depth, s):
    global ans
    # 남은 블럭이 모두 최댓값이라 해도 현재의 최대를 넘길수 없을때 조기종료 해버림
    if s + max_val * (4-depth) <= ans:
        return
    if depth >= 4:
        if ans < s:
            ans = s
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                # dfs수행중에 2까지일때 시작점을 자기자신으로 하는 dfs를 호출함
                # ㅜ 모양은 DFS처리 중에 깊이가 2일때 다시 자기자신을 시작점으로 dfs를 호출해야한다.
                if depth == 2:
                    visited[ny][nx] = True
                    DFS(y, x, depth+1, s+board[ny][nx])
                    visited[ny][nx] = False
                
                visited[ny][nx] = True
                DFS(ny, nx, depth+1, s+board[ny][nx])
                visited[ny][nx] = False
```

<br>

#### 전체코드

``` python
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
max_val = max(map(max, board))
ans = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def DFS(y, x, depth, s):
    global ans
    # 남은 블럭이 모두 최댓값이라 해도 현재의 최대를 넘길수 없을때 조기종료 해버림
    if s + max_val * (4-depth) <= ans:
        return
    if depth >= 4:
        if ans < s:
            ans = s
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                # dfs수행중에 2까지일때 시작점을 자기자신으로 하는 dfs를 호출함
                # ㅗ 모양은 DFS처리 중에 깊이가 2일때 다시 자기자신을 시작점으로 dfs를 호출해야한다.
                if depth == 2:
                    visited[ny][nx] = True
                    DFS(y, x, depth+1, s+board[ny][nx])
                    visited[ny][nx] = False
                
                visited[ny][nx] = True
                DFS(ny, nx, depth+1, s+board[ny][nx])
                visited[ny][nx] = False

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        DFS(i, j, 1, board[i][j])
        visited[i][j] = False

print(ans)
```

