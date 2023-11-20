while 1:
    li = sorted(list(map(int, input().split())))
    if sum(li) == 0:
        break
    li = li[1:-1]
    res = sum(li)/4
    print(res if sum(li)%4 else int(res))