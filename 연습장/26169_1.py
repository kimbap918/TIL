from collections import deque

board = [list(map(int, input().split())) for _ in range(5)]
y, x = map(int, input().split())
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
eat = 0
result = 0

def BFS(y, x):
    global eat
    global result
    Q = deque([[y, x, 0]])  # 이동 횟수도 큐에 함께 저장
    visited = [[False] * 5 for _ in range(5)]  # 방문 여부를 저장하는 2차원 리스트

    while Q:
        col, row, move = Q.popleft()
        if board[col][row] == 1:
            eat += 1
        if eat >= 2:
            result = 1
            return

        if move > 2:
            continue

        for i in range(4):
            ny = col + dy[i]
            nx = row + dx[i]
            if 0 <= ny < 5 and 0 <= nx < 5 and board[ny][nx] != -1 and not visited[ny][nx]:
                if board[ny][nx] == 1:
                    eat += 1
                    Q.append([ny, nx, move + 1])
                    visited[ny][nx] = True
                elif board[ny][nx] == 0:
                    Q.append([ny, nx, move + 1])
                    visited[ny][nx] = True

        visited[col][row] = True

# 초기 위치에 장애물로 설정하여 학생이 해당 위치를 떠났을 때 장애물로 변경되게 함
board[y][x] = -1
BFS(y, x)
print(result)
