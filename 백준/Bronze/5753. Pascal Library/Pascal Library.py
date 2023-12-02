while True :
    lst = [*map(int, input().split())]
    if sum(lst) == 0 : break
    st = [0] * lst[0]
    for _ in range(lst[1]) :
        tmp = [*map(int, input().split())]
        for i in range(len(tmp)) :
            st[i] += tmp[i]
    if lst[1] in st : print("yes")
    else : print("no")