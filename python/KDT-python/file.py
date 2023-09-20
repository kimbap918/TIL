# 'r' : read(읽기전용)
# 'w' : write(쓰기)
# 'a' : append(추가)
with open('test.txt', 'w', encoding='utf-8') as f:
    f.write('Happy Hacking!')
    for i in range(1, 6):
        f.write(f'{i} 번째!\n')