N, M = map(int, input().split()) # 숫자의 개수, 선택하는 개수
arr = sorted(list(map(int, input().split())))
res = []
# 2 4 5


def dfs(start, depth):
    # print(f"dfs({start}, {depth}) -> res: {res}")  # 디버깅 출력
    if depth == M:
        print(' '.join(map(str, res)))
        return
        
    for i in range(start, N): # 0부터 숫자개수까지
            res.append(arr[i])
            dfs(i+1, depth+1)
            res.pop()

dfs(0, 0)