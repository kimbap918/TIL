def solution(name, yearning, photo):
    answer = []
    for i in photo: # may, kein, kain, radi
        res = 0
        for j in name:
            if j in i:
                res += yearning[name.index(j)]
        answer.append(res)
    return answer

# yearning
# [5, 10, 1, 3]

# photo
# [["may", "kein", "kain", "radi"],
#  ["may", "kein", "brin", "deny"], 
#  ["kon", "kain", "may", "coni"]]