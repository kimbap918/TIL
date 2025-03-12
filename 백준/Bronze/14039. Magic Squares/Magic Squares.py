square = [list(map(int, input().split())) for _ in range(4)]
flag = False
arr_row = []
arr_col = []

for i in range(4): # 0 1 2 3
    arr_row.append(sum(square[i]))
    col_sum = 0
    for j in range(4): # 0 1 2 3
        col_sum += square[j][i]
    arr_col.append(col_sum)


for i in range(3):
    if (arr_row[i] != arr_row[i+1]) or (arr_col[i] != arr_col[i+1]):
        print("not magic")
        break
else:
    print("magic")
    