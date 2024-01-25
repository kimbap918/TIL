N, a, b = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(N)]
res = "HAPPY"
t = li[a-1][b-1]
if t < max([li[i][b-1]for i in range(N)]) or t < max([li[a-1][j]for j in range(N)]):
    res = "ANGRY"
print(res)