import sys
from collections import deque
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline


# def DFS(x, y):
#     if 0 <= x < N and 0 <= y < N and visited[x][y] == False:
#         visited[x][y] = True        

#         DFS(x+board[x][y], y)
#         DFS(x, y+board[x][y])
#     else:
#         return

#     if board[x][y] == -1:
#         visited[x][y] = True
#         return



N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]



# DFS(0, 0)
        
# if visited[-1][-1] == True:
#     print("HaruHaru")
# else:
#     print("Hing")
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
