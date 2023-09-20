## 파이썬 그림(백준 BOJ 1926)

<br>

BFS 사용하기

## 문제

어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라. 단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자. 가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다. 그림의 넓이란 그림에 포함된 1의 개수이다.

<br>

## 입력

첫째 줄에 도화지의 세로 크기 n(1 ≤ n ≤ 500)과 가로 크기 m(1 ≤ m ≤ 500)이 차례로 주어진다. 두 번째 줄부터 n+1 줄 까지 그림의 정보가 주어진다. (단 그림의 정보는 0과 1이 공백을 두고 주어지며, 0은 색칠이 안된 부분, 1은 색칠이 된 부분을 의미한다)

<br>

## 출력

첫째 줄에는 그림의 개수, 둘째 줄에는 그 중 가장 넓은 그림의 넓이를 출력하여라. 단, 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0이다.

<br>

## 예제 입력 1 

```
6 5
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1
```

## 예제 출력 1

```
4
9
```

<br>

## 📝 풀어보기 

📌 BFS를 사용하기 위해 deque를 import했다.

도화지의 세로크기 `n`, 가로크기 `m` 을 각각 입력받고 세로크기 범위만큼 리스트에 그림을 그린다.

상하좌우 델타탐색을 위해 `dx` `dy` 를 생성한다.

``` python
from collections import deque
from pprint import pprint
# 도화지의 세로크기 n, 가로크기 m 
n, m = map(int, input().split())
# 세로크기 범위만큼 반복하며 리스트에 그림을 그림
graph = [list(map(int, input().split())) for _ in range(n)]
# 상하좌우 델타탐색
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
```

<br>

📌 요구사항이 `그림의 개수` 와 `가장 큰 그림의 면적` 이므로 그림의 면적을 구할 리스트를 생성하고 세로와 가로 크기만큼 반복하면서 그래프의 값이 1이면 paint에 bfs 함수를 실행한다.

``` python
# 그림의 면적을 구할 리스트 
paint = []
# 세로크기
for i in range(n):
    # 가로크기
    for j in range(m):
        # 그래프의 값이 1이면 
        if graph[i][j] == 1:
            # paint에 bfs실행한 값 추가 
            paint.append(bfs(graph, i, j))
```

<br>

📌 deque를 하나 생성하고 들어온 a,b값을 추가해준다.

그림의 들어온 좌표에 해당하는 값을 0으로 바꿔주고 count를 1로 초기화한다.

큐가 빌때까지 deque의 왼쪽에서 빼낸 값을 x, y에 각각 저장하고 델타탐색을 실행해서 x, y에 상하좌우 좌표값을 넣어서 값이 범위를 벗어나면 건너뛴다.

그래프의 델타탐색 값이 1이라면 0으로 바꿔주고 좌표값을 deque에 넣어준다. 카운트 1을 증가시키고 리턴해주면서 마무리한다.

``` python
# BFS 실행 
def bfs(graph, a, b):
    queue = deque()
    queue.append((a, b)) # queue에 들어온 a, b값 추가 
    graph[a][b] = 0 # 들어온 좌표의 값을 0으로 만든다. 
    count = 1
    
    while queue: # 큐가 빌때까지 
        # x, y = 큐의 왼쪽을 빼낸 값
        x, y = queue.popleft() 
        # 델타탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # nx ny가 범위 내에 없으면 건너뜀
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 그래프의 nx ny 좌표값이 1 이면 0으로 만들고  
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                # queue에 좌표값 append 
                queue.append((nx, ny))
                # count 증가
                count += 1
    return count
```

<br>

#### 전체 코드

``` python
from collections import deque
from pprint import pprint
# 도화지의 세로크기 n, 가로크기 m 
n, m = map(int, input().split())
# 세로크기 범위만큼 반복하며 리스트에 그림을 그림
graph = [list(map(int, input().split())) for _ in range(n)]
# 상하좌우 델타탐색
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# BFS 실행 
def bfs(graph, a, b):
    queue = deque()
    queue.append((a, b)) # queue에 들어온 a, b값 추가 
    graph[a][b] = 0 # 들어온 좌표의 값을 0으로 만든다. 
    count = 1
    
    while queue: # 큐가 빌때까지 
        # x, y = 큐의 왼쪽을 빼낸 값
        x, y = queue.popleft() 
        # 델타탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # nx ny가 범위 내에 없으면 건너뜀
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 그래프의 nx ny 좌표값이 1 이면 0으로 만들고  
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                # queue에 좌표값 append 
                queue.append((nx, ny))
                # count 증가
                count += 1
    return count

# 그림의 면적을 구할 리스트 
paint = []
# 세로크기
for i in range(n):
    # 가로크기
    for j in range(m):
        # 그래프의 값이 1이면 
        if graph[i][j] == 1:
            # paint에 bfs실행한 값 추가 
            paint.append(bfs(graph, i, j))
 
 
if len(paint) == 0:
    print(len(paint))
    print(0)
else:
    print(len(paint))
    print(max(paint))
```

