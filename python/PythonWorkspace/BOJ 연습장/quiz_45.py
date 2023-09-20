T = int(input())

for k in range(T): # 테스트 케이스 횟수
    R, S = input().split() # 문자개수, 입력문자
    A = list(S) # 입력문자를 담은 리스트
    for j in range(int(R)-1): 
        for i in range(len(A)):
            A[i] += S[i] 
    print(''.join(A)) # 문자열 합치기 join()


