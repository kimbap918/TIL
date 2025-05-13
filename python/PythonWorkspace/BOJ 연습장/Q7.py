# 현재 점수가 N일때, 
# 자릴수를 기준으로 점수 N을 반으로 나누어 왼쪽 부분의 각 자릿수 합과
# 오른쪽 부분의 자릿수 합을 더한 값이 동일한 상황

# 123,402 라면
# 1+2+3 = 6
# 4+0+2 = 6


N = input()
length = len(N) // 2

n1 = N[:length]
n2 = N[length:]

sum1 = 0
sum2 = 0

for i in range(length):
    sum1 += int(n1[i])
    sum2 += int(n2[i])

if sum1 == sum2:
    print("LUCKY")
else:
    print("READY")


