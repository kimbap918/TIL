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
    graph[a][b] = 0 
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