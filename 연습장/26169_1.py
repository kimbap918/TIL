def backtrack(board, row, col, moves, apples):
    if apples >= 2:  # 사과를 2개 이상 먹은 경우
        return True

    if moves == 3:  # 이동 횟수가 3번을 초과한 경우
        return False

    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # 상하좌우 방향

    for dx, dy in directions:
        new_row = row + dx
        new_col = col + dy

        if 0 <= new_row < 5 and 0 <= new_col < 5 and board[new_row][new_col] != -1:
            eaten = 0

            if board[new_row][new_col] == 1:  # 사과가 있는 경우
                eaten = 1
                board[new_row][new_col] = 0  # 사과를 먹었으므로 해당 위치를 빈칸으로 변경

            board[row][col] = -1  # 현재 위치를 장애물로 변경
            if backtrack(board, new_row, new_col, moves + 1, apples + eaten):
                return True
            board[row][col] = 0  # 백트래킹: 현재 위치를 원래대로 복구

            if board[new_row][new_col] == 1:  # 사과를 먹은 경우 원래대로 되돌려줌
                board[new_row][new_col] = 1

    return False


board = []
for _ in range(5):
    row = list(map(int, input().split()))
    board.append(row)

r, c = map(int, input().split())

if backtrack(board, r, c, 0, 0):
    print(1)
else:
    print(0)
