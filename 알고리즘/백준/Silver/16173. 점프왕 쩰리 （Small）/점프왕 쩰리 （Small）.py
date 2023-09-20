import sys
from collections import deque
input = sys.stdin.readline


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dx = [1, 0]
dy = [0, 1]


def BFS():
    Q = deque([[0, 0]])


    while Q:
        x, y = Q.popleft()
        if board[x][y] == -1:
            print("HaruHaru")
            exit(0)
        
        dist = board[x][y] 

        for i in range(2):
            nx = x + dx[i] * dist
            ny = y + dy[i] * dist

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = True
                Q.append([nx, ny])

    print("Hing")

BFS()                
