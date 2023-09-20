import copy
import sys
sys.setrecursionlimit(10**6)

def move(board, direction):
    if direction == 'up':
        return transpose(move_left(transpose(board)))
    elif direction == 'down':
        return transpose(move_right(transpose(board)))
    elif direction == 'left':
        return move_left(board)
    elif direction == 'right':
        return move_right(board)

def move_left(board):
    new_board = []
    for row in board:
        new_row = merge(row)
        new_board.append(new_row + [0] * (4 - len(new_row)))
    return new_board

def move_right(board):
    new_board = []
    for row in board:
        new_row = merge(row[::-1])[::-1]
        new_board.append([0] * (4 - len(new_row)) + new_row)
    return new_board

def transpose(board):
    return [list(row) for row in zip(*board)]

def merge(row):
    new_row = []
    i = 0
    while i < len(row):
        if i + 1 < len(row) and row[i] == row[i + 1]:
            new_row.append(row[i] * 2)
            i += 2
        else:
            new_row.append(row[i])
            i += 1
    return new_row

def find_max_block(board):
    memo = {}

    def dfs(board):
        key = tuple(map(tuple, board))
        if key in memo:
            return memo[key]

        max_block = 0
        for direction in ['up', 'down', 'left', 'right']:
            new_board = move(copy.deepcopy(board), direction)
            if new_board != board:
                max_block = max(max_block, dfs(new_board))

        max_block = max(max_block, max(map(max, board)))
        memo[key] = max_block
        return max_block

    return dfs(board)

# 입력 받기
n = int(input())
board = []
for _ in range(n):
    row = list(map(int, input().split()))
    board.append(row)

# 최대 블록 값 찾기
max_block = find_max_block(board)
print(max_block)
