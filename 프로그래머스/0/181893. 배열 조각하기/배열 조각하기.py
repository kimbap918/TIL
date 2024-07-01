def solution(arr, query):
    for idx, query in enumerate(query):
        print(idx, query)
        if idx % 2 == 0:
            arr = arr[:query+1]
        else:
            arr = arr[query:]
    return arr


# [0, 1, 2, 3, 4, 5]
# 4 -> 4 : [0, 1, 2, 3, 4]
# 1 -> 1 : [1, 2, 3, 4]
# 2 -> 2 : [1, 2, 3]
