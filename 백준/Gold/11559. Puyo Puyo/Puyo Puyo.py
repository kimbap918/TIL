board = [list(input()) for _ in range(12)]  # 12x6 보드 입력
dx = [0, 0, 1, -1]  # 좌우
dy = [1, -1, 0, 0]  # 상하
words = ['R', 'G', 'B', 'P', 'Y']
result = 0

def dfs(word, y, x, visited):
    stack = [(y, x)]
    temp = [(y, x)]
    visited[y][x] = True

    while stack:
        cy, cx = stack.pop()
        for i in range(4):  # 4방향 탐색
            ny, nx = cy + dy[i], cx + dx[i]
            if 0 <= ny < 12 and 0 <= nx < 6 and not visited[ny][nx] and board[ny][nx] == word:
                visited[ny][nx] = True
                stack.append((ny, nx))
                temp.append((ny, nx))

    if len(temp) >= 4:  # 4개 이상 연결된 경우 제거
        for py, px in temp:
            board[py][px] = "."
        return True  # 터진 블록이 있음
    return False

def apply_gravity():
    for x in range(6):  # 열 기준으로 적용
        temp = []  # 현재 열에서 블록을 모으기
        for y in range(11, -1, -1):  # 아래에서 위로 검사
            if board[y][x] != ".":
                temp.append(board[y][x])
        
        # 새롭게 블록을 아래로 내리기
        for y in range(11, -1, -1):
            if temp:
                board[y][x] = temp.pop(0)  # 저장한 블록을 순서대로 채움
            else:
                board[y][x] = "."  # 나머지는 빈 칸

def play_game():
    global result
    while True:
        visited = [[False] * 6 for _ in range(12)]
        found = False

        # 블록 터뜨리기
        for i in range(12):
            for j in range(6):
                if board[i][j] in words and not visited[i][j]:
                    if dfs(board[i][j], i, j, visited):
                        found = True

        if not found:
            break  # 더 이상 터질 블록이 없으면 종료

        result += 1  # 연쇄 횟수 증가
        apply_gravity()  # 블록을 아래로 내리기

play_game()
print(result)  # 연쇄 횟수 출력