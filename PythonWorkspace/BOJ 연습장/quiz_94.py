# 0 딸기 1 초코 2 바나나

N = int(input())

milk = list(map(int, input().split()))

for i in range(len(milk)):
    cnt = 0
    sum = 0
    for j in range(i+1, len(milk)):
        print(i, j)
    # if milk[i] == 0:
    #     if milk[i+1] == 1:
    #         cnt += 1
    #         sum += cnt 
    #     else:
    #         cnt = 0
    # elif milk[i] == 1:
    #     if milk[i+1] == 2:
    #         cnt += 1
    #         sum += cnt
    #     else:
    #         cnt = 0
    # elif milk[i] == 2:
    #     if milk[i+1] == 0:
    #         cnt += 1
    #         sum += cnt
    #     else:
    #         cnt = 0
print(cnt)
