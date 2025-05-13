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
            dfs(start, depth+1)
            res.pop()

dfs(0, 0)
