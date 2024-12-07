import sys

board = dict()

row = ['1', '2', '3', '4', '5', '6', '7', '8']
col = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

number = 0
color = 'black'

for r in range(8):
    
    for c in range(8):
        coordinate = col[c] + row[r]
        number += 1

        if r % 2 == 0:
            
            if number % 2 == 0:
                color = 'white'
            else:
                color = 'black'
        else:
            
            if number % 2 == 0:
                color = 'black'
            else:
                color = 'white'

        board[coordinate] = color
        board[str(number)] = color

T = int(sys.stdin.readline())

for _ in range(T):
    notation_1, notation_2 = sys.stdin.readline().rstrip().split()

    if board[notation_1] == board[notation_2]:
        print('YES')
    else:
        print('NO')