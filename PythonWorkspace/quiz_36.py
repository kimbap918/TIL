N = int(input())
D = list(map(int, input().split()))
E = []
F = 0
M = 0

for i in range(N):
    if M < D[i]: # 최대값 구하기
        M = D[i]

for j in range(N):
    E.append(D[j] / M * 100)
    F = (F +E[j])
F = F/N
print(F)