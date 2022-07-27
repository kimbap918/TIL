T = int(input())
p_list = []

for i in range(T): 
    X, Y = map(int, input().split()) # 몸무게, 키 입력받기 
    p_list.append([X,Y]) # 학생의 몸무게를 담은 리스트 

for j in p_list: 
    rank = 1 # 초기값 1
    for k in p_list:
        if j[0] < k[0] and j[1] < k[1]: # 다음사람이 키 몸무게 모두 클 경우에만
            rank += 1 # 카운트가 증가 
    print(rank, end = " ")