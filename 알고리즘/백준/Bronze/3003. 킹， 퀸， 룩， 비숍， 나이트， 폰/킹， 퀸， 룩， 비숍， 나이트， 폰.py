# 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개
# 1 1 2 2 2 8

chess = [1, 1, 2, 2, 2, 8]
chess_input = list(map(int, input().split())) # 0 1 2 2 2 7

for i in range(len(chess)):
    result = chess[i] - chess_input[i]
    print(result, end = ' ')

