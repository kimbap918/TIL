N = int(input())
seat = [["." for _ in range(20)] for _ in range(10)]

for _ in range(N):
    info = input()
    row, column = info[0], int(info[1:])
    seat[ord(row) - 65][column - 1] = "o"

for s in seat:
    print("".join(s))