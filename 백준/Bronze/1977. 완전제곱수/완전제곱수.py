
M = int(input())
N = int(input())
sum = 0
min = 0

for i in range(1, 101): # M, N은 10000이하의 자연수 -> sum의 최대값은 100
    if M <= i*i and N >= i*i: # M이상 N이하의 완전제곱수를 구한다.
        if sum == 0:
            min = i*i
        sum += i*i

if sum == 0:
    print(-1)
else:
    print(sum)
    print(min)