N = int(input())
for _ in range(N) :
    M = int(input()) # 미션 수
    cnt = 0	# 최종 도네이션 금액
    lst = []
    for _ in range(M) :
        lst.append(list(map(int, input().split())))
    KDA = list(map(int, input().split()))
    
    for i in lst :
        tmp = 0
        for j in range(3) :
            if j != 1 :	# 킬, 어시스트
                tmp += i[j] * KDA[j]
            else :	# 데스
                tmp -= i[j] * KDA[j]
        if tmp > 0 : # 0보다 큰 경우에만 더해준다
            cnt += tmp
    print(cnt)
