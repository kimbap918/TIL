K = int(input())
words = input()
N = len(words) // K
board = [list(words[i:i+K]) for i in range(0, len(words), K)]
res = []

for i in range(1, len(board), 2):
    board[i].reverse()


for i in range(K):
    for j in range(N):
        res.append(board[j][i])


print(''.join(res))