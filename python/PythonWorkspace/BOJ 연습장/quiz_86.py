T = int(input())

for i in range(1, T+1):
    tc = int(input())
    N = list(map(int, input().split()))
    
    ave = sum(N)/len(N)
    cnt = 0
    for j in N:
        if j <= ave:
            cnt += 1
    print("#{} {}".format(i, cnt))