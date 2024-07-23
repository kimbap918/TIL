def solution(name, yearning, photo):
    dict = {}
    ans = []
    
    for i in range(len(name)):
        if name[i] not in dict:
            dict[name[i]] = yearning[i]
        else:
            dict[name[i]] += yearning[i]
    # dict = {'may': 5, 'kein': 10, 'kain': 1, 'radi': 3}
    for i in photo:
        res = 0
        for j in i:
            if j in dict:
                res += dict[j]
        ans.append(res)

    return ans