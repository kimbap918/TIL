import math
import sys
from collections import Counter

input = sys.stdin.readline
N = int(input())
a = [] 

for i in range(N):
    a.append(int(input()))
a.sort()
print(int(round((sum(a)/N), 0))) # 1. 산술평균

print(a[math.floor(N/2)]) # 2. 중앙값

cnt_a = Counter(a).most_common()
if len(cnt_a) > 1 and cnt_a[0][1] == cnt_a[1][1]: # 최빈값이 2개 이상이면
    print(cnt_a[1][0]) # 3. 최빈값
else:
    print(cnt_a[0][0]) 

print(max(a) - min(a)) # 4. 범위
