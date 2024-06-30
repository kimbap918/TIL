def solution(a, b, c, d):
    counts = [0] * 7
    # [0, 0, 0, 0, 0, 0, 0]
    result = 0
    
    # 2, 5, 2, 6
    # 굴려진 주사위 4개의 눈금 빈도를 counts리스트에 넣는다.
    # 예를 들어 2가 2번 나왔으면 counts[2] = 2다.
    for dice in a, b, c, d:
        counts[dice] += 1
        # [0, 0, 2, 0, 0, 1, 1]
    if 4 in counts:
        p = counts.index(4)
        result = 1111 * p
        
    elif 3 in counts:
        p = counts.index(3)
        q = counts.index(1)   
        result = (10*p+q)**2
    
    # print(counts)
    # for i, j in enumerate(counts):
    #     print(i, j)
    
    # 눈금이 같은게 2쌍 있는 경우
    elif counts.count(2) == 2:
        # for i, x in enumerate(counts):
        #     if x == 2:
        #         print(i)
        p, q = [i for i, x in enumerate(counts) if x == 2]
        result = (p+q) * (abs(p-q))
    elif 2 in counts:
        p = counts.index(2)
        q, r = [i for i, x in enumerate(counts) if x == 1]
        result = q*r
    else:
        result = min(a, b, c, d)

    return result