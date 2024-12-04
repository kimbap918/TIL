N = int(input())
board = [input() for _ in range(N)]
dx = [0, 0, 1, -1, -1, 1, -1, 1]
dy = [1, -1, 0, 0, -1, 1, 1, -1]

# 결과 배열 초기화
res = [['0'] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if board[i][j].isdigit():
            # 지뢰가 있는 칸은 '*'로 표시
            res[i][j] = "*"
            continue

        count = 0
        for d in range(8):
            ni, nj = i + dx[d], j + dy[d]
            if 0 <= ni < N and 0 <= nj < N and board[ni][nj].isdigit():
                count += int(board[ni][nj])

        # 지뢰 개수 10 이상인 경우 'M' 표시
        if count >= 10:
            res[i][j] = "M"
        else:
            res[i][j] = str(count)

# 결과 출력
for row in res:
    print(''.join(row))
