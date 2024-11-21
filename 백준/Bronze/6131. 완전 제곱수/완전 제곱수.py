N = int(input())

cnt = 0

for i in range(1, 501):
    for j in range(1, 501):
        if i**2 - j**2 == N:
            cnt+=1

print(cnt)