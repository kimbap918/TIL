N = int(input())
p_list = []

for i in range(N):
  X, Y = map(int, input().split())
  p_list.append([X,Y])

for x in p_list:
    rank = 1
    for y in p_list:
        if x[0] < y[0] and x[1] < y[1]:
            rank += 1
    print(rank, end= ' ')