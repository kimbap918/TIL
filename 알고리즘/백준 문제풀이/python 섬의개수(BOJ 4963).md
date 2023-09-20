## 파이썬 섬의개수(백준 BOJ 4963)

<br>

## 문제

정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.

![img](https://www.acmicpc.net/upload/images/island.png)

한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다. 

두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다. 지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.

<br>

## 입력

입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스의 첫째 줄에는 지도의 너비 w와 높이 h가 주어진다. w와 h는 50보다 작거나 같은 양의 정수이다.

둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다.

입력의 마지막 줄에는 0이 두 개 주어진다.

<br>

## 출력

각 테스트 케이스에 대해서, 섬의 개수를 출력한다.

<br>

## 예제 입력 1

```
1 1
0
2 2
0 1
1 0
3 2
1 1 1
1 1 1
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
5 4
1 1 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 1 1
5 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0
```

## 예제 출력 1 복사

```
0
1
1
3
1
9
```

<br>

## 📝 풀어보기

📌 sys를 import해 재귀 제한을 건다.

``` python
import sys
sys.setrecursionlimit(10000)
```

<br>

📌 무한히 반복하며 지도의 너비 `w`, 높이 `h`를 입력받는다.

만약 w, h 가 둘 다 0이라면 break한다.

지도를 입력받을 리스트 `array`, 답을 출력할 `answer`, 방문을 확인할 `visited`를 생성한다.

행 값인 h만큼 반복하며 지도의 내용을 array에 입력받고 

너비와 높이만큼 반복하며 방문한곳이 아닌곳에 answer에 dfs 함수를 실행한 값을 합산한다.

``` python
while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break

    array = []
    answer = 0
    visited = [[False] * w for _ in range(h)]

    for _ in range(h):
        array.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w):
            if not visited[i][j]:
                answer += dfs(i, j, w, h, array, visited)
    print(answer) 
```

<br>

📌 함수 dfs를 선언한다.

`visited[i][j]`거나 `array[i][j] == 0`인 경우 0을 리턴하고 visited를 True로 변경한다.

델타탐색법을 사용하여 8방위를 순회하며 nx, ny에 i,  j에 dx, dy를 합산한다. nx, ny가 범위를 벗어나지 않을때,  `array[nx][ny]`가 1이라면 dfs를 다시 호출한다.

호출할때 마다 1을 리턴한다.

``` python
def dfs(i, j, w, h, array, visited):
    if visited[i][j]:
        return 0
      
    if array[i][j] == 0:
        return 0
      
    visited[i][j] = True
    
    for dx, dy in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
        nx = i + dx
        ny = j + dy
        if 0 <= nx < h and 0 <= ny < w:
            if array[nx][ny] == 1:
                dfs(nx, ny, w, h, array, visited)
    return 1  
```

<br>

#### 전체코드

``` python
import sys
sys.setrecursionlimit(10000)

def dfs(i, j, w, h, array, visited):
    if visited[i][j]:
        return 0
      
    if array[i][j] == 0:
        return 0
      
    visited[i][j] = True
    
    for dx, dy in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
        nx = i + dx
        ny = j + dy
        if 0 <= nx < h and 0 <= ny < w:
            if array[nx][ny] == 1:
                dfs(nx, ny, w, h, array, visited)
    return 1  

while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break

    array = []
    answer = 0
    visited = [[False] * w for _ in range(h)]

    for _ in range(h):
        array.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w):
            if not visited[i][j]:
                answer += dfs(i, j, w, h, array, visited)
    print(answer) 
```

