import sys
import math

A, B, V = map(int, sys.stdin.readline().split())
# A미터를 올라가고 B미터를 미끄러진다. 정상의 높이는 V미터
c = (V-B)/(A-B) # 정상-미끄러지는값 / 오르는값-미끄러지는값
                # (5-1) = 4 / ( 2-1 )= 1 = 4)
print(math.ceil(c))

# 2 - 1 > 5 

A, B, V = map(int, sys.stdin.readline().split())
cnt = 0
height = 0

while True:
    cnt += 1
    height += A
    if height == V:
        print(cnt)
        break
    height -= B