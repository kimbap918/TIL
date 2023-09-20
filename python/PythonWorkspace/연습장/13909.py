N = int(input())
cnt = 0
# 1부터 열려져 있는 창문 개수는 n이 제곱근일때 수가 증가한다
if N == 1:
    print(N)
elif N == 2:
    print(1)
for i in range(1, N):
    if i*i >= N:
        print(cnt)
        break
    cnt += 1


