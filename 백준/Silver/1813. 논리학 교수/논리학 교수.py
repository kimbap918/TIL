
N = int(input()) # N = 4
num = list(map(int, input().split())) # 0 1 2 3
res = -1 # 참의 개수 후보

# 0 1 2 3
for i in range(N+1): # 주어진 N만큼 탐색
    cnt = sum(1 for v in num if v == i) # 해당 조건을 만족하면 1을 생성하고, 생성된 1들을 sum
    if cnt == i:
        res = max(res, i)

print(res)