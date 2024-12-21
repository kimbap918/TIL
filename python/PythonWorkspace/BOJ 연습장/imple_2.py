input_data = input()
row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a'))+1
steps = [(2, -1), (-2, -1), (2, 1), (-2, 1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
cnt = 0

for step in steps:
    nr = row + step[0]
    nc = col + step[1]

    if nr >= 1 and nr <= 8 and nc >= 1 and nc <= 8:
        cnt += 1


print(cnt)