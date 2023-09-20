import sys

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = 0

def find_max_block():
    max_block = 0
    for i in range(N):
        for j in range(N):
            max_block = max(max_block, board[i][j])
    return max_block

def move(direction):
    if direction == 0:  # 위로 이동
        for j in range(N):
            idx = 0
            for i in range(1, N):
                if board[i][j] != 0:
                    if board[i][j] == board[idx][j]:
                        board[idx][j] *= 2
                        board[i][j] = 0
                    else:
                        idx += 1
                        board[idx][j] = board[i][j]
                        if i != idx:
                            board[i][j] = 0
    elif direction == 1:  # 오른쪽으로 이동
        for i in range(N):
            idx = N - 1
            for j in range(N - 2, -1, -1):
                if board[i][j] != 0:
                    if board[i][j] == board[i][idx]:
                        board[i][idx] *= 2
                        board[i][j] = 0
                    else:
                        idx -= 1
                        board[i][idx] = board[i][j]
                        if j != idx:
                            board[i][j] = 0
    elif direction == 2:  # 아래로 이동
        for j in range(N):
            idx = N - 1
            for i in range(N - 2, -1, -1):
                if board[i][j] != 0:
                    if board[i][j] == board[idx][j]:
                        board[idx][j] *= 2
                        board[i][j] = 0
                    else:
                        idx -= 1
                        board[idx][j] = board[i][j]
                        if i != idx:
                            board[i][j] = 0
    elif direction == 3:  # 왼쪽으로 이동
        for i in range(N):
            idx = 0
            for j in range(1, N):
                if board[i][j] != 0:
                    if board[i][j] == board[i][idx]:
                        board[i][idx] *= 2
                        board[i][j] = 0
                    else:
                        idx += 1
                        board[i][idx] = board[i][j]
                        if j != idx:
                            board[i][j] = 0

def dfs(count):
    global answer
    if count == 10:
        answer = max(answer, find_max_block())
        return

    # 현재 상태 저장
    tmp_board = [row[:] for row in board]

    for direction in range(4):
        move(direction)
        dfs(count + 1)
        # 이동 후 상태를 원래대로 복원
        board = [row[:] for row in tmp_board]

dfs(0)
print(answer)
