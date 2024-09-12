#10040 투표
N, M = map(int, input().split(" ")) #N:경기수 M:심사위원수
A = []  #각 경기들의 비용을 재밌는 순서대로
B = []  #심사기준
C = []
for i in range(N):
    A.append(int(input()))
for j in range(M):
    B.append(int(input()))
for i in range(N):
    C.append(0)
for j in range(M):
    for i in range(N):
        if A[i] <= B[j]:
            C[i] += 1
            break
print(C.index(max(C)) + 1)