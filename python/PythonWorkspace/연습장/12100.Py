import sys
from copy import deepcopy

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = 0

def move(board, direction):
    if direction == 0:  # 왼쪽으로 이동
        for i in range(N):
            cur = 0
            for j in range(1, N):
                if board[i][j] != 0:
                    tmp = board[i][j]
                    board[i][j] = 0

                    if board[i][cur] == 0:
                        board[i][cur] = tmp
                    elif board[i][cur] == tmp:
                        board[i][cur] *= 2
                        cur += 1
                    else:
                        cur += 1
                        board[i][cur] = tmp
    elif direction == 1:  # 오른쪽으로 이동
        for i in range(N):
            cur = N - 1
            for j in range(N - 2, -1, -1):
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
    elif direction == 2:  # 위로 이동
        for j in range(N):
            cur = 0
            for i in range(1, N):
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
    elif direction == 3:  # 아래로 이동
        for j in range(N):
            cur = N - 1
            for i in range(N - 2, -1, -1):
                if board[i][j] != 0:
                    tmp = board[i][j]
                    board[i][j] = 0

                    if board[cur][j] == 0:
                        board[cur][j] = tmp
                    elif board[cur][j] == tmp:
                        board[cur][j] *= 2
                        cur -= 1
                    else:
                        cur -= 1
                        board[cur][j] = tmp

    return board

def dfs(board, count):
    global answer
    if count == 10:
        for i in range(N):
            for j in range(N):
                answer = max(answer, board[i][j])
        return

    for direction in range(4):
        tmp_board = deepcopy(board)
        new_board = move(tmp_board, direction)
        dfs(new_board, count + 1)

dfs(board, 0)
print(answer)
