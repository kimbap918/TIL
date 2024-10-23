N , k = map(int, input().split()) 

cnt = [[0,0,0,0,0,0],[0,0,0,0,0,0]]
result = 0
for i in range(N):
    sex , grade  = map(int, input().split())
    cnt[sex][grade - 1] += 1

for i in cnt :
    for j in i:
        if j % k == 0:
            result += j//k
        else:
            result += (j//k) + 1
print(result)