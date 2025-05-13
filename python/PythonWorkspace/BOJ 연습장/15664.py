N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
res = []

def dfs(start, depth):
    if len(res) == M:
        print(' '.join(map(str, res)))
        return

    prev = -1
    for i in range(start, N):
        if prev != arr[i]: 
            res.append(arr[i])
            prev = arr[i]
            dfs(i+1, depth+1)
            res.pop()


# [1, 7, 9, 9]
dfs(0, 0)