# A = int(input())
# B = int(input())
# C = int(input())
# D = str(A * B * C) 

# for i in range(10): 
#     print(D.count(str(i)))

A = int(input())
B = int(input())
C = int(input())
D = list(map(int, str(A * B * C))) # A*B*C값 쪼개서 리스트로 저장
cnt = 0 # 카운트
chk = [] # 카운트 값을 담을 배열

for j in range(10): # 0~9까지 
    for i in range(len(D)): # D리스트의 길이만큼
        if D[i] == j: # 리스트 D에 있는 값이 0~9와 각각 맞으면 
            cnt += 1 # 카운트 상승
    chk.append(cnt) # 카운트 값 리스트에 추가
    cnt = 0 # 카운트 초기화

for j in range(len(chk)):
    print(chk[j])

