s = [input() for i in range(5)]
max_length = 0
 
if len(s) > max_length:
    max_length = len(s)+15
 
for i in range(max_length): # 0 1 2 3 4
    for j in range(len(s)): # 0 1 2 3 4
        if i >= len(s[j]): # 입력한 값의 길이 보다 i가 길거나 같으면
            continue # 건너뜀
        else:
            print(s[j][i], end='')