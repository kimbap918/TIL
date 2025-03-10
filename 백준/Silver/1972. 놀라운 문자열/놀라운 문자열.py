import sys
input = sys.stdin.readline

# arr = []

while True:
    word = input().rstrip()
    if word == '*':
        break

    N = len(word)
    dict = {i: [] for i in range(N-1)}


    for k in range(1, N): # 1, 2, 3
        for i in range(N-k): # 0 1 2, 0 1, 0
            j = i + k 
            dict[k-1].append(word[i]+word[j])

    
    # print(dict)
    # ZGBG =ZG(01), GB(12), BG(23) / ZB(02), GG(13) / ZG(03) 

    flag = True

    for k, v in dict.items():
        # print(v)
        if len(v) != len(set(v)):
            flag = False
            break

    if flag == True:
        print(f'{word} is surprising.')
    else:
        print(f'{word} is NOT surprising.')
    