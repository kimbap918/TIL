T = int(input())
for i in range(1, T+1):
    case = int(input())
    sise = list(map(int, input().split()))
    max_value = sise[-1]
    cnt = 0
    for price in range(len(sise)-1, -1, -1): # 역순으로 진행
        if sise[price] < max_value: # 현재 가격이 최대값보다 작을경우
            cnt += max_value-sise[price] # cnt 에 최대값 - 현재값 누적
        else:
            max_value = sise[price] # 최대값을 현재값으로 바꿈
    print("#{0} {1}".format(i, cnt))

# 1. 인덱스의 마지막날과 가격을 비교할것
