_ = int(input())
li = list(map(int, input().split()))
cnt = 0
t = 1
for n in li:
    if n != t:
        cnt += 1
    else:
        t += 1
print(cnt)