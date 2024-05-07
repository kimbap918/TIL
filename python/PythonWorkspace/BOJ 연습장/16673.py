# 와인을 사기로 마음먹은 해를 0년 차라고 정의하고, 
# n년 차에는 Kn+Pn2 만큼의 와인을 사는 것을 목표로 했다.
# K는 수빈이의 고려대 애착 정도를 나타내는 상수이고, 
# P는 수빈이의 구매중독 정도를 나타내는 상수
# KC + PC^2

# 1 + 1 = 2
# 1*2 + 1*2^2 + 6
# 3 + 3^2 = 12 

import sys
input = sys.stdin.readline

C, K, P = map(int, input().split())
ans = 0

for i in range(1, C+1):
    ans += K*i + P*i**2

print(ans)