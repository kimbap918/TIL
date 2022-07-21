n = 210

def hansu(n):
    han_num = 0
    for i in range(1, n+1): # 1부터 주어진 n까지 
        num_list = list(map(int, str(i)))
        if i < 100:
            han_num += 1
        elif num_list[1]-num_list[0] == num_list[2]-num_list[1]:
            han_num += 1
    return han_num
    # elif 1 <= han_num and N >= han_num
print(hansu(n))