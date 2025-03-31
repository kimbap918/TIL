
def dfs(start):
    if len(res) == 6:
        print(' '.join(map(str, res)))
        return
    

    for i in range(start, K):
        res.append(S[i])
        dfs(i+1)
        res.pop()


while True:
    res = []
    arr = list(map(int, input().split()))
    K, S = arr[:1][0], arr[1:]

    if K == 0:
        break

    dfs(0)
    print()


    