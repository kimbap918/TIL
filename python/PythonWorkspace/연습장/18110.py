import sys
from collections import deque
input = sys.stdin.readline

def round_(n):
    return int(n)+1 if n-int(n) >= 0.5 else int(n)

N = int(input())
rate = round_(N * 0.15)
score = deque(sorted(int(input()) for _ in range(N)))

for i in range(rate):
    score.popleft()
    score.pop()

if sum(score) != 0:
    print(round_((sum(score)/len(score))))
else:
    print(0)
# import decimal

# context = decimal.getcontext()
# context.rounding = decimal.ROUND_HALF_UP
# print(round(decimal.Decimal(2.5), 0))
# print(round(2.5))
# print(round(1.5))
# print(round(0.5))