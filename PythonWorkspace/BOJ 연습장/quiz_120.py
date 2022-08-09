N = int(input())
client = list(map(int, input().split()))
dic = {}
cnt = 0

for i in client:
    if i in dic:
        dic[i] += 1
        cnt += 1
    else:
        dic[i] = 1
print(cnt)
