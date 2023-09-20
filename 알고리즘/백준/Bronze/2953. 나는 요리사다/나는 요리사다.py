max = 0
idx = 0
for i in range(1, 6): # 1부터 5까지
    sc1, sc2, sc3, sc4 = map(int, input().split()) # 점수 입력
    tot = sc1+sc2+sc3+sc4 # 점수를 다 더한다.
    if max < tot: # 최대값 구하기
        max = tot
        idx = i # 최대값이 있는 인덱스 
print(idx, max)