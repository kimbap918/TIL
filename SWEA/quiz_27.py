T = int(input())
for i in range(1, T+1):
    case = int(input())
    sise = list(map(int, input().split()))
    max_value = sise[-1]
    cnt = 0
    for price in range(len(sise)):



    #     if sise_L[price] < sise_L[-1]: # 현재 가격이 마지막날의 
    #         buy += sise_L[price]       # 가격보다 낮을때
    #         cnt += 1 # 값을 누적하고 카운트 증가
    #     if sise_L[price] < sise_L[-1] and cnt > 1:
    #         buy = sise_L[-1]*cnt-buy
    #     if sise_L[price] > sise_L[-1] and cnt >= 1: # 현재 가격이 마지막날의 가격보다 비쌀때
    #         buy = sise_L[price]*cnt-buy # 누적 수량 판매
    #         cnt = 0
    #     elif sise_L[price] > sise_L[-1] and cnt <= 0: # 현재 가격이 마지막날보다 비싸지만 누적 수량이 없을때 
    #         continue

    # print("#{0} {1}".format(i, buy))


# 1. 인덱스의 마지막날과 가격을 비교할것
# 2. 모든 가격이 마지막보다 높으면 0원을 출력할것