import sys
from copy import deepcopy
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0
# 동, 서, 남, 북으로 이동

def move(board, dir):
    if dir == 0: # 방향이 왼쪽
        for i in range(N):
            cur = 0
            for j in range(1, N):
                if board[i][j] != 0: # 0이 아닌값이 있을경우
                    tmp = board[i][j]
                    board[i][j] = 0 # 합쳐질 것이기 때문에 비운다.

                    if board[i][cur] == 0: # 비어있는 공간이면
                        board[i][cur] = tmp # 값을 옮긴다.
                    
                    elif board[i][cur] == tmp: # 값이 같으면
                        board[i][cur] *= 2 # 합친다
                        cur += 1
                    
                    else: # 비어있지 않고, 다른 값이면
                        cur += 1
                        board[i][cur] = tmp

    elif dir == 1: # 방향이 오른쪽
        for i in range(N):
            cur = N-1
            for j in range(N-1, -1, -1):
                if board[i][j] != 0:
                    tmp = board[i][j]
                    board[i][j] = 0

                    if board[i][cur] == 0:
                        board[i][cur] = tmp

                    elif board[i][cur] == tmp:
                        board[i][cur] *= 2
                        cur -= 1
                    
                    else:
                        cur -= 1
                        board[i][cur] = tmp

    elif dir == 2: # 방향이 위
        for j in range(N):
            cur = 0
            for i in range(N):
                if board[i][j] != 0: 
                    tmp = board[i][j]
                    board[i][j] = 0

                    if board[cur][j] == 0: 
                        board[cur][j] = tmp

                    elif board[cur][j] == tmp:
                        board[cur][j] *= 2
                        cur += 1

                    else:
                        cur += 1
                        board[cur][j] = tmp


    else:
        for i in range(N):
            cur = N-1
            for j in range(N-1, -1, -1):
                if board[j][i] != 0:
                    tmp = board[j][i]
                    board[j][i] = 0

                    if board[cur][i] == 0:
                        board[cur][i] = tmp

                    elif board[cur][i] == tmp:
                        board[cur][i] *= 2
                        cur -= 1
                    
                    else:
                        cur -= 1
                        board[cur][i] = tmp

    return board

def DFS(board, cnt):
    global ans
    if cnt == 5:
        for i in range(N):
            for j in range(N):
                ans = max(ans, board[i][j])
        return
    
    # 위, 왼쪽, 아래, 오른쪽
    for i in range(4):
        tmp = move(deepcopy(board), i)
        DFS(tmp, cnt+1)

DFS(board, 0)
print(ans)