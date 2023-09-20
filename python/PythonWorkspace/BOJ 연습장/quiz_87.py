T = int(input())

for i in range(1, T+1):
    square = list(map(int, input().split()))
    square.sort() 
    if square[0] != square[1]:
        print("#{} {}".format(i, square[0]))
    elif square[0] == square[1]:
        print("#{} {}".format(i, square[2])) 