# 동적 프로그래밍 문제

# A공간에서 B공간으로 이동할 때 비용이 최소인 방법을 구한다.
# 단, 이동은 한번에 최대 3칸까지 이동할 수 있다.

# 1. 그리디와 동적 프로그래밍 판단하기
# 2. 점화식 세우기
# 3. N이 1000만 이라면?

# 1) greedy -> 현재 사건이 다음 사건에 영향을 끼치면 사용불가
# A 3 1 3 1 3 1 B
# 무조건 3칸을 이동하면, 1을 선택해야 유리할 때 선택이 불가능

# 앞의 최소값으로 이동할때
# A 3 4 5 2 B
# 3, 2를 선택하면 5의 비용이 들지만, 4를 선택하고 바로 B로 건너가는 방법이 있다.

# 점화식?
# DP = 규칙찾기 = 식으로 정리 = 어렵다
# 1) 최소
# 2) 이동거리의 제약

# dp[i] = cost[i]에 도달할 수 있는 이전의 dp[i-1] [i-2] [i-3] 중에 최소 + cost[i]
# 이 식이 확실한지 알아보려면
# 1) 그리디의 반례를 해결
# 2) 극악의 상황 반례 -> A 9 9 9 1 9 9 9 B

import sys
from collections import deque
input = sys.stdin.readline

# 돌의 개수
N = int(input())

# 돌 마다 독 양을 표현하는 리스트
# B마을에 대한 정의가 필요함.
P = list(map(int, input().split())) + [0]
# 초기값 설정
# 고려해야하는것 
# A 1 2 B = 0
if N < 3:
    print(0)
else:
    dp = deque()
    dp.append(P[0])
    dp.append(P[1])
    dp.append(P[2])

for i in range(3, N+1):
    dp.append(min(dp[0], dp[1], dp[2]) + P[i])
    dp.popleft()

print(dp[-1])