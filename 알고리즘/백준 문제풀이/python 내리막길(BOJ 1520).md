

## 파이썬 내리막길(BOJ 1520)

<br>

## 문제

여행을 떠난 세준이는 지도를 하나 구하였다. 이 지도는 아래 그림과 같이 직사각형 모양이며 여러 칸으로 나뉘어져 있다. 한 칸은 한 지점을 나타내는데 각 칸에는 그 지점의 높이가 쓰여 있으며, 각 지점 사이의 이동은 지도에서 상하좌우 이웃한 곳끼리만 가능하다.

![img](https://upload.acmicpc.net/0e11f3db-35d2-4b01-9aa0-9a39252f05be/-/preview/)

현재 제일 왼쪽 위 칸이 나타내는 지점에 있는 세준이는 제일 오른쪽 아래 칸이 나타내는 지점으로 가려고 한다. 그런데 가능한 힘을 적게 들이고 싶어 항상 높이가 더 낮은 지점으로만 이동하여 목표 지점까지 가고자 한다. 위와 같은 지도에서는 다음과 같은 세 가지 경로가 가능하다.

![img](https://upload.acmicpc.net/917d0418-35db-4081-9f62-69a2cc78721e/-/preview/) ![img](https://upload.acmicpc.net/1ed5b78d-a4a1-49c0-8c23-12a12e2937e1/-/preview/) ![img](https://upload.acmicpc.net/e57e7ef0-cc56-4340-ba5f-b22af1789f63/-/preview/)

지도가 주어질 때 이와 같이 제일 왼쪽 위 지점에서 출발하여 제일 오른쪽 아래 지점까지 항상 내리막길로만 이동하는 경로의 개수를 구하는 프로그램을 작성하시오.

<br>

## 입력

첫째 줄에는 지도의 세로의 크기 M과 가로의 크기 N이 빈칸을 사이에 두고 주어진다. 이어 다음 M개 줄에 걸쳐 한 줄에 N개씩 위에서부터 차례로 각 지점의 높이가 빈 칸을 사이에 두고 주어진다. M과 N은 각각 500이하의 자연수이고, 각 지점의 높이는 10000이하의 자연수이다.

<br>

## 출력

첫째 줄에 이동 가능한 경로의 수 H를 출력한다. 모든 입력에 대하여 H는 10억 이하의 음이 아닌 정수이다.

<br>

## 예제 입력 1

```
4 5
50 45 37 32 30
35 50 40 20 25
30 30 25 17 28
27 24 22 15 10
```

## 예제 출력 1

```
3
```

<br>

## 📝 풀어보기

``` python
```



``` python
import sys
input = sys.stdin.readline

def dfs(x, y):
    # 목적지 도착시 1을 추가하여 이동경로에 모두 추가
    if x == M-1 and y == N-1:
        return 1
    
    # 방문하지 않은 곳을 방문처리
    if dp[x][y] == -1:
        dp[x][y] = 0
        
        # 4방위 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 탐색 범위가 보드를 초과하지 않고
            if 0 <= nx < M and 0 <= ny < N:
                # 현재 위치가 탐색위치보다 높은곳에 있다면(내리막길)
                if board[x][y] > board[nx][ny]:
                    # dp[x][y]에 탐색위치의 dfs를 추가
                    dp[x][y] += dfs(nx, ny)
    
    return dp[x][y]

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
dp = [[-1 for _ in range(N)] for _ in range(M)]

print(dfs(0, 0))

```

