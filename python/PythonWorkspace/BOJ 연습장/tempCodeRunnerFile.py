max_num = 0
x = 0
y = 0

for i in range(1, 10):
    num_list = list(map(int, input().split()))
    max_num_list = max(num_list)
    if max_num_list > max_num:
        max_num = max_num_list
        x = i
        y = num_list.index(max_num_list)+1

print(max_num)
print(x, y)

