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