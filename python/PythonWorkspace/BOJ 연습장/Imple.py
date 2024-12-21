from pprint import pprint as pp

N = int(input())
board = list([(j ,i) for i in range(N)] for j in range(N))
command = list(map(str, input().split()))
x, y = 1, 1
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
move = ['D', 'U', 'L', 'R']


for com in command:
    for i in range(len(move)):
        if com == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 1 or ny < 1 or nx > N or ny > N:
                continue
            x, y = nx, ny


print(x, y)