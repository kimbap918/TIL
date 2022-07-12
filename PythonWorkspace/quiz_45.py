T = int(input())

for k in range(T):
    R, S = input().split()
    A = list(S) 
    for j in range(int(R)-1):
        for i in range(len(A)):
            A[i] += S[i]
    print(''.join(A)) # 문자열 합치기 join()


