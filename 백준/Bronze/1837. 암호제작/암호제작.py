# 입력
P, K = map(int, input().split())

# K까지 나눠지는 수가 있는지 확인
for i in range(2, K):
    if P % i == 0:
        print("BAD", i)
        break
else:
    print("GOOD")